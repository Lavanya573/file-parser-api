# Deployment Guide

This Django project can be deployed to various hosting platforms. Here are the recommended options:

## Option 1: Railway (Recommended for Quick Deployment)

1. **Fork/Clone this repository to your GitHub account**
2. **Go to [Railway.app](https://railway.app/)**
3. **Connect your GitHub account**
4. **Select this repository**
5. **Railway will automatically detect it's a Django app**
6. **Add environment variables:**
   - `SECRET_KEY` - Generate a new Django secret key
   - `DEBUG` - Set to `False` for production
   - `ALLOWED_HOSTS` - Set to your Railway domain
7. **Deploy!**

## Option 2: Render

1. **Fork/Clone this repository to your GitHub account**
2. **Go to [Render.com](https://render.com/)**
3. **Create a new Web Service**
4. **Connect your GitHub repository**
5. **Configure:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn config.wsgi:application`
6. **Add environment variables as needed**
7. **Deploy!**

## Option 3: Heroku

1. **Fork/Clone this repository to your GitHub account**
2. **Install Heroku CLI**
3. **Create a new Heroku app:**
   ```bash
   heroku create your-app-name
   ```
4. **Add PostgreSQL addon:**
   ```bash
   heroku addons:create heroku-postgresql:mini
   ```
5. **Configure environment variables:**
   ```bash
   heroku config:set SECRET_KEY="your-secret-key"
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS="your-app-name.herokuapp.com"
   ```
6. **Deploy:**
   ```bash
   git push heroku main
   ```

## Option 4: PythonAnywhere

1. **Fork/Clone this repository to your GitHub account**
2. **Sign up for [PythonAnywhere](https://www.pythonanywhere.com/)**
3. **Create a new web app**
4. **Clone your repository**
5. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```
6. **Configure WSGI file**
7. **Set up static files**
8. **Deploy!**

## Environment Variables

For production, make sure to set these environment variables:

```bash
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
DATABASE_URL=your-database-url
```

## Database Setup

For production, consider using:
- **PostgreSQL** (recommended)
- **MySQL**
- **SQLite** (only for small projects)

## Static Files

Configure your hosting platform to serve static files from the `static/` directory.

## Media Files

For production, consider using cloud storage:
- **AWS S3**
- **Azure Blob Storage**
- **Google Cloud Storage**

## SSL/HTTPS

Most modern hosting platforms provide free SSL certificates. Make sure to enable HTTPS for production.

## Monitoring

Consider adding:
- **Error tracking** (Sentry)
- **Performance monitoring** (New Relic, DataDog)
- **Logging** (Loggly, Papertrail) 