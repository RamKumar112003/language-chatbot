from googletrans import Translator, LANGUAGES
import logging
from config import SUPPORTED_LANGUAGES

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TranslationService:
    def __init__(self):
        self.translator = Translator()
    
    def detect_language(self, text):
        """Detect the language of the input text"""
        try:
            detection = self.translator.detect(text)
            return {
                'language': detection.lang,
                'confidence': detection.confidence,
                'language_name': LANGUAGES.get(detection.lang, 'Unknown')
            }
        except Exception as e:
            logger.error(f"Error detecting language: {e}")
            return None
    
    def translate_text(self, text, target_language='en', source_language=None):
        """Translate text to target language"""
        try:
            if source_language:
                result = self.translator.translate(
                    text, 
                    dest=target_language, 
                    src=source_language
                )
            else:
                result = self.translator.translate(text, dest=target_language)
            
            return {
                'original_text': text,
                'translated_text': result.text,
                'source_language': result.src,
                'target_language': result.dest,
                'source_language_name': LANGUAGES.get(result.src, 'Unknown'),
                'target_language_name': LANGUAGES.get(result.dest, 'Unknown'),
                'confidence': getattr(result, 'confidence', None)
            }
        except Exception as e:
            logger.error(f"Error translating text: {e}")
            return None
    
    def get_supported_languages(self):
        """Get list of supported languages"""
        return SUPPORTED_LANGUAGES
    
    def is_language_supported(self, language_code):
        """Check if a language code is supported"""
        return language_code in SUPPORTED_LANGUAGES
    
    def get_language_name(self, language_code):
        """Get the full name of a language from its code"""
        return SUPPORTED_LANGUAGES.get(language_code, 'Unknown')
