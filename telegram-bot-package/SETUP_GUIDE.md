# 🚀 ProBot Setup Guide

Complete step-by-step guide to get your Telegram bot running in minutes!

## 📋 Prerequisites

### What You Need:
1. ✅ Python 3.8+ installed
2. ✅ Telegram account
3. ✅ Internet connection
4. ✅ Computer/server to run the bot

### Check Python Version:
```bash
python --version
# Should show Python 3.8 or higher
```

## 🔧 Step-by-Step Setup

### Step 1: Get Your Bot Token

1. Open Telegram
2. Search for [@BotFather](https://t.me/botfather)
3. Start a chat and send `/newbot`
4. Choose a name for your bot (e.g., "My ProBot")
5. Choose a username (must end in 'bot', e.g., "my_probot")
6. Copy the token provided (looks like: `123456789:ABCdefGHIjklMNOpqrSTUvwxyz`)

### Step 2: Get Your Admin User ID

1. Search for [@userinfobot](https://t.me/userinfobot) on Telegram
2. Start the bot
3. Copy your user ID number

### Step 3: Install the Bot

#### Option A: Automated Setup (Recommended)
```bash
python setup.py setup
```

#### Option B: Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Create directories
mkdir logs uploads data backups

# Create environment file
cp .env.example .env
```

### Step 4: Configure Your Bot

1. Edit the `.env` file:
   ```
   # Required settings
   TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrSTUvwxyz
   ADMIN_IDS=123456789
   
   # Optional settings (leave blank for now)
   OPENAI_API_KEY=
   WEATHER_API_KEY=
   NEWS_API_KEY=
   ```

2. Replace with your actual values:
   - `TELEGRAM_BOT_TOKEN`: Your bot token from BotFather
   - `ADMIN_IDS`: Your user ID from userinfobot

### Step 5: Test Your Bot

1. Run the bot:
   ```bash
   python telegram_bot.py
   ```

2. You should see:
   ```
   Starting ProBot...
   ```

3. Open Telegram and find your bot
4. Send `/start` command
5. If you get a welcome message, success! 🎉

## ⚙️ Configuration Options

### Basic Settings
Edit `config.py` to customize:

```python
# Bot identity
BOT_NAME = "Your Bot Name"
BOT_DESCRIPTION = "Your bot description"

# Features to enable/disable
FEATURES = {
    'ai_chat': True,
    'file_processing': True,
    'user_management': True,
    'analytics': True,
    'admin_panel': True,
    # ... more features
}

# Custom messages
MESSAGES = {
    'welcome': "Welcome to my custom bot!",
    'help': "Here's how to use my bot...",
    # ... more messages
}
```

### Bot Types
Choose a pre-configured setup:

#### Business Bot (Customer Support)
```python
# In config.py, use business configuration
FEATURES = QuickSetup.business_bot()['features']
MESSAGES = QuickSetup.business_bot()['messages']
```

#### Community Bot (Group Management)
```python
# In config.py, use community configuration
FEATURES = QuickSetup.community_bot()['features']
MESSAGES = QuickSetup.community_bot()['messages']
```

#### Simple Bot (Basic Features)
```python
# In config.py, use simple configuration
FEATURES = QuickSetup.simple_bot()['features']
MESSAGES = QuickSetup.simple_bot()['messages']
```

## 🚀 Running Your Bot

### Development Mode
```bash
python telegram_bot.py
```

### Production Mode
For 24/7 operation, use:

#### On Linux/Mac:
```bash
# Using nohup
nohup python telegram_bot.py &

# Using screen
screen -S bot
python telegram_bot.py
# Press Ctrl+A+D to detach

# Using systemd (advanced)
# See production guide below
```

#### On Windows:
```bash
# Using start
start python telegram_bot.py

# Using Windows Task Scheduler
# Set up scheduled task to run bot.py
```

## 🔍 Testing Checklist

### Basic Functionality:
- [ ] Bot responds to `/start`
- [ ] Welcome message appears
- [ ] `/help` command works
- [ ] `/features` command works
- [ ] Admin panel accessible (if admin)

### Advanced Features:
- [ ] File upload handling
- [ ] Photo processing
- [ ] Statistics tracking
- [ ] User management
- [ ] Error handling

### Error Testing:
- [ ] Invalid commands handled gracefully
- [ ] Bot doesn't crash on errors
- [ ] Logs are created in `logs/` folder

## 🛠️ Troubleshooting

### Common Issues:

#### "Bot doesn't respond"
- Check if bot is running: `python telegram_bot.py`
- Verify token in `.env` file
- Check internet connection
- Look for errors in console

#### "Module not found error"
- Install dependencies: `pip install -r requirements.txt`
- Check Python version: `python --version`
- Try: `pip install --upgrade -r requirements.txt`

#### "Permission denied"
- On Linux/Mac: `chmod +x telegram_bot.py`
- Run with: `python telegram_bot.py`

#### "Bot token invalid"
- Get new token from @BotFather
- Copy token exactly as provided
- No spaces or extra characters

### Getting Help:
1. Check logs in `logs/` folder
2. Review error messages
3. Verify configuration
4. Test with minimal setup
5. Contact support if needed

## 📊 Production Deployment

### For Serious Business Use:

#### 1. VPS Setup:
```bash
# On your VPS
apt update && apt upgrade -y
apt install python3 python3-pip git

# Clone your bot
git clone your-bot-repo
cd your-bot-repo
pip install -r requirements.txt

# Run with process manager
nohup python telegram_bot.py &
```

#### 2. Using PM2 (Recommended):
```bash
# Install PM2
npm install -g pm2

# Start bot with PM2
pm2 start telegram_bot.py --name probot --interpreter python3

# Monitor
pm2 status
pm2 logs probot
pm2 restart probot
```

#### 3. Using systemd:
```bash
# Create service file
sudo nano /etc/systemd/system/probot.service

# Add content:
[Unit]
Description=ProBot Telegram Bot
After=network.target

[Service]
Type=simple
User=youruser
WorkingDirectory=/path/to/bot
ExecStart=/usr/bin/python3 telegram_bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target

# Enable and start
sudo systemctl enable probot
sudo systemctl start probot
```

## 🔒 Security Best Practices

1. **Keep token secure**
   - Don't share bot token
   - Use environment variables
   - Don't commit token to git

2. **Admin access**
   - Only add trusted admins
   - Use specific user IDs
   - Review admin actions

3. **Regular maintenance**
   - Update dependencies
   - Monitor logs
   - Backup data
   - Check for updates

## 📈 Next Steps

### After Setup:
1. **Customize** the bot for your needs
2. **Test** all features thoroughly
3. **Brand** with your identity
4. **Deploy** to production
5. **Monitor** performance
6. **Scale** as needed

### Advanced Customization:
- Add custom commands
- Integrate external APIs
- Modify response logic
- Enhance admin features
- Add database support

---

## 🆘 Need Help?

**Quick Support Options:**
1. 📚 Check this guide again
2. 🔍 Review error messages
3. 📋 Check configuration files
4. 📧 Contact support: [Your support contact]

**Response Time:** Within 24 hours

---

<p align="center">
  <b>🎉 Congratulations!</b><br>
  Your ProBot is ready to serve users! 🤖
</p>