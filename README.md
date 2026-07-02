<div align="center">

# HarryPanel

**Advanced Web Hosting Control Panel**

A modern, self-hosted control panel for server management — database admin, file manager, deployment tools, and more.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/ykrishhh/HarryPanel?style=for-the-badge&color=yellow)](https://github.com/ykrishhh/HarryPanel)
[![PRs](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge)](https://github.com/ykrishhh/HarryPanel/pulls)

</div>

---

I built HarryPanel because existing control panels are either bloated, ugly, or locked behind paywalls. This one is lightweight, fast, and actually pleasant to use.

## Features

- **Dashboard** — Server stats at a glance: CPU, RAM, disk, network, uptime
- **File Manager** — Browse, upload, download, edit files directly in the browser
- **Database Admin** — MySQL/PostgreSQL/SQLite management with query editor
- **Terminal** — Web-based SSH terminal for remote server access
- **Deployment** — One-click deployments from GitHub/GitLab repos
- **Cron Jobs** — Schedule and manage cron tasks with a visual editor
- **SSL Manager** — Auto-install Let's Encrypt certificates
- **User Management** — Multi-user access with role-based permissions
- **Backup** — Automated backups with restore functionality
- **Docker** — Container management and docker-compose deployment

## Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Python, Flask |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Database** | SQLite (metadata), MySQL/PostgreSQL (managed) |
| **Auth** | JWT + bcrypt |
| **Terminal** | WebSocket + xterm.js |
| **Deployment** | Git, Docker, systemd |

## Quick Start

```bash
# Clone the repo
git clone https://github.com/ykrishhh/HarryPanel.git
cd HarryPanel

# Install dependencies
pip install -r requirements.txt

# Initialize the database
python init_db.py

# Start the server
python app.py
```

Access at `http://your-server:5000`

Default login: `admin` / `admin` (change immediately)

## Architecture

```
HarryPanel/
├── app.py                 # Flask application entry point
├── init_db.py             # Database initialization
├── config.py              # Configuration management
├── requirements.txt       # Python dependencies
├── core/
│   ├── auth.py            # Authentication & authorization
│   ├── file_manager.py    # File operations
│   ├── database.py        # Database management
│   ├── terminal.py        # WebSocket terminal
│   ├── deployer.py        # Git deployment engine
│   ├── cron.py            # Cron job manager
│   ├── ssl.py             # SSL certificate management
│   └── docker.py          # Docker integration
├── templates/
│   ├── dashboard.html     # Main dashboard
│   ├── files.html         # File manager
│   ├── databases.html     # Database admin
│   ├── terminal.html      # Web terminal
│   ├── settings.html      # Settings page
│   └── login.html         # Login page
├── static/
│   ├── css/               # Stylesheets
│   ├── js/                # JavaScript
│   └── img/               # Assets
└── README.md
```

## Configuration

Edit `config.py` or set environment variables:

```python
# config.py
SECRET_KEY = "your-secret-key"
DATABASE = "sqlite:///harrypanel.db"
DEFAULT_PORT = 5000
ALLOWED_HOSTS = ["*"]

# Database connections (for managed databases)
DB_HOST = "localhost"
DB_PORT = 3306
DB_USER = "root"
DB_PASS = ""
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/stats` | Server statistics |
| GET | `/api/files/<path>` | List directory |
| POST | `/api/files/upload` | Upload file |
| GET | `/api/databases` | List databases |
| POST | `/api/query` | Execute SQL query |
| POST | `/api/deploy` | Deploy from git |
| GET | `/api/cron` | List cron jobs |
| POST | `/api/cron` | Create cron job |
| GET | `/api/ssl` | List certificates |
| POST | `/api/ssl/install` | Install SSL cert |

## Security

- All passwords hashed with bcrypt
- JWT tokens for API authentication
- CSRF protection on all forms
- Rate limiting on login attempts
- File upload validation and sandboxing
- SQL injection prevention via parameterized queries

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">

Built by [ykrishhh](https://github.com/ykrishhh) · Security Researcher & Developer

*Contact: [krishy2122@gmail.com](mailto:krishy2122@gmail.com) · [Twitter @harry6ez](https://twitter.com/harry6ez) · [Telegram @harry6e](https://t.me/harry6e)*

</div>

<!-- SEO Keywords: harrypanel, control-panel, web-hosting, server-management, file-manager, database-admin, deployment, self-hosted, python, flask -->
