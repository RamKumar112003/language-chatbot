#!/usr/bin/env python3
"""
Main entry point for the Language Agnostic Telegram Bot
This script allows you to choose between running the private chat bot or channel bot
"""

import os
import sys
from dotenv import load_dotenv

def check_environment():
    """Check if environment variables are properly set"""
    load_dotenv()
    
    if not os.getenv('TELEGRAM_BOT_TOKEN'):
        print("❌ Error: TELEGRAM_BOT_TOKEN not found!")
        print("Please create a .env file with your bot token.")
        print("Copy env_example.txt to .env and add your token.")
        return False
    
    return True

def main():
    """Main function to run the bot"""
    print("🌍 Language Agnostic Telegram Bot")
    print("=" * 40)
    
    if not check_environment():
        sys.exit(1)
    
    print("\nChoose bot mode:")
    print("1. Private Chat Bot (telegram_bot.py)")
    print("2. Channel Bot (channel_bot.py)")
    print("3. Exit")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                print("\n🤖 Starting Private Chat Bot...")
                print("Press Ctrl+C to stop the bot")
                import telegram_bot
                telegram_bot.main()
                break
                
            elif choice == '2':
                print("\n📢 Starting Channel Bot...")
                print("Press Ctrl+C to stop the bot")
                import channel_bot
                channel_bot.main()
                break
                
            elif choice == '3':
                print("👋 Goodbye!")
                sys.exit(0)
                
            else:
                print("❌ Invalid choice. Please enter 1, 2, or 3.")
                
        except KeyboardInterrupt:
            print("\n👋 Bot stopped by user")
            sys.exit(0)
        except Exception as e:
            print(f"❌ Error: {e}")
            sys.exit(1)

if __name__ == '__main__':
    main()
