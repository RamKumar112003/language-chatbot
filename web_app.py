#!/usr/bin/env python3
"""
Web application for the Language Agnostic Telegram Bot
Provides a web interface for translation and language detection
"""

import os
import json
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
from translator import LanguageTranslator
from config import SUPPORTED_LANGUAGES, COMMANDS
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize translator
translator = LanguageTranslator()

@app.route('/')
def index():
    """Main page with translation interface"""
    return render_template('index.html', 
                         languages=SUPPORTED_LANGUAGES,
                         commands=COMMANDS)

@app.route('/api/translate', methods=['POST'])
def api_translate():
    """API endpoint for translation"""
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        target_lang = data.get('target_lang', 'en')
        source_lang = data.get('source_lang', None)
        
        if not text:
            return jsonify({
                'success': False,
                'error': 'Text is required'
            }), 400
        
        # Translate text
        translated_text, message = translator.translate_text(text, target_lang, source_lang)
        
        if translated_text:
            # Detect source language if not provided
            if not source_lang:
                detected_lang, detected_name = translator.detect_language(text)
                source_lang = detected_lang
                source_name = detected_name
            else:
                source_name = SUPPORTED_LANGUAGES.get(source_lang, source_lang)
            
            target_name = SUPPORTED_LANGUAGES.get(target_lang, target_lang)
            
            return jsonify({
                'success': True,
                'translated_text': translated_text,
                'source_language': source_lang,
                'source_name': source_name,
                'target_language': target_lang,
                'target_name': target_name,
                'message': message
            })
        else:
            return jsonify({
                'success': False,
                'error': message
            }), 400
            
    except Exception as e:
        logger.error(f"Translation error: {e}")
        return jsonify({
            'success': False,
            'error': f'Translation failed: {str(e)}'
        }), 500

@app.route('/api/detect', methods=['POST'])
def api_detect():
    """API endpoint for language detection"""
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({
                'success': False,
                'error': 'Text is required'
            }), 400
        
        # Detect language
        lang_code, lang_name = translator.detect_language(text)
        
        if lang_code:
            return jsonify({
                'success': True,
                'language_code': lang_code,
                'language_name': lang_name,
                'text': text
            })
        else:
            return jsonify({
                'success': False,
                'error': lang_name
            }), 400
            
    except Exception as e:
        logger.error(f"Language detection error: {e}")
        return jsonify({
            'success': False,
            'error': f'Language detection failed: {str(e)}'
        }), 500

@app.route('/api/languages', methods=['GET'])
def api_languages():
    """API endpoint to get supported languages"""
    return jsonify({
        'success': True,
        'languages': SUPPORTED_LANGUAGES
    })

@app.route('/telegram')
def telegram_info():
    """Page with Telegram bot information"""
    return render_template('telegram.html', 
                         languages=SUPPORTED_LANGUAGES,
                         commands=COMMANDS)

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html', languages=SUPPORTED_LANGUAGES)

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Get port from environment or use default
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    print(f"🌍 Starting Language Agnostic Web App on port {port}")
    print(f"🔗 Open http://localhost:{port} in your browser")
    
    app.run(host='0.0.0.0', port=port, debug=debug)
