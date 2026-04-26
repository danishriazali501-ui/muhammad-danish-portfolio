# 🚀 Deployment Guide - Free Hosting on Render.com

## Step 1: Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `portfolio-django`
3. Make it Public
4. Click **Create repository**

## Step 2: Push Code to GitHub
Open terminal in project folder and run:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/portfolio-django.git
git push -u origin main
```

## Step 3: Deploy on Render.com
1. Go to https://render.com and Sign Up (Free)
2. Click **New +** → **Web Service**
3. Connect your GitHub repository
4. Fill these settings:

| Setting | Value |
|---------|-------|
| Name | `portfolio-django` |
| Environment | `Python 3` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn portfolio.wsgi:application` |
| Plan | Free |

5. Click **Advanced** and add Environment Variable:
   - Key: `SECRET_KEY`
   - Value: `your-new-secret-key-here` (generate at https://djecrety.ir/)

6. Click **Create Web Service**

## Step 4: Wait for Deployment
- Render will automatically build and deploy
- Your site will be live at: `https://portfolio-django.onrender.com`

## Step 5: Custom Domain (Free)
1. Go to https://www.freenom.com (free .tk, .ml, .ga domains)
2. Search and register a free domain
3. In Render dashboard → Settings → Custom Domains
4. Add your domain and follow DNS instructions

## 🎉 Done!
Your portfolio is now live on the internet for FREE!
