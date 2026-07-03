<div align="center">

<img src="assets/logo.svg" width="380" alt="HarryPanel">

# HarryPanel

**The control panel you can deploy in 60 seconds on any cloud.**

[![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/ykrishhh/HarryPanel?style=flat-square&color=cyan)](https://github.com/ykrishhh/HarryPanel)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?style=flat-square)](https://python.org)
[![Deploy](https://img.shields.io/badge/Deploy-Railway-black.svg?style=flat-square)](https://railway.com)

</div>

---

HarryPanel is a lightweight, Python-based web hosting control panel that runs anywhere — Railway, Render, Fly.io, or your own VPS. No SSH required. No root access needed. Just deploy and manage.

Unlike traditional panels (HestiaCP, 1Panel, CyberPanel) that require dedicated servers and root shell access, HarryPanel works on any cloud platform with a single `git push`.

## Quick Start

```bash
git clone https://github.com/ykrishhh/HarryPanel.git
cd HarryPanel/harry-backend
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000`

## Deploy to Railway

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/new)

```bash
railway login
railway init
railway up
```

## Features

- **Real-time Dashboard** — CPU, memory, and disk monitoring with live updates
- **Process Manager** — View and manage running processes by CPU/memory usage
- **Service Monitor** — Check status of system services (nginx, mysql, docker, etc.)
- **File Manager** — Browse directories, view files, navigate your server
- **Database Admin** — SQLite browser with query editor
- **Web Terminal** — Remote shell via WebSocket — no SSH client needed
- **Deployment Ready** — One-click deploy to Railway, Render, or any Docker host

## Why HarryPanel?

| Feature | HarryPanel | HestiaCP | 1Panel | CyberPanel |
|---------|-----------|----------|--------|------------|
| **Deploy anywhere** | Any cloud | VPS only | VPS only | VPS only |
| **Root required** | No | Yes | Yes | Yes |
| **Install time** | 60 seconds | 30+ minutes | 10+ minutes | 15+ minutes |
| **Stack** | Python/Flask | Bash/PHP | Go/Vue | Python/Django |
| **Resource usage** | ~50MB RAM | ~256MB RAM | ~512MB RAM | ~384MB RAM |

## Tech Stack

`Python` `Flask` `SocketIO` `SQLite` `HTML/CSS/JS`

## Screenshots

<div align="center">

*Dashboard with real-time monitoring*

<img src="docs/screenshots/dashboard.png" width="800" alt="Dashboard">

</div>

> Screenshots coming soon. Want to help? Open a PR with a screenshot of your HarryPanel instance.

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

[MIT License](LICENSE) — Built by [ykrishhh](https://github.com/ykrishhh)

---

<div align="center">

**Star this repo if you find it useful!** ⭐

</div>
