# Multi-Environment Setup Summary

## 📁 What Was Created

### 1. Requirements Files (`requirements/`)
- **`base.txt`** - Core dependencies for all environments (Django, Wagtail, PostgreSQL adapter, python-decouple)
- **`development.txt`** - Development tools (Debug Toolbar, pytest, black, flake8, etc.)
- **`stage.txt`** - Staging requirements (Gunicorn, Redis, Sentry)
- **`production.txt`** - Production requirements (Gunicorn, Redis, Sentry, CSP, WhiteNoise)

### 2. Settings Files (`voyah/settings/`)
- **`base.py`** - Updated to remove environment-specific configs
- **`development.py`** - Enhanced with Debug Toolbar, logging, SQLite database
- **`stage.py`** - NEW! Production-like environment with configurable security
- **`production.py`** - Enhanced with full security, caching, monitoring

### 3. Environment Variable Templates
- **`.env.development.example`** - Development environment variables (minimal)
- **`.env.stage.example`** - Staging environment variables
- **`.env.production.example`** - Production environment variables

### 4. Setup Scripts (`scripts/`)
- **`setup_development.sh`** - Automated development environment setup
- **`setup_stage.sh`** - Automated staging environment setup
- **`setup_production.sh`** - Automated production environment setup

### 5. Documentation
- **`ENVIRONMENTS.md`** - Comprehensive guide for all environments
- **`.gitignore`** - Proper exclusions for sensitive files

### 6. Updated Files
- **`requirements.txt`** - Now points to `requirements/development.txt` for backward compatibility
- **`voyah/urls.py`** - Added Debug Toolbar support for development

## 🚀 Quick Start Guide

### Development
```bash
# Option 1: Use setup script
./scripts/setup_development.sh

# Option 2: Manual setup
pip install -r requirements/development.txt
python manage.py migrate --settings=voyah.settings.development
python manage.py runserver --settings=voyah.settings.development
```

### Staging
```bash
# Use setup script
./scripts/setup_stage.sh

# Configure .env file
cp .env.stage.example .env
nano .env  # Edit with your credentials

# Run with Gunicorn
gunicorn voyah.wsgi:application \
    --env DJANGO_SETTINGS_MODULE=voyah.settings.stage \
    --bind 0.0.0.0:8000
```

### Production
```bash
# Use setup script
./scripts/setup_production.sh

# Configure .env file
cp .env.production.example .env
nano .env  # Edit with your credentials

# Run deployment checks
python manage.py check --deploy --settings=voyah.settings.production

# Run with Gunicorn
gunicorn voyah.wsgi:application \
    --env DJANGO_SETTINGS_MODULE=voyah.settings.production \
    --bind 0.0.0.0:8000 \
    --workers 4
```

## 🔑 Key Features by Environment

### Development
✅ DEBUG mode enabled
✅ SQLite database (no setup required)
✅ Django Debug Toolbar
✅ Console email backend
✅ No caching (dummy cache)
✅ Verbose logging
✅ Django Extensions (shell_plus, etc.)

### Staging
✅ Production-like configuration
✅ PostgreSQL database
✅ Redis caching
✅ SMTP email
✅ Gunicorn server
✅ Sentry integration
✅ Configurable security settings
✅ File logging

### Production
✅ Maximum security (HSTS, CSP, SSL)
✅ PostgreSQL with connection pooling
✅ Redis caching with compression
✅ WhiteNoise for static files
✅ Gunicorn server
✅ Sentry error tracking
✅ Admin email notifications
✅ Rotating file logs
✅ Performance optimizations

## 📋 Environment Variables

### Development
No environment variables required! Uses sensible defaults.

### Staging/Production
**Required:**
- `SECRET_KEY` - Django secret key
- `ALLOWED_HOSTS` - Comma-separated allowed hosts
- `DB_NAME`, `DB_USER`, `DB_PASSWORD` - Database credentials
- `EMAIL_HOST`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` - Email config
- `WAGTAILADMIN_BASE_URL` - Base URL for Wagtail admin

**Optional:**
- `DEBUG` - Enable/disable debug mode
- `REDIS_URL` - Redis connection URL
- `SENTRY_DSN` - Sentry error tracking
- `SECURE_SSL_REDIRECT` - Force HTTPS

## 🔒 Security Checklist for Production

Before deploying to production, ensure:

- [ ] `SECRET_KEY` is set to a random, unique string
- [ ] `DEBUG=False` in production
- [ ] `ALLOWED_HOSTS` configured with your domain(s)
- [ ] Strong database passwords
- [ ] HTTPS enabled with valid SSL certificate
- [ ] `SECURE_SSL_REDIRECT=True`
- [ ] Sentry configured for error tracking
- [ ] Database backups configured
- [ ] Firewall rules configured
- [ ] `.env` file never committed to version control
- [ ] All security headers tested

## 🛠️ Common Commands

### Switch Environments
```bash
# Method 1: Command line flag
python manage.py <command> --settings=voyah.settings.development
python manage.py <command> --settings=voyah.settings.stage
python manage.py <command> --settings=voyah.settings.production

# Method 2: Environment variable
export DJANGO_SETTINGS_MODULE=voyah.settings.production
python manage.py <command>
```

### Generate Secret Key
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### Run Tests
```bash
pytest --settings=voyah.settings.development
```

### Check Deployment Readiness
```bash
python manage.py check --deploy --settings=voyah.settings.production
```

## 📦 Dependencies Overview

### Base (All Environments)
- Django 5.1
- Wagtail 6.3
- psycopg2-binary (PostgreSQL)
- python-decouple (environment variables)

### Development Only
- django-debug-toolbar
- django-extensions
- pytest, pytest-django, pytest-cov
- black, flake8, isort, pylint

### Staging/Production
- gunicorn (WSGI server)
- whitenoise (static files)
- django-redis (caching)
- sentry-sdk (error tracking)
- django-csp (security headers)

## 🔄 Migration Path

If you're upgrading from the old setup:

1. **Install new requirements:**
   ```bash
   pip install -r requirements/development.txt
   ```

2. **No code changes needed!** Your existing code will work as-is.

3. **For staging/production:** Create `.env` file from templates and configure.

4. **Test each environment:**
   ```bash
   python manage.py check --settings=voyah.settings.development
   python manage.py check --settings=voyah.settings.stage
   python manage.py check --settings=voyah.settings.production
   ```

## 📚 Additional Resources

- Full documentation: `ENVIRONMENTS.md`
- Django deployment: https://docs.djangoproject.com/en/5.1/howto/deployment/
- Wagtail deployment: https://docs.wagtail.org/en/stable/advanced_topics/deploying.html
- Gunicorn docs: https://docs.gunicorn.org/

## 🆘 Troubleshooting

### "No module named 'decouple'"
```bash
pip install python-decouple
```

### "No module named 'debug_toolbar'"
```bash
pip install -r requirements/development.txt
```

### Database connection errors
Check your `.env` file and ensure PostgreSQL is running.

### Static files not loading
```bash
python manage.py collectstatic --settings=voyah.settings.production
```

## ✅ Next Steps

1. **Development:** Start coding! Everything is ready.
2. **Staging:** Set up PostgreSQL and Redis, configure `.env`
3. **Production:** Follow security checklist, configure `.env`, deploy!

For detailed instructions, see `ENVIRONMENTS.md`.

