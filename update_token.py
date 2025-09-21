#!/usr/bin/env python3
"""
Script to help update the bot token in .env file
"""

import os

def update_bot_token():
    """Update the bot token in .env file"""
    print("🤖 Bot Token Updater")
    print("=" * 30)
    
    # Check if .env exists
    if not os.path.exists('.env'):
        print("❌ .env file not found!")
        return False
    
    # Read current .env
    with open('.env', 'r') as f:
        content = f.read()
    
    print("Current .env content:")
    print("-" * 20)
    print(content)
    print("-" * 20)
    
    # Get new token from user
    print("\n📝 Please enter your bot token from @BotFather:")
    print("(It should look like: 123456789:ABCdefGHIjklMNOpqrsTUVwxyz)")
    new_token = input("Bot Token: ").strip()
    
    if not new_token or new_token == "your_bot_token_here":
        print("❌ Invalid token! Please enter a real bot token.")
        return False
    
    # Update the content
    updated_content = content.replace("TELEGRAM_BOT_TOKEN=your_bot_token_here", f"TELEGRAM_BOT_TOKEN={new_token}")
    
    # Write back to .env
    with open('.env', 'w') as f:
        f.write(updated_content)
    
    print("✅ Bot token updated successfully!")
    print("\nUpdated .env content:")
    print("-" * 20)
    print(updated_content)
    print("-" * 20)
    
    return True

def main():
    """Main function"""
    print("🌍 Language Agnostic Translator - Token Updater")
    print("=" * 50)
    
    print("\n📋 Before we start, you need to get a bot token from Telegram:")
    print("1. Open Telegram")
    print("2. Search for @BotFather")
    print("3. Send /newbot")
    print("4. Follow the instructions")
    print("5. Copy the bot token")
    
    input("\nPress Enter when you have your bot token...")
    
    if update_bot_token():
        print("\n🎉 Token updated! Now you can run your bot:")
        print("python run_telegram_bot.py")
    else:
        print("\n❌ Failed to update token. Please try again.")

if __name__ == '__main__':
    main()
