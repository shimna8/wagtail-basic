# Getting Started Checklist

## ✅ Pre-Launch Checklist

### System Requirements
- [ ] Python 3.10+ installed
- [ ] pip installed and updated
- [ ] Virtual environment support available
- [ ] 500MB+ free disk space

### Project Setup
- [ ] Virtual environment created ✓
- [ ] Dependencies installed ✓
- [ ] Database migrations applied ✓
- [ ] Project health check passed ✓

## 🚀 Launch Your Project

### Step 1: Start the Development Server

**Linux/macOS:**
```bash
cd mywagtailproject
chmod +x run.sh
./run.sh
```

**Windows:**
```bash
cd mywagtailproject
run.bat
```

**Manual:**
```bash
cd mywagtailproject
source venv/bin/activate  # or venv\Scripts\activate
python manage.py runserver
```

### Step 2: Access the Application

Open your browser and navigate to:
- **Frontend:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/

### Step 3: Create Admin User (if needed)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

## 📝 First-Time Setup Tasks

### Task 1: Explore the Admin Panel
- [ ] Login to admin panel
- [ ] Explore the Pages section
- [ ] Check the Home page
- [ ] Review available apps

### Task 2: Customize Site Settings
- [ ] Go to Settings → Sites
- [ ] Update site name and domain
- [ ] Configure site settings

### Task 3: Create Your First Page
- [ ] Go to Pages
- [ ] Click "Add child page"
- [ ] Create a new page
- [ ] Publish the page

### Task 4: Explore Features
- [ ] Upload an image (Images section)
- [ ] Upload a document (Documents section)
- [ ] Create a form (Forms section)
- [ ] Test search functionality

## 🎨 Customization Tasks

### Task 5: Customize Home Page
Edit `home/models.py`:
```python
class HomePage(Page):
    # Add your custom fields here
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]
```

Then run:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Task 6: Create Custom Page Type
Create a new model in `home/models.py`:
```python
class BlogPage(Page):
    body = RichTextField()
    
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
```

### Task 7: Add Static Files
1. Create `mywagtailproject/static/css/custom.css`
2. Add your CSS
3. Link in templates: `{% static 'css/custom.css' %}`

### Task 8: Create Custom Template
1. Create `mywagtailproject/templates/custom_page.html`
2. Extend base template
3. Add your HTML

## 🔧 Development Tasks

### Task 9: Set Up Version Control
```bash
git init
git add .
git commit -m "Initial Wagtail project setup"
```

### Task 10: Create .env File
Create `.env` in project root:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### Task 11: Install Development Tools
```bash
pip install django-debug-toolbar
pip install black
pip install flake8
```

### Task 12: Configure Email (Optional)
Edit settings to configure email backend:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

## 📚 Learning Resources

### Read These First
- [ ] README.md - Overview
- [ ] SETUP_GUIDE.md - Detailed setup
- [ ] DEVELOPMENT.md - Development guide

### Wagtail Resources
- [ ] [Wagtail Getting Started](https://docs.wagtail.org/en/stable/getting_started/)
- [ ] [Wagtail Tutorial](https://docs.wagtail.org/en/stable/getting_started/tutorial.html)
- [ ] [Wagtail API](https://docs.wagtail.org/en/stable/advanced_topics/api/)

### Django Resources
- [ ] [Django Documentation](https://docs.djangoproject.com/)
- [ ] [Django Models](https://docs.djangoproject.com/en/5.1/topics/db/models/)
- [ ] [Django Views](https://docs.djangoproject.com/en/5.1/topics/http/views/)

## 🧪 Testing

### Task 13: Run Tests
```bash
python manage.py test
```

### Task 14: Create Your First Test
Create `home/tests.py`:
```python
from django.test import TestCase
from home.models import HomePage

class HomePageTests(TestCase):
    def test_home_page_exists(self):
        self.assertTrue(HomePage.objects.exists())
```

## 🚀 Deployment Preparation

### Task 15: Prepare for Production
- [ ] Set `DEBUG = False` in production settings
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up PostgreSQL database
- [ ] Configure static file serving
- [ ] Set up media file storage
- [ ] Configure email backend
- [ ] Enable HTTPS
- [ ] Set up logging

### Task 16: Create Production Settings
Create `mywagtailproject/settings/production.py`:
```python
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
# Add production-specific settings
```

## 📋 Troubleshooting

### Issue: Port 8000 already in use
```bash
python manage.py runserver 8001
```

### Issue: Static files not loading
```bash
python manage.py collectstatic
```

### Issue: Database errors
```bash
python manage.py migrate
```

### Issue: Import errors
- Check `INSTALLED_APPS` in settings
- Verify app is created with `startapp`

## ✨ Next Steps

1. **Explore the Admin Panel** - Get familiar with Wagtail
2. **Create Content** - Add pages and media
3. **Customize Templates** - Make it your own
4. **Add Custom Models** - Extend functionality
5. **Deploy** - Share with the world

## 📞 Need Help?

- Check DEVELOPMENT.md for detailed guides
- Review Wagtail documentation
- Visit Wagtail community forums
- Check Django documentation

## 🎉 You're Ready!

Your Wagtail project is fully set up and ready for development. Start by running the development server and exploring the admin panel.

```bash
./run.sh  # or run.bat on Windows
```

Happy coding! 🚀

---

**Project:** mywagtailproject  
**Wagtail:** 6.3.5  
**Django:** 5.1.13  
**Status:** Ready for Development ✓

