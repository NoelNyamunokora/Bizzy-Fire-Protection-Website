# Bizzy Fire Protection Services Website

Professional fire protection services website built with Flask.

## Features
- Modern responsive design
- Service showcase
- Product catalog
- Contact form
- Client testimonials

## Setup
```bash
pip install -r requirements.txt
python app.py
```

## Deployment
Deploy to Render.com:
1. Connect this GitHub repository
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `gunicorn app:app`
4. Upload images manually to `/static/images/` and `/static/projects/` folders

## Note
Images are not included in this repository due to size constraints. Upload them directly to your hosting server.
