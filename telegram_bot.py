import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from telegram.constants import ParseMode
from translator import LanguageTranslator
from config import TELEGRAM_BOT_TOKEN, SUPPORTED_LANGUAGES, COMMANDS

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class TelegramTranslationBot:
    def __init__(self):
        self.translator = LanguageTranslator()
        self.user_preferences = {}  # Store user language preferences
        
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command"""
        user = update.effective_user
        welcome_message = f"""
🌍 Welcome to the Language Agnostic Translator Bot, {user.first_name}!

I can help you:
• Translate text between multiple languages
• Detect the language of any text
• Set your preferred target language

Use /help to see all available commands.
        """
        await update.message.reply_text(welcome_message)
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /help command"""
        help_text = "🤖 *Available Commands:*\n\n"
        for command, description in COMMANDS.items():
            help_text += f"• /{command} - {description}\n"
        
        help_text += "\n💡 *How to use:*\n"
        help_text += "• Send me any text and I'll translate it to your preferred language\n"
        help_text += "• Use /set_lang to change your target language\n"
        help_text += "• Use /detect to identify the language of text\n"
        help_text += "• Use /languages to see all supported languages"
        
        await update.message.reply_text(help_text, parse_mode=ParseMode.MARKDOWN)
    
    async def languages_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /languages command"""
        languages_text = "🌐 *Supported Languages:*\n\n"
        for code, name in SUPPORTED_LANGUAGES.items():
            languages_text += f"• {code.upper()} - {name}\n"
        
        languages_text += "\nUse /set_lang <code> to set your preferred language."
        
        await update.message.reply_text(languages_text, parse_mode=ParseMode.MARKDOWN)
    
    async def set_lang_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /set_lang command"""
        if not context.args:
            await update.message.reply_text(
                "Please specify a language code. Use /languages to see available options.\n"
                "Example: /set_lang es"
            )
            return
        
        lang_code = context.args[0].lower()
        user_id = update.effective_user.id
        
        if self.translator.is_language_supported(lang_code):
            self.user_preferences[user_id] = lang_code
            lang_name = SUPPORTED_LANGUAGES[lang_code]
            await update.message.reply_text(
                f"✅ Your preferred language has been set to {lang_name} ({lang_code.upper()})"
            )
        else:
            await update.message.reply_text(
                f"❌ Language code '{lang_code}' is not supported. Use /languages to see available options."
            )
    
    async def detect_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /detect command"""
        if not context.args:
            await update.message.reply_text(
                "Please provide text to detect the language.\n"
                "Example: /detect Hello, how are you?"
            )
            return
        
        text = " ".join(context.args)
        lang_code, lang_name = self.translator.detect_language(text)
        
        if lang_code:
            await update.message.reply_text(
                f"🔍 *Language Detection Result:*\n\n"
                f"Text: `{text}`\n"
                f"Detected Language: {lang_name} ({lang_code.upper()})",
                parse_mode=ParseMode.MARKDOWN
            )
        else:
            await update.message.reply_text(f"❌ {lang_name}")
    
    async def translate_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /translate command"""
        if len(context.args) < 2:
            await update.message.reply_text(
                "Please provide text and target language.\n"
                "Example: /translate Hello, how are you? es"
            )
            return
        
        target_lang = context.args[-1].lower()
        text = " ".join(context.args[:-1])
        
        if not self.translator.is_language_supported(target_lang):
            await update.message.reply_text(
                f"❌ Language code '{target_lang}' is not supported. Use /languages to see available options."
            )
            return
        
        translated_text, message = self.translator.translate_text(text, target_lang)
        
        if translated_text:
            await update.message.reply_text(
                f"🔄 *Translation Result:*\n\n"
                f"Original: `{text}`\n\n"
                f"Translated: `{translated_text}`\n\n"
                f"_{message}_",
                parse_mode=ParseMode.MARKDOWN
            )
        else:
            await update.message.reply_text(f"❌ {message}")
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle regular text messages"""
        user_id = update.effective_user.id
        text = update.message.text
        
        # Get user's preferred language or use default
        target_lang = self.user_preferences.get(user_id, 'en')
        
        # Translate the message
        translated_text, message = self.translator.translate_text(text, target_lang)
        
        if translated_text:
            # Detect source language
            source_lang, source_name = self.translator.detect_language(text)
            
            response = f"🔄 *Translation:*\n\n"
            response += f"Original ({source_name}): `{text}`\n\n"
            response += f"Translated: `{translated_text}`\n\n"
            response += f"_{message}_"
            
            await update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)
        else:
            await update.message.reply_text(f"❌ {message}")
    
    async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle errors"""
        logger.error(f"Update {update} caused error {context.error}")
        if update and update.effective_message:
            await update.effective_message.reply_text(
                "❌ An error occurred while processing your request. Please try again."
            )

def main():
    """Main function to run the bot"""
    if not TELEGRAM_BOT_TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN not found in environment variables!")
        print("Please set your TELEGRAM_BOT_TOKEN in the .env file")
        return
    
    # Create bot instance
    bot = TelegramTranslationBot()
    
    # Create application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Add command handlers
    application.add_handler(CommandHandler("start", bot.start_command))
    application.add_handler(CommandHandler("help", bot.help_command))
    application.add_handler(CommandHandler("languages", bot.languages_command))
    application.add_handler(CommandHandler("set_lang", bot.set_lang_command))
    application.add_handler(CommandHandler("detect", bot.detect_command))
    application.add_handler(CommandHandler("translate", bot.translate_command))
    
    # Add message handler for regular text
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bot.handle_message))
    
    # Add error handler
    application.add_error_handler(bot.error_handler)
    
    # Start the bot
    logger.info("Starting the Language Agnostic Translator Bot...")
    print("Bot is starting... Press Ctrl+C to stop.")
    
    try:
        application.run_polling(allowed_updates=Update.ALL_TYPES)
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
        print("Bot stopped.")

if __name__ == '__main__':
    main()
