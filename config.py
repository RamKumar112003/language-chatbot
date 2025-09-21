import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')

# Translation Configuration
DEFAULT_TARGET_LANGUAGE = 'en'  # English as default target
SUPPORTED_LANGUAGES = {
    'en': 'English',
    'es': 'Spanish', 
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'ja': 'Japanese',
    'ko': 'Korean',
    'zh': 'Chinese',
    'ar': 'Arabic',
    'hi': 'Hindi',
    'th': 'Thai',
    'vi': 'Vietnamese',
    'tr': 'Turkish',
    'pl': 'Polish',
    'nl': 'Dutch',
    'sv': 'Swedish',
    'da': 'Danish',
    'no': 'Norwegian'
}

# Bot Commands
COMMANDS = {
    'start': 'Start the bot and see available commands',
    'help': 'Show help information',
    'translate': 'Translate text to a specific language',
    'detect': 'Detect the language of the text',
    'languages': 'Show supported languages',
    'set_lang': 'Set your preferred target language'
}