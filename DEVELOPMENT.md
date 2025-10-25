# Development Guide

## Environment Setup

### Initial Setup
```bash
# Clone/navigate to project
cd mywagtailproject

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
```

## Project Configuration

### Settings Structure
- `mywagtailproject/settings/base.py` - Base settings
- `mywagtailproject/settings/development.py` - Development settings
- `mywagtailproject/settings/stage.py` - Staging settings
- `mywagtailproject/settings/production.py` - Production settings

### Key Settings to Customize
```python
# In settings/base.py
SITE_NAME = "My Wagtail Site"
WAGTAIL_SITE_NAME = "My Wagtail Site"

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

## Creating Custom Page Types

### Example: Blog Page
```python
# home/models.py
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.blocks import RichTextBlock, ImageBlock
from wagtail.admin.panels import FieldPanel

class BlogPage(Page):
    intro = RichTextField()
    body = StreamField([
        ('rich_text', RichTextBlock()),
        ('image', ImageBlock()),
    ])
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]
    
    class Meta:
        verbose_name = "Blog Page"
```

## Working with Models

### Creating Models
```python
from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class CustomPage(Page):
    description = models.CharField(max_length=255)
    content = RichTextField()
    
    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('content'),
    ]
```

### Migrations
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migration status
python manage.py showmigrations

# Rollback migration
python manage.py migrate app_name 0001
```

## Static Files & Assets

### Organization
```
mywagtailproject/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
└── home/
    └── static/
        └── home/
            ├── css/
            └── js/
```

### Collecting Static Files
```bash
# Development (automatic)
python manage.py runserver

# Production
python manage.py collectstatic --noinput
```

## Templates

### Template Hierarchy
```
templates/
├── base.html              # Base template
├── home/
│   ├── home_page.html     # Home page
│   └── blog_page.html     # Blog page
└── search/
    └── search.html        # Search results
```

### Template Tags
```django
{% load wagtailcore_tags %}

{# Get page URL #}
{% pageurl page %}

{# Get image rendition #}
{% image page.image width-400 %}

{# Rich text #}
{{ page.body|richtext }}
```

## Testing

### Running Tests
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test home

# Run specific test class
python manage.py test home.tests.HomePageTests

# Run with verbosity
python manage.py test --verbosity=2
```

### Writing Tests
```python
# home/tests.py
from django.test import TestCase
from home.models import HomePage

class HomePageTests(TestCase):
    def setUp(self):
        self.home = HomePage.objects.create(title="Home")
    
    def test_home_page_exists(self):
        self.assertTrue(HomePage.objects.exists())
```

## Debugging

### Django Debug Toolbar
```bash
pip install django-debug-toolbar
```

Add to `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    # ...
    'debug_toolbar',
]
```

Add to `MIDDLEWARE`:
```python
MIDDLEWARE = [
    # ...
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
```

### Logging
```python
import logging
logger = logging.getLogger(__name__)

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
```

## Performance Tips

1. **Use select_related() and prefetch_related()**
   ```python
   pages = Page.objects.select_related('owner').prefetch_related('tags')
   ```

2. **Cache queries**
   ```python
   from django.views.decorators.cache import cache_page
   
   @cache_page(60 * 15)  # 15 minutes
   def my_view(request):
       pass
   ```

3. **Use database indexes**
   ```python
   class MyModel(models.Model):
       name = models.CharField(max_length=100, db_index=True)
   ```

4. **Optimize images**
   - Use appropriate formats (WebP, JPEG)
   - Compress before upload
   - Use responsive images

## Common Issues & Solutions

### Issue: Static files not loading
**Solution:** Run `python manage.py collectstatic`

### Issue: Database locked
**Solution:** Delete `db.sqlite3` and run migrations again

### Issue: Import errors
**Solution:** Ensure app is in `INSTALLED_APPS`

### Issue: Template not found
**Solution:** Check template path and `TEMPLATES` setting

## Useful Commands

```bash
# Shell access
python manage.py shell

# Check project health
python manage.py check

# Show installed apps
python manage.py show_urls

# Database shell
python manage.py dbshell

# Create fixture
python manage.py dumpdata > fixture.json

# Load fixture
python manage.py loaddata fixture.json
```

## Version Control

### .gitignore
```
venv/
*.pyc
__pycache__/
*.sqlite3
.env
.DS_Store
media/
staticfiles/
```

### Commit Messages
```
feat: Add new feature
fix: Fix bug
docs: Update documentation
style: Format code
refactor: Refactor code
test: Add tests
```

---

Happy coding! 🚀

