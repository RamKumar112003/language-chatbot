# Quick Start Guide

## 🚀 Get Your Bot Running in 5 Minutes

### Step 1: Get Bot Token
1. Open Telegram and search for [@BotFather](https://t.me/botfather)
2. Send `/newbot` command
3. Follow instructions to create your bot
4. Copy the bot token (looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

### Step 2: Setup Project
1. **Run setup script:**
   ```bash
   python setup.py
   ```

2. **Edit .env file:**
   - Open `.env` file
   - Replace `your_bot_token_here` with your actual bot token
   - Save the file

### Step 3: Run the Bot
```bash
python run_bot.py
```

### Step 4: Test Your Bot
1. Open Telegram
2. Search for your bot (the username you created)
3. Send `/start` to begin
4. Send any text message to test translation

## 🎯 Quick Commands

| Command | What it does |
|---------|-------------|
| `/start` | Start the bot |
| `/help` | See all commands |
| `/set_lang es` | Set Spanish as preferred language |
| `/translate Hello es` | Translate "Hello" to Spanish |
| `/detect Hola` | Detect language of "Hola" |
| `/languages` | See all supported languages |

## 🔧 VS Code Users

1. Open project in VS Code
2. Press `F5` or go to Run > Start Debugging
3. Choose "Run Bot Selector" from the dropdown
4. Select your preferred bot mode

## 📱 Channel Integration

1. Create a Telegram channel
2. Add your bot as administrator
3. Run: `python channel_bot.py`
4. Use `/translate es Hello` in the channel

## 🆘 Need Help?

- Check `README.md` for detailed instructions
- Make sure your bot token is correct
- Verify Python 3.7+ is installed
- Check your internet connection

**Happy translating! 🌍🤖**
