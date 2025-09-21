#!/usr/bin/env python3
"""
Setup script for the Language Agnostic Telegram Bot
"""

import os
import sys
import subprocess

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required!")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version {sys.version.split()[0]} is compatible")
    return True

def create_env_file():
    """Create .env file if it doesn't exist"""
    if not os.path.exists('.env'):
        if os.path.exists('env_example.txt'):
            print("🔄 Creating .env file from template...")
            with open('env_example.txt', 'r') as src:
                content = src.read()
            with open('.env', 'w') as dst:
                dst.write(content)
            print("✅ .env file created")
            print("⚠️  Please edit .env file and add your bot token!")
        else:
            print("❌ env_example.txt not found!")
            return False
    else:
        print("✅ .env file already exists")
    return True

def main():
    """Main setup function"""
    print("🌍 Language Agnostic Telegram Bot Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not run_command("pip install -r requirements.txt", "Installing dependencies"):
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Create .env file
    if not create_env_file():
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Edit .env file and add your Telegram bot token")
    print("2. Get a bot token from @BotFather on Telegram")
    print("3. Run the bot using: python run_bot.py")
    print("4. Or run directly: python telegram_bot.py")
    
    # Check if .env has been configured
    with open('.env', 'r') as f:
        content = f.read()
        if 'your_bot_token_here' in content:
            print("\n⚠️  Remember to update your bot token in the .env file!")

if __name__ == '__main__':
    main()
