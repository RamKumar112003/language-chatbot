import logging
from deep_translator import GoogleTranslator
from langdetect import detect, LangDetectException
from config import SUPPORTED_LANGUAGES, DEFAULT_TARGET_LANGUAGE
import requests
import json

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LanguageTranslator:
    def __init__(self):
        self.translator = GoogleTranslator()
        
    def detect_language(self, text):
        """
        Detect the language of the given text
        """
        try:
            if not text or not text.strip():
                return None, "Text is empty or invalid"
            
            detected_lang = detect(text)
            language_name = SUPPORTED_LANGUAGES.get(detected_lang, detected_lang)
            return detected_lang, language_name
        except LangDetectException as e:
            logger.error(f"Language detection error: {e}")
            return None, f"Could not detect language: {str(e)}"
        except Exception as e:
            logger.error(f"Unexpected error in language detection: {e}")
            return None, f"Error detecting language: {str(e)}"
    
    def translate_text(self, text, target_lang=None, source_lang=None):
        """
        Translate text to target language
        """
        try:
            if not text or not text.strip():
                return None, "Text is empty or invalid"
            
            if target_lang is None:
                target_lang = DEFAULT_TARGET_LANGUAGE
            
            # Detect source language if not provided
            if source_lang is None:
                source_lang, _ = self.detect_language(text)
                if source_lang is None:
                    return None, "Could not detect source language"
            
            # Don't translate if source and target are the same
            if source_lang == target_lang:
                return text, f"Text is already in {SUPPORTED_LANGUAGES.get(target_lang, target_lang)}"
            
            # Try multiple translation methods
            translated_text = None
            
            # Method 1: Try GoogleTranslator
            try:
                translator = GoogleTranslator(source=source_lang, target=target_lang)
                translated_text = translator.translate(text)
                if translated_text and translated_text != text:
                    source_lang_name = SUPPORTED_LANGUAGES.get(source_lang, source_lang)
                    target_lang_name = SUPPORTED_LANGUAGES.get(target_lang, target_lang)
                    return translated_text, f"Translated from {source_lang_name} to {target_lang_name}"
            except Exception as e:
                logger.warning(f"GoogleTranslator failed: {e}")
            
            # Method 2: Try MyMemory API as fallback
            try:
                url = "https://api.mymemory.translated.net/get"
                params = {
                    'q': text,
                    'langpair': f"{source_lang}|{target_lang}"
                }
                response = requests.get(url, params=params, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    if data.get('responseStatus') == 200:
                        translated_text = data['responseData']['translatedText']
                        if translated_text and translated_text != text:
                            source_lang_name = SUPPORTED_LANGUAGES.get(source_lang, source_lang)
                            target_lang_name = SUPPORTED_LANGUAGES.get(target_lang, target_lang)
                            return translated_text, f"Translated from {source_lang_name} to {target_lang_name}"
            except Exception as e:
                logger.warning(f"MyMemory API failed: {e}")
            
            # If all methods fail, return original text with message
            if not translated_text or translated_text == text:
                return text, f"Translation service unavailable. Text appears to be in {SUPPORTED_LANGUAGES.get(source_lang, source_lang)}"
            
            return translated_text, f"Translated from {SUPPORTED_LANGUAGES.get(source_lang, source_lang)} to {SUPPORTED_LANGUAGES.get(target_lang, target_lang)}"
                
        except Exception as e:
            logger.error(f"Translation error: {e}")
            return None, f"Translation failed: {str(e)}"
    
    def get_supported_languages(self):
        """
        Get list of supported languages
        """
        return SUPPORTED_LANGUAGES
    
    def is_language_supported(self, lang_code):
        """
        Check if language code is supported
        """
        return lang_code in SUPPORTED_LANGUAGES
