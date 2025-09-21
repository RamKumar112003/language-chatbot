# Deployment Guide - Language Agnostic Translator

## 🌐 Web Application Deployment

This guide covers deploying your Language Agnostic Translator web application to various platforms.

## 🚀 Quick Start

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run web application
python run_web.py

# Open http://localhost:5000 in your browser
```

### VS Code
1. Press **F5**
2. Select **"Run Web Application"** for development
3. Select **"Run Web App (Production)"** for production mode

## 📱 Platform Deployment Options

### 1. Heroku (Recommended for Beginners)

#### Prerequisites
- Heroku account (free tier available)
- Heroku CLI installed
- Git repository

#### Steps
1. **Install Heroku CLI**
   ```bash
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku App**
   ```bash
   heroku create your-app-name
   ```

4. **Set Environment Variables**
   ```bash
   heroku config:set TELEGRAM_BOT_TOKEN=your_bot_token_here
   heroku config:set TELEGRAM_CHANNEL_ID=your_channel_id_here
   ```

5. **Deploy**
   ```bash
   git add .
   git commit -m "Initial deployment"
   git push heroku main
   ```

6. **Open Your App**
   ```bash
   heroku open
   ```

### 2. Railway

#### Steps
1. **Connect GitHub Repository**
   - Go to [Railway.app](https://railway.app)
   - Connect your GitHub account
   - Select your repository

2. **Configure Environment Variables**
   - Add `TELEGRAM_BOT_TOKEN`
   - Add `TELEGRAM_CHANNEL_ID` (optional)

3. **Deploy**
   - Railway will automatically deploy
   - Get your live URL

### 3. Render

#### Steps
1. **Create New Web Service**
   - Go to [Render.com](https://render.com)
   - Connect your GitHub repository

2. **Configure Build Settings**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn web_app:app`

3. **Set Environment Variables**
   - Add your bot token and channel ID

4. **Deploy**
   - Click "Create Web Service"

### 4. PythonAnywhere

#### Steps
1. **Create Account**
   - Sign up at [PythonAnywhere.com](https://pythonanywhere.com)

2. **Upload Files**
   - Upload all project files to your account

3. **Create Web App**
   - Go to Web tab
   - Create new web app
   - Choose Flask
   - Set source code path

4. **Configure WSGI**
   - Edit the WSGI file to point to your app

5. **Set Environment Variables**
   - Add to your web app configuration

### 5. DigitalOcean App Platform

#### Steps
1. **Create App**
   - Go to DigitalOcean App Platform
   - Create new app from GitHub

2. **Configure App Spec**
   ```yaml
   name: language-translator
   services:
   - name: web
     source_dir: /
     github:
       repo: your-username/your-repo
       branch: main
     run_command: gunicorn web_app:app
     environment_slug: python
     instance_count: 1
     instance_size_slug: basic-xxs
     envs:
     - key: TELEGRAM_BOT_TOKEN
       value: your_bot_token_here
   ```

3. **Deploy**
   - Click "Create Resources"

## 🔧 Environment Variables

### Required
- `TELEGRAM_BOT_TOKEN` - Your bot token from @BotFather

### Optional
- `TELEGRAM_CHANNEL_ID` - Channel ID for channel integration
- `PORT` - Port number (default: 5000)
- `FLASK_DEBUG` - Debug mode (true/false)

## 📊 Monitoring and Maintenance

### Health Check
Your app includes a health check endpoint:
```
GET /api/languages
```

### Logs
Monitor your application logs:
```bash
# Heroku
heroku logs --tail

# Railway
railway logs

# Render
Check the logs tab in your dashboard
```

### Performance
- The app uses Gunicorn for production
- Configure worker processes based on your needs
- Monitor memory usage and response times

## 🛠️ Customization

### Adding New Languages
1. Edit `config.py`
2. Add new language to `SUPPORTED_LANGUAGES`
3. Redeploy your application

### Styling Changes
1. Modify templates in `templates/` directory
2. Update CSS in `templates/base.html`
3. Test locally before deploying

### API Endpoints
- `GET /` - Main translation interface
- `POST /api/translate` - Translation API
- `POST /api/detect` - Language detection API
- `GET /api/languages` - Supported languages
- `GET /telegram` - Telegram bot information
- `GET /about` - About page

## 🔒 Security Considerations

### Environment Variables
- Never commit `.env` files to version control
- Use platform-specific secret management
- Rotate tokens regularly

### CORS
- CORS is enabled for API endpoints
- Configure allowed origins for production

### Rate Limiting
- Consider adding rate limiting for production
- Monitor API usage

## 📈 Scaling

### Horizontal Scaling
- Use load balancers
- Deploy multiple instances
- Use Redis for session storage

### Vertical Scaling
- Increase instance size
- Add more memory/CPU
- Optimize database queries

## 🐛 Troubleshooting

### Common Issues

1. **App Won't Start**
   - Check environment variables
   - Verify all dependencies are installed
   - Check logs for errors

2. **Translation Not Working**
   - Verify internet connection
   - Check if translation service is available
   - Monitor API rate limits

3. **Static Files Not Loading**
   - Check file paths
   - Verify static folder structure
   - Clear browser cache

### Debug Mode
Enable debug mode for development:
```bash
export FLASK_DEBUG=true
python run_web.py
```

## 📞 Support

If you encounter issues:
1. Check the logs
2. Verify environment variables
3. Test locally first
4. Check platform-specific documentation

## 🎉 Success!

Once deployed, your web application will be available at your platform's URL. Users can:
- Translate text between 20+ languages
- Detect language of any text
- Use the responsive web interface
- Access from any device

**Happy translating! 🌍🤖**
