import logging
import asyncio
from telegram import Update, Bot
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from telegram.constants import ParseMode
from translator import LanguageTranslator
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID, SUPPORTED_LANGUAGES

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class ChannelTranslationBot:
    def __init__(self):
        self.translator = LanguageTranslator()
        self.channel_language_preferences = {}  # Store channel language preferences
        
    async def handle_channel_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle messages in the channel"""
        if not update.channel_post:
            return
            
        message = update.channel_post
        text = message.text
        
        if not text or not text.strip():
            return
        
        # Check if message is a translation request
        if text.startswith('/translate'):
            await self.handle_translate_request(message, context)
        elif text.startswith('/detect'):
            await self.handle_detect_request(message, context)
        else:
            # Auto-translate if enabled for this channel
            await self.auto_translate_message(message, context)
    
    async def handle_translate_request(self, message, context: ContextTypes.DEFAULT_TYPE):
        """Handle /translate command in channel"""
        text_parts = message.text.split(' ', 2)
        if len(text_parts) < 3:
            await message.reply_text(
                "Usage: /translate <target_language> <text>\n"
                "Example: /translate es Hello, how are you?"
            )
            return
        
        target_lang = text_parts[1].lower()
        text_to_translate = text_parts[2]
        
        if not self.translator.is_language_supported(target_lang):
            await message.reply_text(
                f"❌ Language code '{target_lang}' is not supported.\n"
                f"Use /languages to see available options."
            )
            return
        
        translated_text, message_info = self.translator.translate_text(text_to_translate, target_lang)
        
        if translated_text:
            source_lang, source_name = self.translator.detect_language(text_to_translate)
            target_name = SUPPORTED_LANGUAGES.get(target_lang, target_lang)
            
            response = f"🔄 *Translation:*\n\n"
            response += f"Original ({source_name}): `{text_to_translate}`\n\n"
            response += f"Translated to {target_name}: `{translated_text}`"
            
            await message.reply_text(response, parse_mode=ParseMode.MARKDOWN)
        else:
            await message.reply_text(f"❌ {message_info}")
    
    async def handle_detect_request(self, message, context: ContextTypes.DEFAULT_TYPE):
        """Handle /detect command in channel"""
        text_parts = message.text.split(' ', 1)
        if len(text_parts) < 2:
            await message.reply_text(
                "Usage: /detect <text>\n"
                "Example: /detect Hello, how are you?"
            )
            return
        
        text = text_parts[1]
        lang_code, lang_name = self.translator.detect_language(text)
        
        if lang_code:
            await message.reply_text(
                f"🔍 *Language Detection:*\n\n"
                f"Text: `{text}`\n"
                f"Detected Language: {lang_name} ({lang_code.upper()})",
                parse_mode=ParseMode.MARKDOWN
            )
        else:
            await message.reply_text(f"❌ {lang_name}")
    
    async def auto_translate_message(self, message, context: ContextTypes.DEFAULT_TYPE):
        """Auto-translate messages in the channel"""
        channel_id = message.chat_id
        
        # Check if auto-translation is enabled for this channel
        if channel_id not in self.channel_language_preferences:
            return
        
        target_lang = self.channel_language_preferences[channel_id]
        text = message.text
        
        # Detect source language
        source_lang, source_name = self.translator.detect_language(text)
        
        # Only translate if source language is different from target
        if source_lang and source_lang != target_lang:
            translated_text, message_info = self.translator.translate_text(text, target_lang, source_lang)
            
            if translated_text:
                target_name = SUPPORTED_LANGUAGES.get(target_lang, target_lang)
                
                response = f"🌐 *Auto Translation:*\n\n"
                response += f"Original ({source_name}): `{text}`\n\n"
                response += f"Translated to {target_name}: `{translated_text}`"
                
                await message.reply_text(response, parse_mode=ParseMode.MARKDOWN)
    
    async def set_channel_language(self, channel_id, target_lang):
        """Set the target language for a channel"""
        if self.translator.is_language_supported(target_lang):
            self.channel_language_preferences[channel_id] = target_lang
            return True
        return False
    
    async def get_channel_language(self, channel_id):
        """Get the target language for a channel"""
        return self.channel_language_preferences.get(channel_id)
    
    async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle errors"""
        logger.error(f"Update {update} caused error {context.error}")

def main():
    """Main function to run the channel bot"""
    if not TELEGRAM_BOT_TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN not found in environment variables!")
        print("Please set your TELEGRAM_BOT_TOKEN in the .env file")
        return
    
    if not TELEGRAM_CHANNEL_ID:
        logger.warning("TELEGRAM_CHANNEL_ID not set. Channel integration will be limited.")
    
    # Create bot instance
    bot = ChannelTranslationBot()
    
    # Create application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Add message handler for channel posts
    application.add_handler(MessageHandler(filters.ChatType.CHANNEL, bot.handle_channel_message))
    
    # Add error handler
    application.add_error_handler(bot.error_handler)
    
    # Start the bot
    logger.info("Starting the Channel Translation Bot...")
    print("Channel bot is starting... Press Ctrl+C to stop.")
    
    try:
        application.run_polling(allowed_updates=Update.ALL_TYPES)
    except KeyboardInterrupt:
        logger.info("Channel bot stopped by user")
        print("Channel bot stopped.")

if __name__ == '__main__':
    main()
