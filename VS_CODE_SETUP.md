# VS Code Setup Guide

## 🚀 Quick Setup for VS Code

### Step 1: Open Project in VS Code
1. Open VS Code
2. File → Open Folder
3. Select the "language agnostic chatbot" folder

### Step 2: Install Python Extension (if not already installed)
1. Go to Extensions (Ctrl+Shift+X)
2. Search for "Python"
3. Install the official Python extension by Microsoft

### Step 3: Set Python Interpreter
1. Press Ctrl+Shift+P
2. Type "Python: Select Interpreter"
3. Choose your Python 3.10 interpreter

### Step 4: Create Environment File
1. Copy `env_example.txt` to `.env`
2. Edit `.env` and add your bot token:
   ```
   TELEGRAM_BOT_TOKEN=your_actual_bot_token_here
   ```

### Step 5: Run the Bot
You have 3 options:

#### Option A: Use the Run Button
1. Press F5 or go to Run → Start Debugging
2. Select "Run Bot Selector" from the dropdown
3. Choose your preferred bot mode

#### Option B: Use the Terminal
1. Open Terminal (Ctrl+`)
2. Run: `python run_bot.py`
3. Select your preferred mode

#### Option C: Run Individual Files
1. Press F5
2. Select "Run Private Chat Bot" or "Run Channel Bot"

## 🔧 VS Code Features Available

### Debugging
- Set breakpoints by clicking on line numbers
- Use F5 to start debugging
- Use F10/F11 to step through code

### IntelliSense
- Auto-completion for Python code
- Hover over functions to see documentation
- Error highlighting and suggestions

### Integrated Terminal
- Run commands directly in VS Code
- Multiple terminal tabs available
- Easy access to Python environment

## 🧪 Testing

### Run Tests
1. Open Terminal (Ctrl+`)
2. Run: `python test_bot.py`
3. Check if all tests pass

### Test Individual Components
```python
# Test translator
python -c "from translator import LanguageTranslator; t = LanguageTranslator(); print(t.translate_text('Hello', 'es'))"

# Test configuration
python -c "from config import SUPPORTED_LANGUAGES; print(SUPPORTED_LANGUAGES)"
```

## 🐛 Troubleshooting

### Common Issues

1. **"Module not found" error**
   - Make sure you're in the correct directory
   - Check if all dependencies are installed: `pip install -r requirements.txt`

2. **"TELEGRAM_BOT_TOKEN not found"**
   - Create `.env` file with your bot token
   - Make sure the file is in the project root

3. **Python interpreter not found**
   - Press Ctrl+Shift+P
   - Type "Python: Select Interpreter"
   - Choose the correct Python version

4. **Bot not responding**
   - Check your internet connection
   - Verify the bot token is correct
   - Make sure the bot is running (look for "Bot is starting..." message)

## 📁 Project Structure in VS Code

```
language agnostic chatbot/
├── .vscode/
│   └── launch.json          # VS Code launch configurations
├── telegram_bot.py          # Main private chat bot
├── channel_bot.py           # Channel integration bot
├── translator.py            # Translation logic
├── config.py                # Configuration settings
├── run_bot.py              # Bot launcher
├── test_bot.py             # Test suite
├── requirements.txt        # Python dependencies
├── README.md              # Full documentation
├── QUICK_START.md         # Quick setup guide
└── VS_CODE_SETUP.md       # This file
```

## 🎯 Recommended VS Code Extensions

- **Python** (Microsoft) - Essential for Python development
- **Python Docstring Generator** - Auto-generate docstrings
- **Python Indent** - Better indentation handling
- **autoDocstring** - Generate docstrings automatically
- **GitLens** - Enhanced Git capabilities

## 🚀 Ready to Go!

Once you've completed the setup:
1. Get your bot token from @BotFather
2. Add it to the `.env` file
3. Press F5 and select "Run Bot Selector"
4. Start chatting with your bot!

**Happy coding! 🤖🌍**
