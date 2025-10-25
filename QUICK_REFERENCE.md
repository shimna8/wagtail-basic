# Quick Reference Card

## 🚀 Getting Started

### Development (Fastest)
```bash
./scripts/setup_development.sh
python manage.py runserver --settings=mywagtailproject.settings.development
```

### Staging
```bash
./scripts/setup_stage.sh
# Edit .env with your credentials
gunicorn mywagtailproject.wsgi:application --env DJANGO_SETTINGS_MODULE=mywagtailproject.settings.stage
```

### Production
```bash
./scripts/setup_production.sh
# Edit .env with your credentials
gunicorn mywagtailproject.wsgi:application --env DJANGO_SETTINGS_MODULE=mywagtailproject.settings.production --workers 4
```

## 📦 Install Requirements

```bash
# Development
pip install -r requirements/development.txt

# Staging
pip install -r requirements/stage.txt

# Production
pip install -r requirements/production.txt
```

## ⚙️ Common Commands

### Run Server
```bash
# Development
python manage.py runserver --settings=mywagtailproject.settings.development

# Staging/Production (with Gunicorn)
gunicorn mywagtailproject.wsgi:application --env DJANGO_SETTINGS_MODULE=mywagtailproject.settings.stage
```

### Migrations
```bash
python manage.py makemigrations --settings=mywagtailproject.settings.development
python manage.py migrate --settings=mywagtailproject.settings.development
```

### Create Superuser
```bash
python manage.py createsuperuser --settings=mywagtailproject.settings.development
```

### Collect Static Files
```bash
python manage.py collectstatic --noinput --settings=mywagtailproject.settings.production
```

### Run Tests
```bash
pytest --settings=mywagtailproject.settings.development
```

### Django Shell
```bash
# Regular shell
python manage.py shell --settings=mywagtailproject.settings.development

# Enhanced shell (with django-extensions)
python manage.py shell_plus --settings=mywagtailproject.settings.development
```

### Check Deployment
```bash
python manage.py check --deploy --settings=mywagtailproject.settings.production
```

## 🔑 Generate Secret Key

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

## 📁 File Structure

```
mywagtailproject/
├── requirements/
│   ├── base.txt              # Core dependencies
│   ├── development.txt       # + Development tools
│   ├── stage.txt             # + Staging tools
│   └── production.txt        # + Production tools
├── mywagtailproject/
│   └── settings/
│       ├── base.py           # Base settings
│       ├── development.py    # Development settings
│       ├── stage.py          # Staging settings
│       └── production.py     # Production settings
├── scripts/
│   ├── setup_development.sh
│   ├── setup_stage.sh
│   └── setup_production.sh
├── .env.development.example
├── .env.stage.example
└── .env.production.example
```

## 🌍 Environment Variables

### Development
No .env file needed! Uses defaults.

### Staging/Production
Create `.env` file with:
```bash
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=example.com,www.example.com
DB_NAME=mywagtailproject
DB_USER=postgres
DB_PASSWORD=your-password
EMAIL_HOST=smtp.example.com
EMAIL_HOST_USER=noreply@example.com
EMAIL_HOST_PASSWORD=your-email-password
WAGTAILADMIN_BASE_URL=https://example.com
REDIS_URL=redis://127.0.0.1:6379/0
```

## 🔄 Switch Environments

### Method 1: Command Flag
```bash
python manage.py <command> --settings=mywagtailproject.settings.development
python manage.py <command> --settings=mywagtailproject.settings.stage
python manage.py <command> --settings=mywagtailproject.settings.production
```

### Method 2: Environment Variable
```bash
export DJANGO_SETTINGS_MODULE=mywagtailproject.settings.production
python manage.py <command>
```

## 🔍 Debugging

### View Current Settings
```bash
python manage.py diffsettings --settings=mywagtailproject.settings.development
```

### Check Configuration
```bash
python manage.py check --settings=mywagtailproject.settings.development
```

### View Logs
```bash
# Development (console output)
# Just check terminal

# Staging/Production
tail -f logs/stage.log
tail -f logs/production.log
```

## 🗄️ Database Setup

### PostgreSQL (Staging/Production)
```bash
sudo -u postgres psql
CREATE DATABASE mywagtailproject_stage;
CREATE USER mywagtailproject WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE mywagtailproject_stage TO mywagtailproject;
\q
```

## 🚨 Troubleshooting

### Module Not Found
```bash
pip install -r requirements/development.txt
```

### Database Connection Error
Check `.env` file and ensure PostgreSQL is running:
```bash
sudo systemctl status postgresql
```

### Redis Connection Error
Ensure Redis is running:
```bash
sudo systemctl status redis-server
```

### Static Files Not Loading
```bash
python manage.py collectstatic --settings=mywagtailproject.settings.production
```

## 📚 Documentation

- **Full Guide:** `ENVIRONMENTS.md`
- **Setup Summary:** `ENVIRONMENT_SETUP_SUMMARY.md`
- **This Card:** `QUICK_REFERENCE.md`

## 🔗 URLs

- **Frontend:** http://127.0.0.1:8000/
- **Admin:** http://127.0.0.1:8000/admin/
- **Django Admin:** http://127.0.0.1:8000/django-admin/
- **Debug Toolbar:** http://127.0.0.1:8000/__debug__/ (dev only)

## ✅ Pre-Deployment Checklist

- [ ] `SECRET_KEY` is random and secure
- [ ] `DEBUG=False`
- [ ] `ALLOWED_HOSTS` configured
- [ ] Database credentials secure
- [ ] HTTPS enabled
- [ ] Static files collected
- [ ] Migrations applied
- [ ] Superuser created
- [ ] Sentry configured
- [ ] Backups configured

## 🆘 Need Help?

1. Check `ENVIRONMENTS.md` for detailed documentation
2. Run `python manage.py check --deploy` for deployment issues
3. Check logs in `logs/` directory
4. Review Django/Wagtail documentation

