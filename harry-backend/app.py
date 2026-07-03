import os
import subprocess
import time as _time
from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO

# psutil mock for Android/Termux (no native build support)
class _Psutil:
    def cpu_percent(self, interval=0): return 12.5
    def cpu_count(self): return 4
    def cpu_freq(self): return type('F', (), {'current': 1800})()
    def virtual_memory(self): return type('M', (), {'total': 4*1024**3, 'used': int(2.5*1024**3), 'percent': 62})()
    def disk_usage(self, p): return type('D', (), {'total': 128*1024**3, 'used': int(58*1024**3), 'percent': 45})()
    def boot_time(self): return _time.time() - 86400
    def process_iter(self, attrs):
        procs = [
            {'pid':1,'name':'init','cpu_percent':0.1,'memory_percent':0.2,'status':'running'},
            {'pid':2,'name':'kworker/0:1','cpu_percent':0.5,'memory_percent':0.1,'status':'running'},
            {'pid':127,'name':'sshd','cpu_percent':0.0,'memory_percent':0.8,'status':'sleeping'},
            {'pid':337,'name':'python3','cpu_percent':15.3,'memory_percent':8.2,'status':'running'},
            {'pid':412,'name':'node','cpu_percent':3.2,'memory_percent':4.1,'status':'running'},
            {'pid':501,'name':'nginx','cpu_percent':0.3,'memory_percent':1.2,'status':'sleeping'},
            {'pid':612,'name':'cron','cpu_percent':0.0,'memory_percent':0.3,'status':'sleeping'},
            {'pid':723,'name':'dbus-daemon','cpu_percent':0.0,'memory_percent':0.4,'status':'sleeping'},
        ]
        class _P:
            def __init__(self, d): self._d = d
            def __getitem__(self, k): return self._d.get(k)
            @property
            def info(self): return self._d
        return [_P(p) for p in procs]

psutil = _Psutil()

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = os.urandom(24)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/server/info')
def server_info():
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    boot = psutil.boot_time()
    return jsonify({
        'cpu': {'percent': psutil.cpu_percent(), 'count': psutil.cpu_count(), 'freq': psutil.cpu_freq().current},
        'memory': {'total': mem.total, 'used': mem.used, 'percent': mem.percent},
        'disk': {'total': disk.total, 'used': disk.used, 'percent': disk.percent},
        'boot_time': boot, 'uptime': _time.time() - boot,
    })

@app.route('/api/server/processes')
def server_processes():
    procs = []
    for p in psutil.process_iter(['pid','name','cpu_percent','memory_percent','status']):
        try:
            info = p.info
            procs.append({'pid':info['pid'],'name':info['name'],'cpu':info['cpu_percent'] or 0,'memory':round(info['memory_percent'] or 0,1),'status':info['status']})
        except: pass
    procs.sort(key=lambda x: x['cpu'], reverse=True)
    return jsonify(procs[:50])

@app.route('/api/server/services')
def server_services():
    services = []
    for svc in ['nginx','apache2','mysql','postgresql','redis','docker','ssh','cron']:
        try:
            result = subprocess.run(['pgrep', '-x', svc], capture_output=True, text=True, timeout=3)
            status = 'active' if result.returncode == 0 else 'inactive'
        except: status = 'unknown'
        services.append({'name': svc, 'status': status})
    return jsonify(services)

@app.route('/api/files/list')
def files_list():
    path = request.args.get('path', os.path.expanduser('~'))
    entries = []
    try:
        for name in os.listdir(path):
            full = os.path.join(path, name)
            try:
                stat = os.stat(full)
                entries.append({'name':name,'path':full,'is_dir':os.path.isdir(full),'size':stat.st_size,'modified':stat.st_mtime,'mode':oct(stat.st_mode)[-3:]})
            except OSError: continue
    except PermissionError:
        return jsonify({'error':'Permission denied','path':path}), 403
    entries.sort(key=lambda x: (not x['is_dir'], x['name'].lower()))
    return jsonify({'path':path,'entries':entries})

@app.route('/api/files/read')
def files_read():
    path = request.args.get('path','')
    try:
        with open(path,'r',errors='replace') as f: content = f.read(100000)
        return jsonify({'path':path,'content':content})
    except Exception as e: return jsonify({'error':str(e)}), 400

@app.route('/api/db/list')
def db_list():
    dbs = []
    home = os.path.expanduser('~')
    for f in os.listdir(home):
        if f.endswith(('.db','.sqlite','.sqlite3')):
            full = os.path.join(home, f)
            dbs.append({'name':f,'path':full,'size':os.path.getsize(full)})
    return jsonify(dbs)

@app.route('/api/db/tables')
def db_tables():
    import sqlite3
    path = request.args.get('path','')
    try:
        conn = sqlite3.connect(path)
        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]
        result = {}
        for t in tables:
            cursor = conn.execute(f'SELECT COUNT(*) FROM [{t}]')
            count = cursor.fetchone()[0]
            cursor = conn.execute(f'PRAGMA table_info([{t}])')
            cols = [row[1] for row in cursor.fetchall()]
            result[t] = {'count':count,'columns':cols}
        conn.close()
        return jsonify(result)
    except Exception as e: return jsonify({'error':str(e)}), 400

@app.route('/api/db/query', methods=['POST'])
def db_query():
    import sqlite3
    data = request.json
    path = data.get('path','')
    query = data.get('query','')
    try:
        conn = sqlite3.connect(path)
        conn.row_factory = sqlite3.Row
        cursor = conn.execute(query)
        if query.strip().upper().startswith(('INSERT','UPDATE','DELETE','CREATE','DROP')):
            conn.commit()
            return jsonify({'affected':cursor.rowcount})
        rows = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return jsonify({'rows':rows,'count':len(rows)})
    except Exception as e: return jsonify({'error':str(e)}), 400

@app.route('/api/deploy/status')
def deploy_status():
    return jsonify({'repo':'ykrishhh/HarryPanel','branch':'main','last_deploy':'2026-07-03T12:59:03Z','status':'active','url':'https://harrypanel.up.railway.app'})

@socketio.on('terminal_exec')
def handle_terminal_exec(data):
    cmd = data.get('command','')
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30, cwd=os.path.expanduser('~'))
        output = result.stdout + result.stderr
        socketio.emit('terminal_output', {'output': output[:5000]})
    except subprocess.TimeoutExpired:
        socketio.emit('terminal_output', {'output':'Command timed out (30s limit)'})
    except Exception as e:
        socketio.emit('terminal_output', {'output':f'Error: {str(e)}'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port, debug=True, allow_unsafe_werkzeug=True)
