# Augment Setup Prompt for Django/Wagtail Projects

Copy and paste this prompt to Augment when starting a new Django/Wagtail project to get a complete multi-environment setup with code quality tools.

---

## 🚀 PROMPT FOR AUGMENT:

```
Please set up a complete Django/Wagtail project with the following configurations:

## 1. Multi-Environment Setup

Create separate requirements and settings files for development, staging, and production:

### Requirements Structure:
- Create `requirements/` directory with:
  - `base.txt` - Core dependencies (Django, Wagtail, PostgreSQL driver, python-decouple)
  - `development.txt` - Development tools (Debug Toolbar, pytest, black, flake8, isort, etc.)
  - `stage.txt` - Staging requirements (Gunicorn, Redis, Sentry)
  - `production.txt` - Production requirements (Gunicorn, Redis, Sentry, security tools)
- Create `requirements.txt` pointing to `requirements/development.txt`

### Settings Structure:
- Refactor `settings.py` into `settings/` directory:
  - `base.py` - Base settings shared across all environments
  - `development.py` - Development settings (DEBUG=True, SQLite, Debug Toolbar)
  - `stage.py` - Staging settings (PostgreSQL, Redis, configurable security)
  - `production.py` - Production settings (PostgreSQL, Redis, full security, WhiteNoise)

### Environment Files:
- Create `.env.development.example` - Minimal development config
- Create `.env.stage.example` - Full staging configuration template
- Create `.env.production.example` - Full production configuration template

### Scripts:
- Create `scripts/setup_development.sh` - Automated development setup
- Create `scripts/setup_stage.sh` - Staging setup script
- Create `scripts/setup_production.sh` - Production setup script
- Make all scripts executable

### Update Run Scripts:
- Update `run.sh` to use `mywagtailproject.settings.development`
- Update `run.bat` to use `mywagtailproject.settings.development`

## 2. Code Quality & Testing Configuration

Create comprehensive code quality and testing setup:

### Configuration Files:
1. **`.gitignore`** - Comprehensive ignore patterns including:
   - Python bytecode and cache
   - Virtual environments
   - Database files
   - Static/media files
   - Environment variables
   - IDE files
   - Test coverage reports (htmlcov/, coverage.xml, .coverage.*)
   - Code quality tool caches (.mypy_cache/, .ruff_cache/, .pytest_cache/)
   - Tool-specific folders (.pylint.d/, .bandit/, .pre-commit-cache/, .black/)
   - Documentation builds (docs/_build/, site/)
   - Database backups (db.sqlite3.backup.*)

2. **`.pre-commit-config.yaml`** - Pre-commit hooks with:
   - General file checks (trailing whitespace, EOF, YAML/JSON validation)
   - Black (line-length=100)
   - isort (profile=black, line-length=100)
   - Flake8 (max-line-length=100, ignore E203,W503)
   - Bandit (security checks, exclude tests/migrations)
   - django-upgrade (target Django version)
   - YAML and Markdown formatters
   - detect-secrets

3. **`pytest.ini`** - Pytest configuration with:
   - Django settings module integration
   - Test discovery patterns
   - Coverage reporting (HTML, terminal, XML)
   - Coverage minimum threshold (80%)
   - Test markers (unit, integration, slow, django_db, wagtail, models, views, forms, api, admin)
   - Logging configuration
   - Database reuse for faster tests
   - Filter warnings appropriately

4. **`setup.cfg`** - Legacy tool configuration for:
   - Flake8 (max-line-length=100, exclusions, per-file ignores)
   - isort (Black-compatible profile)
   - Coverage (branch coverage, exclusions)
   - MyPy (type checking with Django plugin)
   - Pylint (Django-aware configuration)
   - Bandit (security scanning)

5. **`pyproject.toml`** - Modern Python project configuration with:
   - Project metadata
   - Black configuration (line-length=100)
   - isort configuration (Black profile)
   - Pytest configuration (comprehensive settings)
   - Coverage configuration (detailed reporting)
   - MyPy configuration (type checking)
   - Ruff configuration (modern fast linting)
   - Bandit configuration (security)
   - Pylint configuration

6. **`.secrets.baseline`** - Baseline file for detect-secrets

7. **`Makefile`** - Convenient commands for:
   - Installation (install, install-dev, install-stage, install-prod)
   - Setup (setup, setup-hooks)
   - Django management (run, migrate, makemigrations, shell, createsuperuser, collectstatic, check)
   - Testing (test, test-fast, test-unit, test-integration, coverage, coverage-open)
   - Code quality (lint, format, format-check, type-check, security, secrets)
   - Pre-commit (pre-commit, pre-commit-update)
   - Cleaning (clean, clean-db)
   - All-in-one commands (dev, quality, ci)
   - Include colored output for better readability

## 3. Core Models & Wagtail Setup

Create a `core` app with reusable base models and blocks:

### Core App Structure:
- Create `core/` app with `python manage.py startapp core`
- Add `'core'` to INSTALLED_APPS (before 'home')

### Hero/Banner Blocks (StreamField Components):

1. **BannerBlock** - Static banner with:
   - Title, subtitle fields
   - Responsive images (desktop, tablet, mobile)
   - Height options (small/medium/large/full)
   - Overlay opacity (0-100%)
   - Text alignment (left/center/right) and color (white/black)
   - CTA button (text, internal page link, external URL)

2. **SliderBlock** - Image carousel with:
   - ListBlock of slides (2-10 slides)
   - Each slide: title, subtitle, responsive images, CTA
   - Autoplay settings (on/off, speed in milliseconds)
   - Navigation (show/hide arrows and dots)
   - Height, overlay, text alignment options

3. **VideoBlock** - Video banner with:
   - Video URL (YouTube/Vimeo)
   - Poster/fallback image
   - Title, subtitle, CTA overlay
   - Video settings (autoplay, loop, muted, show controls)
   - Height, overlay, text alignment options

4. **ParallaxBlock** - Parallax scrolling with:
   - Large background image (2400x1200px recommended)
   - Parallax speed (slow/medium/fast)
   - Title, subtitle, CTA
   - Height, overlay, text alignment options

### SEOMixin (Abstract Model):
- **og_image** - Social media sharing image (ForeignKey to wagtailimages.Image)
- **twitter_card_type** - Choice field (summary, summary_large_image)
- **canonical_url** - URLField for custom canonical URL
- **no_index** - BooleanField for robots meta tag
- **no_follow** - BooleanField for robots meta tag
- Helper methods: get_meta_title(), get_meta_description(), get_meta_image(), get_robots_tag()
- Promote panels for admin organization
- Note: Don't duplicate seo_title and search_description (Wagtail Page already has these)

### BasePage (Abstract Model):
- Inherit from SEOMixin and Page
- Add `hero` StreamField with all 4 hero blocks (max_num=1, blank=True)
- Helper methods: has_hero(), get_hero_type(), get_hero_data()
- Organize panels: content_panels (with hero), promote_panels (with SEO fields)

### Update HomePage:
- Change from `Page` to inherit from `BasePage`
- Add `body` StreamField for page content (heading, paragraph, image, html blocks)
- Organize content_panels to include hero and body

### Create Migrations:
- Run `python manage.py makemigrations core home`
- Run `python manage.py migrate`

### Template Directory:
- Create `mywagtailproject/templates/blocks/` directory for block templates

## 4. Documentation

Create comprehensive documentation:

1. **`ENVIRONMENTS.md`** - Complete guide covering:
   - Overview of all environments
   - Setup instructions for each environment
   - Database configuration
   - Redis/caching setup
   - Email configuration
   - Security settings
   - Deployment examples
   - Troubleshooting

2. **`ENVIRONMENT_SETUP_SUMMARY.md`** - Quick summary with:
   - What was created
   - Features by environment comparison table
   - Migration path from single settings file

3. **`QUICK_REFERENCE.md`** - Command reference card with:
   - Common commands for each environment
   - Quick setup steps
   - Useful one-liners

4. **`CODE_QUALITY_SETUP.md`** - Comprehensive guide for:
   - Configuration files explanation
   - Getting started with each tool
   - Running tests (basic, markers, coverage)
   - Code formatting (Black, isort)
   - Code linting (Flake8, Ruff, Pylint)
   - Security scanning (Bandit, detect-secrets)
   - Type checking (MyPy)
   - Pre-commit hooks usage
   - Writing tests with examples
   - IDE integration (VS Code, PyCharm)
   - CI/CD integration examples
   - Best practices

5. **`CONFIG_FILES_SUMMARY.md`** - Quick reference with:
   - Files created overview
   - Quick start commands
   - Configuration overview
   - Common workflows
   - Tool configuration summary table
   - Test markers usage
   - IDE integration tips
   - Troubleshooting

6. **`CORE_MODELS_SETUP.md`** - Core models documentation:
   - Overview of core app structure
   - Hero blocks documentation (Banner, Slider, Video, Parallax)
   - SEOMixin and BasePage usage
   - Usage examples for different page types
   - Admin panel organization
   - Next steps (templates, CSS, JavaScript)
   - Customization tips

7. **`HERO_BLOCKS_QUICK_REFERENCE.md`** - Quick reference card:
   - Overview of all 4 hero block types
   - Common settings and options
   - Recommended image sizes
   - How to use in Wagtail admin
   - Best practices and guidelines
   - Troubleshooting tips

## 5. Key Configuration Standards

Use these standards throughout:
- **Line length**: 100 characters
- **Code formatter**: Black
- **Import sorter**: isort (Black profile)
- **Linter**: Flake8 (with Ruff as modern alternative)
- **Test framework**: pytest with pytest-django
- **Coverage minimum**: 80%
- **Python version**: 3.10+
- **Django version**: 5.1+
- **Wagtail version**: 6.3+

## 5. Environment-Specific Features

### Development:
- DEBUG=True
- SQLite database
- Django Debug Toolbar
- Console email backend
- Dummy cache
- Verbose logging

### Staging:
- Configurable DEBUG
- PostgreSQL database
- Redis cache
- SMTP email
- Sentry integration
- File logging
- Production-like security (configurable)

### Production:
- DEBUG=False
- PostgreSQL with connection pooling
- Redis with compression
- WhiteNoise for static files
- Full security headers (HSTS, CSP, SSL)
- Sentry integration
- Rotating file logs
- Gunicorn WSGI server

## 7. Additional Requirements

- Ensure all scripts are executable (chmod +x)
- Update URLs configuration to include Debug Toolbar conditionally
- Create .gitignore with comprehensive patterns for all tools
- Ensure backward compatibility (requirements.txt points to development)
- Include helpful comments in all configuration files
- Add colored output to Makefile for better UX
- Create visual diagrams if helpful
- Create templates/blocks/ directory for hero block templates

## 8. Final Deliverables

Provide:
1. Summary of all files created
2. Quick start guide
3. Verification commands
4. Next steps for the developer
5. Visual diagram of the configuration structure (if applicable)
6. Core models summary with usage examples

Please create all these files and configurations now.
```

---

## 📋 CHECKLIST

After running the prompt, verify these items:

### Files Created:
- [ ] `requirements/base.txt`
- [ ] `requirements/development.txt`
- [ ] `requirements/stage.txt`
- [ ] `requirements/production.txt`
- [ ] `requirements.txt`
- [ ] `mywagtailproject/settings/base.py`
- [ ] `mywagtailproject/settings/development.py`
- [ ] `mywagtailproject/settings/stage.py`
- [ ] `mywagtailproject/settings/production.py`
- [ ] `.env.development.example`
- [ ] `.env.stage.example`
- [ ] `.env.production.example`
- [ ] `scripts/setup_development.sh`
- [ ] `scripts/setup_stage.sh`
- [ ] `scripts/setup_production.sh`
- [ ] `.gitignore`
- [ ] `.pre-commit-config.yaml`
- [ ] `pytest.ini`
- [ ] `setup.cfg`
- [ ] `pyproject.toml`
- [ ] `.secrets.baseline`
- [ ] `Makefile`
- [ ] `core/models.py` (with BannerBlock, SliderBlock, VideoBlock, ParallaxBlock, SEOMixin, BasePage)
- [ ] `mywagtailproject/templates/blocks/` directory
- [ ] `ENVIRONMENTS.md`
- [ ] `ENVIRONMENT_SETUP_SUMMARY.md`
- [ ] `QUICK_REFERENCE.md`
- [ ] `CODE_QUALITY_SETUP.md`
- [ ] `CONFIG_FILES_SUMMARY.md`
- [ ] `CORE_MODELS_SETUP.md`
- [ ] `HERO_BLOCKS_QUICK_REFERENCE.md`

### Files Updated:
- [ ] `run.sh` - Uses development settings
- [ ] `run.bat` - Uses development settings
- [ ] `mywagtailproject/urls.py` - Debug Toolbar integration
- [ ] `mywagtailproject/settings/base.py` - Added 'core' to INSTALLED_APPS
- [ ] `home/models.py` - Updated HomePage to inherit from BasePage

### Migrations Created:
- [ ] Core app migrations (if any models are concrete)
- [ ] Home app migrations (for updated HomePage)

### Verification Commands:
```bash
# Check file structure
ls -la requirements/
ls -la mywagtailproject/settings/
ls -la scripts/

# Verify Makefile works
make help

# Check Python can import settings
python -c "from mywagtailproject.settings import development; print('✓ Settings OK')"

# Verify scripts are executable
ls -l scripts/*.sh

# Check core app and models
python -c "from core.models import BasePage, BannerBlock; print('✓ Core models OK')"

# Verify migrations
python manage.py showmigrations core home
```

---

## 🎯 USAGE TIPS

1. **Copy the entire prompt** from the "PROMPT FOR AUGMENT" section
2. **Paste it into Augment** when starting a new Django/Wagtail project
3. **Wait for completion** - Augment will create all files and configurations
4. **Run verification** using the checklist above
5. **Start development** with `make dev`

## 📝 CUSTOMIZATION

You can customize the prompt by:
- Changing line length (default: 100)
- Adjusting coverage threshold (default: 80%)
- Adding/removing specific tools
- Modifying environment names
- Adding project-specific requirements

## 🔄 UPDATES

Keep this prompt updated when you:
- Add new tools to your workflow
- Change configuration standards
- Update Python/Django/Wagtail versions
- Discover new best practices

---

**Last Updated**: 2024-10-25
**Compatible With**: Django 5.1+, Wagtail 6.3+, Python 3.10+

