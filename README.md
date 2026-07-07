<div align="center">

# HarryPanel

**Self-Hosted Server Management Panel — Deploy, Monitor & Manage Infrastructure**

[![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen?style=for-the-badge)](https://github.com/ykrishhh/HarryPanel)
[![Language](https://img.shields.io/badge/Language-Python%20%7C%20HTML%20%7C%20CSS-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![Framework](https://img.shields.io/badge/Framework-Flask-000000?style=for-the-badge&logo=flask&logoColor=white)]()
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/ykrishhh/HarryPanel?style=for-the-badge&color=yellow)](https://github.com/ykrishhh/HarryPanel/stargazers)
[![Forks](https://img.shields.io/github/forks/ykrishhh/HarryPanel?style=for-the-badge&color=orange)](https://github.com/ykrishhh/HarryPanel/network)
[![Issues](https://img.shields.io/github/issues/ykrishhh/HarryPanel?style=for-the-badge&color=red)](https://github.com/ykrishhh/HarryPanel/issues)

</div>

---

## 🎯 Overview

**HarryPanel** is a lightweight, self-hosted server management dashboard built for developers and sysadmins who want full control over their infrastructure without the bloat of enterprise solutions. Deploy applications, monitor system health, manage services, and execute commands — all from a clean, terminal-inspired web interface.

---

## 🏗️ Architecture

```mermaid
graph TB
    subgraph "Frontend"
        UI[Dashboard UI]
        WS[WebSocket Client]
        TERM[Terminal Emulator]
    end

    subgraph "Backend (Flask)"
        API[REST API]
        AUTH[JWT Auth]
        PROC[Process Manager]
        MON[System Monitor]
        DEPLOY[Deployment Engine]
        WS_SRV[WebSocket Server]
    end

    subgraph "System Layer"
        SYSTEMD[systemd]
        DOCKER[Docker Engine]
        NGINX[Nginx]
        LOGS[Log Files]
        METRICS[/proc, /sys, psutil]
    end

    UI --> API
    UI --> WS
    TERM --> WS_SRV
    API --> AUTH
    API --> PROC
    API --> MON
    API --> DEPLOY
    WS_SRV --> PROC
    PROC --> SYSTEMD
    PROC --> DOCKER
    MON --> METRICS
    DEPLOY --> NGINX
    DEPLOY --> SYSTEMD
```

---

## 🚀 Features

### 📊 System Monitoring
| Feature | Description |
|---------|-------------|
| **Real-time CPU/RAM/Disk** | Live charts with WebSocket updates |
| **Process List** | Searchable, sortable, kill/restart actions |
| **Network I/O** | Per-interface bandwidth, connections |
| **Temperature Sensors** | lm-sensors integration |
| **Service Status** | systemd unit monitoring & control |

### 🚢 Deployment Management
| Feature | Description |
|---------|-------------|
| **Git-based Deploys** | Pull, build, deploy from any git repo |
| **Docker Support** | Compose up/down, image management |
| **Static Sites** | One-click Hugo, Jekyll, Next.js exports |
| **Nginx Config** | Auto-generate & manage vhosts |
| **SSL/TLS** | Let's Encrypt integration (certbot) |
| **Rollbacks** | One-click previous version restore |

### 🖥️ Remote Terminal
- Full PTY-based terminal in browser (xterm.js)
- Multiple concurrent sessions
- Command history & autocomplete
- Copy/paste support

### 🔐 Security
- JWT-based authentication
- Rate limiting on auth endpoints
- Optional 2FA (TOTP)
- Audit logging for all actions
- IP allowlist support

---

## ⚡ Quick Start

### Requirements
- Linux server (Ubuntu 20.04+, Debian 11+, RHEL 8+)
- Python 3.10+
- systemd (for service management)
- Docker (optional, for container deployments)
- Nginx (for reverse proxy)

### Installation
```bash
# Clone repository
git clone https://github.com/ykrishhh/HarryPanel.git
cd HarryPanel

# Create virtual environment
python -m venv venv && source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize database
flask --app harrypanel db upgrade

# Create admin user
flask --app harrypanel create-admin --username admin --email admin@example.com
```

### Configuration
```bash
# Copy config template
cp config.example.yaml config.yaml

# Edit configuration
# ├── secret_key: "your-secret-key"
# ├── database_url: "sqlite:///harrypanel.db"
# ├── jwt_expiry_hours: 24
# ├── allow_registration: false
# ├── ssh_key_path: "/home/user/.ssh/id_rsa"
# └── nginx_sites_path: "/etc/nginx/sites-available"
```

### Running
```bash
# Development
flask --app harrypanel run --host 0.0.0.0 --port 5000

# Production (with gunicorn)
gunicorn -w 4 -b 0.0.0.0:5000 "harrypanel:create_app()"

# As systemd service
sudo cp harrypanel.service /etc/systemd/system/
sudo systemctl enable --now harrypanel
```

### Nginx Reverse Proxy
```nginx
server {
    listen 80;
    server_name panel.yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

---

## 📁 Project Structure

```
HarryPanel/
├── harrypanel/
│   ├── __init__.py
│   ├── create_app.py           # Flask app factory
│   ├── config.py               # Configuration
│   ├── extensions.py           # SQLAlchemy, JWT, SocketIO
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py             # User model
│   │   ├── server.py           # Server/host model
│   │   ├── deployment.py       # Deployment model
│   │   └── audit.py            # Audit log model
│   ├── api/
│   │   ├── __init__.py
│   │   ├── auth.py             # Login, register, 2FA
│   │   ├── servers.py          # Server CRUD
│   │   ├── deployments.py      # Deployment management
│   │   ├── monitoring.py       # Metrics endpoints
│   │   └── terminal.py         # WebSocket terminal
│   ├── services/
│   │   ├── __init__.py
│   │   ├── systemd.py          # systemd integration
│   │   ├── docker.py           # Docker API wrapper
│   │   ├── nginx.py            # Nginx config generator
│   │   ├── git.py              # Git operations
│   │   ├── ssl.py              # Let's Encrypt / certbot
│   │   └── monitor.py          # psutil-based metrics
│   ├── cli/
│   │   ├── __init__.py
│   │   ├── admin.py            # Admin commands
│   │   └── db.py               # Database commands
│   ├── templates/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── servers.html
│   │   ├── deployments.html
│   │   ├── terminal.html
│   │   └── auth/
│   │       ├── login.html
│   │       └── register.html
│   └── static/
│       ├── css/
│       │   └── main.css        # Terminal-inspired theme
│       ├── js/
│       │   ├── app.js          # Alpine.js app
│       │   ├── terminal.js     # xterm.js integration
│       │   └── charts.js       # Chart.js dashboards
│       └── fonts/
├── migrations/                 # Alembic migrations
├── tests/
│   ├── unit/
│   └── integration/
├── harrypanel.service          # systemd unit
├── requirements.txt
├── pyproject.toml
├── config.example.yaml
├── LICENSE
└── README.md
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Flask 3.x, SQLAlchemy 2.x, Flask-SocketIO |
| **Auth** | PyJWT, pyotp (TOTP), bcrypt |
| **System** | psutil, docker-py, python-systemd |
| **Git** | GitPython |
| **Frontend** | Alpine.js, xterm.js, Chart.js, Tailwind CSS |
| **Database** | SQLite (dev), PostgreSQL (prod) |
| **Process** | gunicorn, systemd |

---

## 🗺️ Roadmap

- [ ] **v0.5** Multi-server management (agent-based)
- [ ] **v0.6** Kubernetes deployment support
- [ ] **v0.7** Database management (PostgreSQL, MySQL, Redis)
- [ ] **v0.8** Backup/restore scheduling
- [ ] **v0.9** Plugin system for custom modules
- [ ] **v1.0** Stable release with full documentation

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">

Made with ❤️ by [Krish](https://github.com/ykrishhh) | [Portfolio](https://harrydev.one) | [Twitter](https://x.com/ykrishhh)

</div>