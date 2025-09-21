#!/usr/bin/env python3
"""
Test script to verify the bot components work correctly
"""

import os
import sys

def test_imports():
    """Test if all modules can be imported"""
    print("🔄 Testing imports...")
    try:
        from translator import LanguageTranslator
        from config import SUPPORTED_LANGUAGES, COMMANDS
        from telegram_bot import TelegramTranslationBot
        from channel_bot import ChannelTranslationBot
        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_translator():
    """Test the translator functionality"""
    print("\n🔄 Testing translator...")
    try:
        from translator import LanguageTranslator
        translator = LanguageTranslator()
        
        # Test language detection
        lang, name = translator.detect_language("Hello world")
        print(f"✅ Language detection: {lang} - {name}")
        
        # Test translation
        result, msg = translator.translate_text("Hello world", "es")
        print(f"✅ Translation: {result}")
        print(f"✅ Message: {msg}")
        
        return True
    except Exception as e:
        print(f"❌ Translator error: {e}")
        return False

def test_config():
    """Test configuration"""
    print("\n🔄 Testing configuration...")
    try:
        from config import SUPPORTED_LANGUAGES, COMMANDS
        
        print(f"✅ Supported languages: {len(SUPPORTED_LANGUAGES)}")
        print(f"✅ Commands: {len(COMMANDS)}")
        
        # Test some language codes
        test_langs = ['en', 'es', 'fr', 'de']
        for lang in test_langs:
            if lang in SUPPORTED_LANGUAGES:
                print(f"✅ Language {lang}: {SUPPORTED_LANGUAGES[lang]}")
            else:
                print(f"❌ Language {lang} not found")
                return False
        
        return True
    except Exception as e:
        print(f"❌ Config error: {e}")
        return False

def test_bot_creation():
    """Test bot creation without starting"""
    print("\n🔄 Testing bot creation...")
    try:
        from telegram_bot import TelegramTranslationBot
        from channel_bot import ChannelTranslationBot
        
        # Test private bot creation
        private_bot = TelegramTranslationBot()
        print("✅ Private bot created successfully")
        
        # Test channel bot creation
        channel_bot = ChannelTranslationBot()
        print("✅ Channel bot created successfully")
        
        return True
    except Exception as e:
        print(f"❌ Bot creation error: {e}")
        return False

def test_environment():
    """Test environment setup"""
    print("\n🔄 Testing environment...")
    
    # Check if .env file exists
    if os.path.exists('.env'):
        print("✅ .env file exists")
    else:
        print("⚠️  .env file not found - you'll need to create it")
    
    # Check Python version
    python_version = sys.version_info
    if python_version >= (3, 7):
        print(f"✅ Python version {python_version.major}.{python_version.minor} is compatible")
    else:
        print(f"❌ Python version {python_version.major}.{python_version.minor} is too old (need 3.7+)")
        return False
    
    return True

def main():
    """Run all tests"""
    print("🧪 Language Agnostic Telegram Bot - Test Suite")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_translator,
        test_config,
        test_bot_creation,
        test_environment
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The bot is ready to run.")
        print("\nNext steps:")
        print("1. Get a bot token from @BotFather on Telegram")
        print("2. Create .env file with your token")
        print("3. Run: python run_bot.py")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return False
    
    return True

if __name__ == '__main__':
    main()
