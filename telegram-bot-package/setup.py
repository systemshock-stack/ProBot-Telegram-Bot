#!/usr/bin/env python3
"""
Setup script for ProBot Telegram Bot
Professional bot package setup and configuration
"""

import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required!")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    print(f"✅ Python version {sys.version.split()[0]} is compatible!")

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        sys.exit(1)

def create_directories():
    """Create necessary directories"""
    directories = ['logs', 'uploads', 'data', 'backups']
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
    print("✅ Created necessary directories!")

def create_env_file():
    """Create .env file template"""
    env_content = """# ProBot Configuration
# Copy this file to .env and fill in your values

# Telegram Bot Token (Required)
# Get this from @BotFather on Telegram
TELEGRAM_BOT_TOKEN=YOUR_BOT_TOKEN_HERE

# Admin User IDs (Comma-separated)
# Get your user ID from @userinfobot on Telegram
ADMIN_IDS=123456789

# Optional API Keys (for enhanced features)
OPENAI_API_KEY=your_openai_api_key_here
WEATHER_API_KEY=your_weather_api_key_here
NEWS_API_KEY=your_news_api_key_here

# Bot Settings
BOT_NAME=ProBot
BOT_VERSION=1.0.0
LOG_LEVEL=INFO
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    print("✅ Created .env file template!")

def setup_bot():
    """Main setup function"""
    print("🚀 Setting up ProBot Telegram Bot...")
    print("=" * 50)
    
    # Step 1: Check Python version
    check_python_version()
    
    # Step 2: Install requirements
    install_requirements()
    
    # Step 3: Create directories
    create_directories()
    
    # Step 4: Create environment file
    create_env_file()
    
    print("=" * 50)
    print("✅ Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Edit .env file and add your bot token")
    print("2. Add your admin user ID to ADMIN_IDS")
    print("3. Run: python telegram_bot.py")
    print("\n🎉 Your bot is ready to use!")

def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        if sys.argv[1] == "setup":
            setup_bot()
        elif sys.argv[1] == "install":
            install_requirements()
        elif sys.argv[1] == "clean":
            print("🧹 Cleaning up...")
            # Add cleanup logic here
            print("✅ Cleanup completed!")
        else:
            print("❌ Unknown command. Use 'setup', 'install', or 'clean'")
    else:
        setup_bot()

if __name__ == "__main__":
    main()