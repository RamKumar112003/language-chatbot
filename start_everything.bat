@echo off
title Language Agnostic Translator - Complete Setup
echo.
echo ========================================
echo   Language Agnostic Translator
echo   Complete Setup and Launcher
echo ========================================
echo.
echo This will set up everything and let you choose what to run.
echo.
pause
echo.
echo Running complete setup...
python setup_complete.py
echo.
echo Setup complete! Now you can:
echo 1. Run Telegram Bot
echo 2. Run Web Application
echo 3. Exit
echo.
set /p choice="Enter your choice (1-3): "
if "%choice%"=="1" (
    echo.
    echo Starting Telegram Bot...
    python run_telegram_bot.py
) else if "%choice%"=="2" (
    echo.
    echo Starting Web Application...
    python run_web.py
) else if "%choice%"=="3" (
    echo.
    echo Goodbye!
    exit
) else (
    echo.
    echo Invalid choice. Please run again.
)
echo.
echo Press any key to exit...
pause >nul
