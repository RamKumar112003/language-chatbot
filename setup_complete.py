#!/usr/bin/env python3
"""
Complete Setup Script for Language Agnostic Translator
This script will set up everything you need to run the bot and web app
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def print_header(title):
    """Print a formatted header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

def run_command(command, description, check=True):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=check, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} completed successfully")
            return True
        else:
            print(f"⚠️  {description} completed with warnings")
            if result.stderr:
                print(f"   Warning: {result.stderr.strip()}")
            return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        if e.stderr:
            print(f"   Error: {e.stderr.strip()}")
        return False

def check_python_version():
    """Check Python version"""
    print_header("CHECKING PYTHON VERSION")
    version = sys.version_info
    if version.major == 3 and version.minor >= 7:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} is not compatible (need 3.7+)")
        return False

def install_dependencies():
    """Install required packages"""
    print_header("INSTALLING DEPENDENCIES")
    return run_command("pip install -r requirements.txt", "Installing Python packages")

def create_env_file():
    """Create .env file if it doesn't exist"""
    print_header("SETTING UP ENVIRONMENT")
    
    if os.path.exists('.env'):
        print("✅ .env file already exists")
        return True
    
    if os.path.exists('env_example.txt'):
        print("🔄 Creating .env file from template...")
        shutil.copy('env_example.txt', '.env')
        print("✅ .env file created")
        print("⚠️  Please edit .env file and add your bot token!")
        return True
    else:
        print("🔄 Creating .env file...")
        with open('.env', 'w') as f:
            f.write("# Telegram Bot Configuration\n")
            f.write("TELEGRAM_BOT_TOKEN=your_bot_token_here\n")
            f.write("TELEGRAM_CHANNEL_ID=your_channel_id_here\n")
        print("✅ .env file created")
        print("⚠️  Please edit .env file and add your bot token!")
        return True

def create_batch_files():
    """Create Windows batch files for easy running"""
    print_header("CREATING BATCH FILES")
    
    # Create run_telegram_bot.bat
    with open('run_telegram_bot.bat', 'w') as f:
        f.write('@echo off\n')
        f.write('echo Starting Telegram Bot...\n')
        f.write('python run_telegram_bot.py\n')
        f.write('pause\n')
    
    # Create run_web_app.bat
    with open('run_web_app.bat', 'w') as f:
        f.write('@echo off\n')
        f.write('echo Starting Web Application...\n')
        f.write('python run_web.py\n')
        f.write('pause\n')
    
    # Create run_bot_selector.bat
    with open('run_bot_selector.bat', 'w') as f:
        f.write('@echo off\n')
        f.write('echo Starting Bot Selector...\n')
        f.write('python run_bot.py\n')
        f.write('pause\n')
    
    print("✅ Batch files created for easy running")

def test_components():
    """Test all components"""
    print_header("TESTING COMPONENTS")
    
    # Test translator
    try:
        from translator import LanguageTranslator
        translator = LanguageTranslator()
        result, msg = translator.translate_text("Hello world", "es")
        print("✅ Translator working")
    except Exception as e:
        print(f"❌ Translator error: {e}")
        return False
    
    # Test web app
    try:
        from web_app import app
        with app.test_client() as client:
            response = client.get('/')
            if response.status_code == 200:
                print("✅ Web app working")
            else:
                print(f"❌ Web app error: {response.status_code}")
                return False
    except Exception as e:
        print(f"❌ Web app error: {e}")
        return False
    
    # Test telegram bot
    try:
        from telegram_bot import TelegramTranslationBot
        bot = TelegramTranslationBot()
        print("✅ Telegram bot working")
    except Exception as e:
        print(f"❌ Telegram bot error: {e}")
        return False
    
    return True

def create_quick_start_guide():
    """Create a quick start guide"""
    print_header("CREATING QUICK START GUIDE")
    
    guide = """# 🚀 QUICK START GUIDE

## How to Run Your Language Agnostic Translator

### Option 1: Double-Click Batch Files (Easiest)
- `run_telegram_bot.bat` - Run Telegram bot
- `run_web_app.bat` - Run web application
- `run_bot_selector.bat` - Choose what to run

### Option 2: VS Code
1. Press F5
2. Select what you want to run:
   - "Run Private Chat Bot"
   - "Run Web Application"
   - "Run Bot Selector"

### Option 3: Command Line
```bash
# Telegram Bot
python run_telegram_bot.py

# Web Application
python run_web.py

# Bot Selector
python run_bot.py
```

## Setup Steps

### 1. Get Bot Token
1. Go to Telegram
2. Search for @BotFather
3. Send /newbot
4. Follow instructions
5. Copy the bot token

### 2. Configure Bot
1. Open .env file
2. Replace `your_bot_token_here` with your actual token
3. Save the file

### 3. Run Your Bot
- Double-click `run_telegram_bot.bat` for Telegram bot
- Double-click `run_web_app.bat` for web app
- Open http://localhost:5000 in your browser

## Features Available

### Web Application
- Real-time translation
- Language detection
- Beautiful responsive UI
- Works on all devices

### Telegram Bot
- Private chat translation
- Channel integration
- Auto language detection
- 20+ languages supported

## Need Help?
- Check README.md for detailed instructions
- Check DEPLOYMENT_GUIDE.md for web deployment
- All files are ready to use!

Happy translating! 🌍🤖
"""
    
    with open('QUICK_START_GUIDE.txt', 'w', encoding='utf-8') as f:
        f.write(guide)
    
    print("✅ Quick start guide created")

def main():
    """Main setup function"""
    print("🌍 Language Agnostic Translator - Complete Setup")
    print("This script will set up everything you need!")
    
    # Check Python version
    if not check_python_version():
        print("\n❌ Setup failed: Python version not compatible")
        return False
    
    # Install dependencies
    if not install_dependencies():
        print("\n❌ Setup failed: Could not install dependencies")
        return False
    
    # Create .env file
    if not create_env_file():
        print("\n❌ Setup failed: Could not create .env file")
        return False
    
    # Create batch files
    create_batch_files()
    
    # Test components
    if not test_components():
        print("\n⚠️  Some components have issues, but setup is mostly complete")
    
    # Create quick start guide
    create_quick_start_guide()
    
    print_header("SETUP COMPLETE! 🎉")
    print("""
✅ Everything is ready to use!

📁 Files created:
   - .env (edit this with your bot token)
   - run_telegram_bot.bat (double-click to run bot)
   - run_web_app.bat (double-click to run web app)
   - run_bot_selector.bat (double-click to choose)
   - QUICK_START_GUIDE.txt (read this first!)

🚀 Next steps:
   1. Get bot token from @BotFather on Telegram
   2. Edit .env file with your token
   3. Double-click run_telegram_bot.bat or run_web_app.bat
   4. Start translating!

🌐 Web app will be available at: http://localhost:5000
🤖 Telegram bot will work once you add your token

Happy translating! 🌍🤖
""")
    
    return True

if __name__ == '__main__':
    main()
