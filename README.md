# Language Agnostic Telegram Bot

A powerful Telegram bot that provides real-time language translation and detection services. The bot can work both in private chats and Telegram channels, making it perfect for multilingual communities.

## Features

🌍 **Multi-language Support**: Supports 20+ languages including English, Spanish, French, German, Chinese, Japanese, Arabic, and more.

🤖 **Smart Translation**: 
- Automatic language detection
- Translate text to any supported language
- Set preferred target language per user
- Channel-wide auto-translation

📱 **Telegram Integration**:
- Private chat support
- Channel integration
- Inline commands
- User-friendly interface

⚡ **Easy to Use**:
- Simple commands
- Real-time translation
- Error handling
- Comprehensive help system

## Installation

### Prerequisites

- Python 3.7 or higher
- A Telegram bot token (get from [@BotFather](https://t.me/botfather))
- pip package manager

### Setup

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd language-agnostic-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create environment file**
   - Copy `env_example.txt` to `.env`
   - Edit `.env` and add your bot token:
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   TELEGRAM_CHANNEL_ID=your_channel_id_here
   ```

4. **Get your bot token**
   - Message [@BotFather](https://t.me/botfather) on Telegram
   - Use `/newbot` command
   - Follow the instructions to create your bot
   - Copy the token to your `.env` file

5. **Get your channel ID (optional)**
   - Add your bot to the channel as an administrator
   - Forward a message from the channel to [@userinfobot](https://t.me/userinfobot)
   - Copy the channel ID to your `.env` file

## Usage

### Running the Bot

#### For Private Chats
```bash
python telegram_bot.py
```

#### For Channel Integration
```bash
python channel_bot.py
```

### Bot Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/start` | Start the bot and see welcome message | `/start` |
| `/help` | Show all available commands | `/help` |
| `/translate <text> <lang>` | Translate text to specific language | `/translate Hello es` |
| `/detect <text>` | Detect the language of text | `/detect Hola mundo` |
| `/languages` | Show all supported languages | `/languages` |
| `/set_lang <code>` | Set your preferred target language | `/set_lang es` |

### Supported Languages

| Code | Language | Code | Language |
|------|----------|------|----------|
| `en` | English | `es` | Spanish |
| `fr` | French | `de` | German |
| `it` | Italian | `pt` | Portuguese |
| `ru` | Russian | `ja` | Japanese |
| `ko` | Korean | `zh` | Chinese |
| `ar` | Arabic | `hi` | Hindi |
| `th` | Thai | `vi` | Vietnamese |
| `tr` | Turkish | `pl` | Polish |
| `nl` | Dutch | `sv` | Swedish |
| `da` | Danish | `no` | Norwegian |

## How to Use

### In Private Chat

1. **Start a conversation** with your bot
2. **Send any text** and it will be automatically translated to your preferred language
3. **Use commands** for specific functions:
   - `/set_lang es` - Set Spanish as your preferred language
   - `/detect Hola` - Detect the language of "Hola"
   - `/translate Hello es` - Translate "Hello" to Spanish

### In Channels

1. **Add the bot** to your channel as an administrator
2. **Use channel commands**:
   - `/translate es Hello world` - Translate to Spanish
   - `/detect Hola mundo` - Detect language
3. **Auto-translation** can be enabled for the entire channel

## Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
# Required: Your bot token from @BotFather
TELEGRAM_BOT_TOKEN=your_bot_token_here

# Optional: Channel ID for channel integration
TELEGRAM_CHANNEL_ID=your_channel_id_here
```

### Customizing Languages

Edit `config.py` to add or modify supported languages:

```python
SUPPORTED_LANGUAGES = {
    'en': 'English',
    'es': 'Spanish',
    # Add more languages here
}
```

## Running in VS Code

1. **Open the project** in VS Code
2. **Install Python extension** if not already installed
3. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Create `.env` file** with your bot token
6. **Run the bot**:
   - Press `F5` or use the Run button
   - Or run in terminal: `python telegram_bot.py`

## Troubleshooting

### Common Issues

1. **"TELEGRAM_BOT_TOKEN not found"**
   - Make sure you have created a `.env` file
   - Check that the token is correct and not empty

2. **"Bot not responding"**
   - Verify the bot token is correct
   - Check if the bot is running (look for "Bot is starting..." message)
   - Make sure you've started a conversation with the bot

3. **"Translation failed"**
   - Check your internet connection
   - The Google Translate service might be temporarily unavailable
   - Try again in a few minutes

4. **"Language not supported"**
   - Use `/languages` to see supported language codes
   - Make sure you're using the correct 2-letter language code

### Getting Help

- Check the logs for error messages
- Verify your bot token and channel ID
- Make sure all dependencies are installed
- Check your internet connection

## Contributing

Feel free to contribute to this project by:
- Adding new languages
- Improving translation accuracy
- Adding new features
- Fixing bugs
- Improving documentation

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues or have questions:
1. Check the troubleshooting section
2. Review the logs for error messages
3. Make sure all setup steps were followed correctly
4. Verify your bot token and permissions

---

**Happy translating! 🌍🤖**
