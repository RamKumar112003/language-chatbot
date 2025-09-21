#!/usr/bin/env python3
"""
Test script for the web application
"""

import requests
import json
import time
import sys

def test_web_app():
    """Test the web application functionality"""
    base_url = "http://localhost:5000"
    
    print("🧪 Testing Web Application")
    print("=" * 40)
    
    # Test 1: Home page
    print("🔄 Testing home page...")
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            print("✅ Home page loads successfully")
        else:
            print(f"❌ Home page failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Home page error: {e}")
        return False
    
    # Test 2: API - Get languages
    print("🔄 Testing languages API...")
    try:
        response = requests.get(f"{base_url}/api/languages")
        if response.status_code == 200:
            data = response.json()
            if data.get('success') and 'languages' in data:
                print(f"✅ Languages API works - {len(data['languages'])} languages")
            else:
                print("❌ Languages API returned invalid data")
                return False
        else:
            print(f"❌ Languages API failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Languages API error: {e}")
        return False
    
    # Test 3: API - Translation
    print("🔄 Testing translation API...")
    try:
        payload = {
            "text": "Hello world",
            "target_lang": "es"
        }
        response = requests.post(f"{base_url}/api/translate", json=payload)
        if response.status_code == 200:
            data = response.json()
            if data.get('success') and 'translated_text' in data:
                print(f"✅ Translation API works - '{data['translated_text']}'")
            else:
                print(f"❌ Translation API returned invalid data: {data}")
                return False
        else:
            print(f"❌ Translation API failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Translation API error: {e}")
        return False
    
    # Test 4: API - Language detection
    print("🔄 Testing language detection API...")
    try:
        payload = {
            "text": "Hola mundo"
        }
        response = requests.post(f"{base_url}/api/detect", json=payload)
        if response.status_code == 200:
            data = response.json()
            if data.get('success') and 'language_code' in data:
                print(f"✅ Language detection API works - {data['language_name']}")
            else:
                print(f"❌ Language detection API returned invalid data: {data}")
                return False
        else:
            print(f"❌ Language detection API failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Language detection API error: {e}")
        return False
    
    # Test 5: Other pages
    print("🔄 Testing other pages...")
    pages = [
        ("/telegram", "Telegram page"),
        ("/about", "About page")
    ]
    
    for url, name in pages:
        try:
            response = requests.get(f"{base_url}{url}")
            if response.status_code == 200:
                print(f"✅ {name} loads successfully")
            else:
                print(f"❌ {name} failed: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ {name} error: {e}")
            return False
    
    print("\n🎉 All tests passed! Web application is working perfectly!")
    return True

def main():
    """Main test function"""
    print("🌍 Language Agnostic Translator - Web App Test Suite")
    print("=" * 60)
    
    # Check if web app is running
    try:
        response = requests.get("http://localhost:5000", timeout=5)
        if response.status_code != 200:
            print("❌ Web application is not running!")
            print("Please start the web app first:")
            print("  python run_web.py")
            return False
    except Exception:
        print("❌ Web application is not running!")
        print("Please start the web app first:")
        print("  python run_web.py")
        return False
    
    # Run tests
    success = test_web_app()
    
    if success:
        print("\n🚀 Your web application is ready for deployment!")
        print("📱 Access it at: http://localhost:5000")
        print("🌐 Deploy to Heroku, Railway, or Render for public access")
    else:
        print("\n❌ Some tests failed. Please check the errors above.")
        return False
    
    return True

if __name__ == '__main__':
    main()
