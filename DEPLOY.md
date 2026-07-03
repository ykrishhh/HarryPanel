# Deploy HarryPanel to Railway

## Option 1: One-Click Deploy (Recommended)

1. Click the button below:

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/new)

2. Connect your GitHub account
3. Select the `ykrishhh/HarryPanel` repository
4. Railway will automatically detect the Nixpacks builder
5. Click "Deploy"

## Option 2: CLI Deploy

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Initialize project
cd HarryPanel
railway init

# Deploy
railway up

# Check status
railway status
```

## Option 3: Docker Deploy

```bash
# Build image
docker build -t harrypanel .

# Run container
docker run -p 5000:5000 harrypanel
```

## Environment Variables

Set these in Railway dashboard:

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port | 5000 |
| `SECRET_KEY` | Flask secret key | Auto-generated |

## Post-Deploy

After deployment, your panel will be available at:
`https://your-project.up.railway.app`

## Troubleshooting

### Build fails
- Check that `requirements.txt` includes all dependencies
- Verify Python version compatibility

### App crashes on start
- Check Railway logs: `railway logs`
- Ensure PORT env var is set

### Terminal not working
- SocketIO requires WebSocket support
- Railway supports this by default
