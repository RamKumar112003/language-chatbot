#!/usr/bin/env python3
"""
Telegram Bot Runner - Ensures correct Python interpreter
"""

import sys
import os
import subprocess

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 7:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} is not compatible (need 3.7+)")
        return False

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import telegram
        import flask
        from translator import LanguageTranslator
        print("✅ All required packages are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def main():
    """Main function to run the Telegram bot"""
    print("🤖 Language Agnostic Telegram Bot Runner")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Check for .env file
    if not os.path.exists('.env'):
        print("⚠️  .env file not found!")
        print("Please create .env file with your bot token:")
        print("TELEGRAM_BOT_TOKEN=your_bot_token_here")
        print("\nYou can copy env_example.txt to .env and edit it.")
        
        # Ask if user wants to create .env file
        response = input("\nDo you want to create .env file now? (y/n): ").lower().strip()
        if response == 'y':
            if os.path.exists('env_example.txt'):
                with open('env_example.txt', 'r') as src:
                    content = src.read()
                with open('.env', 'w') as dst:
                    dst.write(content)
                print("✅ .env file created from template")
                print("⚠️  Please edit .env file and add your bot token!")
            else:
                print("❌ env_example.txt not found!")
                sys.exit(1)
        else:
            print("❌ Cannot run bot without .env file")
            sys.exit(1)
    
    # Run the bot
    print("\n🚀 Starting Telegram Bot...")
    print("Press Ctrl+C to stop the bot")
    print("=" * 50)
    
    try:
        # Import and run the bot
        from telegram_bot import main as bot_main
        bot_main()
    except KeyboardInterrupt:
        print("\n👋 Bot stopped by user")
    except Exception as e:
        print(f"\n❌ Error running bot: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
