# GitHub Setup & Deployment Guide

## Step 1: Create GitHub Repository

1. **Go to [GitHub.com](https://github.com) and sign in**
2. **Click the "+" icon in the top right corner**
3. **Select "New repository"**
4. **Fill in the details:**
   - **Repository name:** `file-parser-api` (or your preferred name)
   - **Description:** `Django REST API for file parsing with progress tracking`
   - **Make it Public** (so you can get a website link)
   - **Don't initialize with README** (we already have one)
   - **Don't add .gitignore** (we already have one)
5. **Click "Create repository"**

## Step 2: Connect Your Local Repository

After creating the GitHub repository, you'll see commands. Use these:

```bash
# Add the remote origin (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/file-parser-api.git

# Rename your branch to main (GitHub's default)
git branch -M main

# Push your code to GitHub
git push -u origin main
```

## Step 3: Get Your Website Link

### Option A: GitHub Pages (Static Files Only)
Since this is a Django backend API, GitHub Pages won't work directly. You need a backend hosting service.

### Option B: Railway (Recommended - Free)
1. **Go to [Railway.app](https://railway.app/)**
2. **Sign up with your GitHub account**
3. **Click "New Project"**
4. **Select "Deploy from GitHub repo"**
5. **Choose your `file-parser-api` repository**
6. **Railway will automatically detect it's a Django app**
7. **Add environment variables:**
   - `SECRET_KEY` - Generate a new Django secret key
   - `DEBUG` - Set to `False`
   - `ALLOWED_HOSTS` - Set to your Railway domain
8. **Deploy!**
9. **Your website will be available at:** `https://your-app-name.railway.app`

### Option C: Render (Free Tier Available)
1. **Go to [Render.com](https://render.com/)**
2. **Sign up with your GitHub account**
3. **Create a new Web Service**
4. **Connect your GitHub repository**
5. **Configure:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn config.wsgi:application`
6. **Deploy!**
7. **Your website will be available at:** `https://your-app-name.onrender.com`

## Step 4: Test Your API

Once deployed, test your API endpoints:

```bash
# Test the API root
curl https://your-app-name.railway.app/

# List files
curl https://your-app-name.railway.app/files/

# Upload a file
curl -X POST -F "name=Test File" -F "file=@sample_data/sample.csv" https://your-app-name.railway.app/files/
```

## Step 5: Share Your Website

Your API will be available at:
- **Railway:** `https://your-app-name.railway.app`
- **Render:** `https://your-app-name.onrender.com`

## Troubleshooting

### If you get a "No module named 'django'" error:
- Make sure `requirements.txt` is in your repository
- Check that the hosting platform is installing dependencies

### If you get a database error:
- Most hosting platforms provide PostgreSQL
- Update your `DATABASE_URL` environment variable

### If you get a "DisallowedHost" error:
- Make sure `ALLOWED_HOSTS` includes your domain
- Set it to `*` for testing (not recommended for production)

## Next Steps

1. **Customize your API** - Add more file formats, authentication, etc.
2. **Add a frontend** - Create a React/Vue.js app to consume your API
3. **Set up a custom domain** - Point your own domain to your hosted API
4. **Add monitoring** - Set up logging and error tracking

## Support

If you need help:
- Check the hosting platform's documentation
- Look at Django deployment guides
- Ask in the hosting platform's community forums 