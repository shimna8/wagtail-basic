# Environment Configuration Guide

This project supports multiple environments with separate settings and requirements files.

## Directory Structure

```
voyah/
├── requirements/
│   ├── base.txt               # Base requirements for all environments
│   ├── development.txt        # Development-specific requirements
│   ├── stage.txt              # Staging-specific requirements
│   └── production.txt         # Production-specific requirements
├── voyah/
│   └── settings/
│       ├── base.py            # Base settings for all environments
│       ├── development.py     # Development settings
│       ├── stage.py           # Staging settings
│       └── production.py      # Production settings
├── .env.development.example   # Example environment variables for development
├── .env.stage.example         # Example environment variables for staging
└── .env.production.example    # Example environment variables for production
```

## Environments

### 1. Development

**Purpose:** Local development with debugging tools and relaxed security.

**Features:**
- DEBUG mode enabled
- SQLite database
- Console email backend
- Django Debug Toolbar
- Django Extensions
- Dummy cache (no caching)
- Verbose logging

**Setup:**
```bash
# Install development requirements
pip install -r requirements/development.txt

# Copy environment file (optional for development)
cp .env.development.example .env

# Run with development settings
python manage.py runserver --settings=voyah.settings.development
# OR set environment variable
export DJANGO_SETTINGS_MODULE=voyah.settings.development
python manage.py runserver
```

### 2. Staging

**Purpose:** Pre-production testing environment that mirrors production.

**Features:**
- DEBUG mode off (configurable)
- PostgreSQL database
- Redis caching
- SMTP email backend
- Gunicorn server
- Sentry integration
- Production-like security settings (configurable)

**Setup:**
```bash
# Install staging requirements
pip install -r requirements/stage.txt

# Copy and configure environment file
cp .env.stage.example .env
# Edit .env with your staging credentials

# Create logs directory
mkdir -p logs

# Run migrations
python manage.py migrate --settings=voyah.settings.stage

# Collect static files
python manage.py collectstatic --noinput --settings=voyah.settings.stage

# Run with Gunicorn
gunicorn voyah.wsgi:application --env DJANGO_SETTINGS_MODULE=voyah.settings.stage
```

### 3. Production

**Purpose:** Live production environment with maximum security and performance.

**Features:**
- DEBUG mode off
- PostgreSQL database with connection pooling
- Redis caching with compression
- SMTP email backend
- Gunicorn server
- WhiteNoise for static files
- Full security headers (HSTS, CSP, etc.)
- Sentry integration
- Admin email notifications
- Rotating file logs

**Setup:**
```bash
# Install production requirements
pip install -r requirements/production.txt

# Copy and configure environment file
cp .env.production.example .env
# Edit .env with your production credentials

# Create logs directory
mkdir -p logs

# Run migrations
python manage.py migrate --settings=voyah.settings.production

# Collect static files
python manage.py collectstatic --noinput --settings=voyah.settings.production

# Run with Gunicorn
gunicorn voyah.wsgi:application \
    --env DJANGO_SETTINGS_MODULE=voyah.settings.production \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --timeout 60 \
    --access-logfile logs/access.log \
    --error-logfile logs/error.log
```

## Environment Variables

Each environment uses environment variables for sensitive configuration. Use the `.env` file or set them in your deployment platform.

### Required for Staging/Production:
- `SECRET_KEY` - Django secret key (generate with `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`)
- `ALLOWED_HOSTS` - Comma-separated list of allowed hosts
- `DB_NAME`, `DB_USER`, `DB_PASSWORD` - Database credentials
- `EMAIL_HOST`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` - Email configuration
- `WAGTAILADMIN_BASE_URL` - Base URL for Wagtail admin

### Optional:
- `DEBUG` - Enable/disable debug mode (default: False for stage/prod)
- `REDIS_URL` - Redis connection URL
- `SENTRY_DSN` - Sentry error tracking DSN
- `SECURE_SSL_REDIRECT` - Force HTTPS redirect

## Switching Between Environments

### Method 1: Command Line Flag
```bash
python manage.py runserver --settings=voyah.settings.development
python manage.py migrate --settings=voyah.settings.stage
```

### Method 2: Environment Variable
```bash
export DJANGO_SETTINGS_MODULE=voyah.settings.production
python manage.py runserver
```

### Method 3: .env File
```bash
# In .env file
DJANGO_SETTINGS_MODULE=voyah.settings.development
```

## Database Setup

### Development (SQLite)
No setup required - SQLite database is created automatically.

### Staging/Production (PostgreSQL)
```bash
# Install PostgreSQL
sudo apt-get install postgresql postgresql-contrib

# Create database and user
sudo -u postgres psql
CREATE DATABASE voyah_stage;
CREATE USER voyah WITH PASSWORD 'your_password';
ALTER ROLE voyah SET client_encoding TO 'utf8';
ALTER ROLE voyah SET default_transaction_isolation TO 'read committed';
ALTER ROLE voyah SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE voyah_stage TO voyah;
\q
```

## Redis Setup (Staging/Production)

```bash
# Install Redis
sudo apt-get install redis-server

# Start Redis
sudo systemctl start redis-server
sudo systemctl enable redis-server

# Test connection
redis-cli ping
# Should return: PONG
```

## Security Checklist for Production

- [ ] Change `SECRET_KEY` to a random string
- [ ] Set `DEBUG=False`
- [ ] Configure `ALLOWED_HOSTS` with your domain
- [ ] Use strong database passwords
- [ ] Enable HTTPS and set `SECURE_SSL_REDIRECT=True`
- [ ] Configure Sentry for error tracking
- [ ] Set up regular database backups
- [ ] Configure firewall rules
- [ ] Use environment variables for all secrets
- [ ] Never commit `.env` files to version control
- [ ] Review and test all security headers

## Deployment Examples

### Using systemd (Linux)
Create `/etc/systemd/system/voyah.service`:
```ini
[Unit]
Description=Wagtail Project
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/voyah
Environment="DJANGO_SETTINGS_MODULE=voyah.settings.production"
ExecStart=/path/to/venv/bin/gunicorn voyah.wsgi:application --bind 0.0.0.0:8000

[Install]
WantedBy=multi-user.target
```

### Using Docker
See `Dockerfile` for containerized deployment.

## Troubleshooting

### Import Error: No module named 'decouple'
```bash
pip install python-decouple
```

### Database Connection Error
Check your database credentials in `.env` and ensure PostgreSQL is running.

### Static Files Not Loading
Run `python manage.py collectstatic` with the appropriate settings module.

### Redis Connection Error
Ensure Redis is running: `sudo systemctl status redis-server`

## Additional Resources

- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/)
- [Wagtail Deployment Guide](https://docs.wagtail.org/en/stable/advanced_topics/deploying.html)
- [Gunicorn Documentation](https://docs.gunicorn.org/)

