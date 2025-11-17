# voyah - Latest Wagtail CMS Setup

A modern Wagtail CMS project with the latest updates and best practices.

## 🚀 Quick Start

### Linux/macOS
```bash
chmod +x run.sh
./run.sh
```

### Windows
```bash
run.bat
```

### Manual Setup
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic

# Start development server
python manage.py runserver
```

## 📋 System Requirements

- **Python:** 3.10 or higher
- **pip:** Latest version
- **Virtual Environment:** Recommended

## 📦 Installed Packages

### Core Framework
- **Django 5.1.13** - Web framework
- **Wagtail 6.3.5** - CMS platform

### Database & ORM
- **django-modelcluster 6.4** - Model clustering
- **django-treebeard 4.7.1** - Hierarchical data

### Content Management
- **django-taggit 6.1.0** - Tagging system
- **draftjs_exporter 5.1.0** - Rich text export

### Media & Images
- **Pillow 11.3.0** - Image processing
- **pillow-heif 1.1.1** - HEIF format support
- **Willow 1.11.0** - Image operations

### API & REST
- **djangorestframework 3.16.1** - REST API framework
- **django-filter 25.1** - Filtering support

### Utilities
- **beautifulsoup4 4.12.3** - HTML parsing
- **openpyxl 3.1.5** - Excel handling
- **requests 2.32.5** - HTTP library

## 🌐 Access Points

| Service | URL | Purpose |
|---------|-----|---------|
| Frontend | http://127.0.0.1:8000/ | Main website |
| Admin | http://127.0.0.1:8000/admin/ | Wagtail admin panel |
| Search | http://127.0.0.1:8000/search/ | Search functionality |

## 📁 Project Structure

```
voyah/
├── manage.py                 # Django CLI
├── requirements.txt          # Dependencies
├── db.sqlite3               # Development database
├── SETUP_GUIDE.md           # Detailed setup guide
├── run.sh / run.bat         # Quick start scripts
├── voyah/        # Project settings
│   ├── settings/            # Django settings
│   ├── urls.py              # URL routing
│   ├── wsgi.py              # WSGI config
│   ├── static/              # Static files
│   └── templates/           # Templates
├── home/                    # Home app
│   ├── models.py            # Page models
│   ├── migrations/          # DB migrations
│   └── templates/           # App templates
└── search/                  # Search app
    ├── views.py             # Search views
    └── templates/           # Search templates
```

## 🛠️ Common Commands

### Development
```bash
# Run development server
python manage.py runserver

# Create superuser
python manage.py createsuperuser

# Run migrations
python manage.py migrate

# Create new app
python manage.py startapp myapp

# Run tests
python manage.py test

# Django shell
python manage.py shell
```

### Database
```bash
# Make migrations
python manage.py makemigrations

# Show migration status
python manage.py showmigrations

# Migrate specific app
python manage.py migrate home
```

### Static Files
```bash
# Collect static files
python manage.py collectstatic

# Find static files
python manage.py findstatic
```

## 🎨 Customization

### Create Custom Page Type
Edit `home/models.py`:
```python
from wagtail.models import Page
from wagtail.fields import RichTextField

class BlogPage(Page):
    body = RichTextField()
    
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
```

### Add Custom App
```bash
python manage.py startapp myapp
# Add 'myapp' to INSTALLED_APPS in settings
```

## 🚀 Deployment

### Production Checklist
- [ ] Set `DEBUG = False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use PostgreSQL database
- [ ] Set up static file serving
- [ ] Configure media storage
- [ ] Enable HTTPS
- [ ] Set up proper logging
- [ ] Configure email backend

### Environment Variables
Create `.env` file:
```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=postgresql://user:pass@localhost/db
```

## 📚 Resources

- [Wagtail Documentation](https://docs.wagtail.org/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Wagtail Community](https://wagtail.org/community/)
- [GitHub Repository](https://github.com/wagtail/wagtail)

## 📝 License

This project uses Wagtail CMS which is licensed under the BSD 3-Clause License.

## 🤝 Support

For issues or questions:
1. Check the SETUP_GUIDE.md
2. Review Wagtail documentation
3. Visit Wagtail community forums
4. Check project logs

---

**Created:** October 2025  
**Wagtail Version:** 6.3.5  
**Django Version:** 5.1.13  
**Python:** 3.10+

