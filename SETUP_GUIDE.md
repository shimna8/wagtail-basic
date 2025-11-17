# Wagtail Project Setup Guide

## Project Overview
This is a new Wagtail CMS project created with the latest updates (October 2025).

**Project Name:** voyah  
**Location:** `/media/shimna/679d4f93-1438-4a46-8af7-ec5d8b4cdb4b/projects/django/voyah`

## Technology Stack

### Core Dependencies
- **Django:** 5.1.13 (Latest stable version)
- **Wagtail:** 6.3.5 (Latest stable version)
- **Python:** 3.10+

### Key Packages Installed
- **django-modelcluster:** 6.4 - For clustering Django models
- **django-taggit:** 6.1.0 - For tagging functionality
- **django-treebeard:** 4.7.1 - For hierarchical data structures
- **djangorestframework:** 3.16.1 - For REST API support
- **Pillow:** 11.3.0 - For image processing
- **pillow-heif:** 1.1.1 - For HEIF image format support
- **Willow:** 1.11.0 - For image operations
- **beautifulsoup4:** 4.12.3 - For HTML parsing
- **openpyxl:** 3.1.5 - For Excel file handling

## Project Structure

```
voyah/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── db.sqlite3               # SQLite database (development)
├── Dockerfile               # Docker configuration
├── venv/                    # Virtual environment
├── voyah/        # Main project settings
│   ├── settings/            # Django settings modules
│   ├── urls.py              # URL routing
│   ├── wsgi.py              # WSGI application
│   ├── static/              # Static files (CSS, JS)
│   └── templates/           # Project-wide templates
├── home/                    # Home app (example Wagtail app)
│   ├── models.py            # Page models
│   ├── migrations/          # Database migrations
│   ├── static/              # App-specific static files
│   └── templates/           # App-specific templates
└── search/                  # Search functionality app
    ├── views.py             # Search views
    └── templates/           # Search templates
```

## Getting Started

### 1. Activate Virtual Environment
```bash
cd voyah
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Run Development Server
```bash
python manage.py runserver
```
The site will be available at: `http://127.0.0.1:8000/`

### 3. Access Wagtail Admin
```
http://127.0.0.1:8000/admin/
```

### 4. Create Superuser (if needed)
```bash
python manage.py createsuperuser
```

## Database

- **Type:** SQLite (default for development)
- **Location:** `db.sqlite3`
- **Status:** Migrations already applied ✓

### Run Migrations
```bash
python manage.py migrate
```

### Create New Migrations
```bash
python manage.py makemigrations
```

## Key Features

### Wagtail 6.3 Features
- Advanced page management
- Built-in image optimization
- HEIF image format support
- Comprehensive admin interface
- Search functionality
- Document management
- Form builder
- Redirect management
- User management
- Workflow system

### Django 5.1 Features
- Latest security updates
- Performance improvements
- Enhanced ORM capabilities
- Improved async support

## Development Commands

### Collect Static Files
```bash
python manage.py collectstatic
```

### Run Tests
```bash
python manage.py test
```

### Shell Access
```bash
python manage.py shell
```

### Check Project Health
```bash
python manage.py check
```

## Customization

### Adding New Apps
1. Create app: `python manage.py startapp myapp`
2. Add to `INSTALLED_APPS` in settings
3. Create models and migrations
4. Register in Wagtail admin if needed

### Creating Custom Page Types
Edit `home/models.py` to create custom page models inheriting from `Page`.

### Static Files
- Project-wide: `voyah/static/`
- App-specific: `home/static/`

### Templates
- Project-wide: `voyah/templates/`
- App-specific: `home/templates/`

## Deployment

### Production Checklist
- [ ] Set `DEBUG = False` in settings
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up proper database (PostgreSQL recommended)
- [ ] Configure static file serving
- [ ] Set up media file storage
- [ ] Configure email backend
- [ ] Enable HTTPS
- [ ] Set up proper logging
- [ ] Configure caching

### Environment Variables
Create a `.env` file for sensitive settings:
```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=postgresql://user:password@localhost/dbname
```

## Useful Resources

- **Wagtail Documentation:** https://docs.wagtail.org/
- **Django Documentation:** https://docs.djangoproject.com/
- **Wagtail Community:** https://wagtail.org/community/
- **GitHub:** https://github.com/wagtail/wagtail

## Next Steps

1. **Customize the Home Page:** Edit `home/models.py`
2. **Add Custom Page Types:** Create new page models
3. **Configure Static Files:** Set up CSS/JS
4. **Create Content:** Use Wagtail admin to create pages
5. **Set Up Search:** Configure search backend
6. **Deploy:** Choose hosting platform

## Support

For issues or questions:
- Check Wagtail documentation
- Visit Wagtail community forums
- Review Django documentation
- Check project logs for errors

---

**Project Created:** October 2025  
**Wagtail Version:** 6.3.5  
**Django Version:** 5.1.13

