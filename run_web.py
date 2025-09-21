#!/usr/bin/env python3
"""
Web application launcher for the Language Agnostic Translator
"""

import os
import sys
from dotenv import load_dotenv

def check_environment():
    """Check if environment is properly set up"""
    load_dotenv()
    
    # Check if required packages are installed
    try:
        import flask
        import flask_cors
        from translator import LanguageTranslator
        print("✅ All required packages are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def main():
    """Main function to run the web application"""
    print("🌍 Language Agnostic Translator - Web Application")
    print("=" * 50)
    
    if not check_environment():
        sys.exit(1)
    
    # Test translator
    try:
        from translator import LanguageTranslator
        translator = LanguageTranslator()
        print("✅ Translator initialized successfully")
    except Exception as e:
        print(f"❌ Translator error: {e}")
        sys.exit(1)
    
    # Get configuration
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    print(f"\n🚀 Starting web application...")
    print(f"📱 Open http://localhost:{port} in your browser")
    print(f"🔧 Debug mode: {'ON' if debug else 'OFF'}")
    print(f"⏹️  Press Ctrl+C to stop")
    
    try:
        from web_app import app
        app.run(host='0.0.0.0', port=port, debug=debug)
    except KeyboardInterrupt:
        print("\n👋 Web application stopped by user")
    except Exception as e:
        print(f"\n❌ Error starting web application: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
