# Django/Wagtail Project Setup - Step-by-Step Checklist

Complete checklist of all steps performed to set up a production-ready Django/Wagtail project with multi-environment configuration and code quality tools.

---

## 📋 PHASE 1: Multi-Environment Setup

### Step 1: Create Requirements Structure
- [ ] Create `requirements/` directory
- [ ] Create `requirements/base.txt` with core dependencies:
  - Django, Wagtail, psycopg2-binary, python-decouple, pytz
- [ ] Create `requirements/development.txt` with dev tools:
  - Include: `-r base.txt`
  - Add: django-debug-toolbar, django-extensions, pytest, pytest-django, pytest-cov
  - Add: black, flake8, isort, pylint, mypy, bandit
  - Add: Sphinx (documentation)
- [ ] Create `requirements/stage.txt` with staging requirements:
  - Include: `-r base.txt`
  - Add: gunicorn, whitenoise, sentry-sdk, django-redis
- [ ] Create `requirements/production.txt` with production requirements:
  - Include: `-r base.txt`
  - Add: gunicorn, whitenoise, sentry-sdk, django-redis, django-csp
- [ ] Create `requirements.txt` pointing to `requirements/development.txt`

### Step 2: Refactor Settings Structure
- [ ] Create `voyah/settings/` directory
- [ ] Create `voyah/settings/__init__.py` (empty)
- [ ] Move and refactor `settings.py` to `settings/base.py`:
  - Remove environment-specific settings
  - Keep: INSTALLED_APPS, MIDDLEWARE, TEMPLATES, AUTH_PASSWORD_VALIDATORS
  - Keep: LANGUAGE_CODE, TIME_ZONE, USE_I18N, USE_TZ
  - Keep: STATIC_URL, STATICFILES_DIRS, MEDIA_URL, MEDIA_ROOT
  - Keep: WAGTAIL_SITE_NAME, WAGTAILADMIN_BASE_URL
  - Use python-decouple for SECRET_KEY and other env vars
- [ ] Create `settings/development.py`:
  - Import from base: `from .base import *`
  - Set: DEBUG = True
  - Configure: SQLite database
  - Add: django-debug-toolbar to INSTALLED_APPS and MIDDLEWARE
  - Set: EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
  - Set: CACHES = dummy cache
  - Configure: Verbose logging
- [ ] Create `settings/stage.py`:
  - Import from base: `from .base import *`
  - Set: Configurable DEBUG via env var
  - Configure: PostgreSQL database
  - Configure: Redis cache
  - Configure: SMTP email
  - Add: Sentry integration
  - Set: Medium security settings
  - Configure: File logging
- [ ] Create `settings/production.py`:
  - Import from base: `from .base import *`
  - Set: DEBUG = False
  - Configure: PostgreSQL with connection pooling
  - Configure: Redis with compression
  - Add: WhiteNoise to MIDDLEWARE
  - Set: Full security headers (SECURE_SSL_REDIRECT, HSTS, CSP)
  - Add: Sentry integration
  - Configure: Rotating file logs
  - Set: ALLOWED_HOSTS from env var

### Step 3: Create Environment Variable Templates
- [ ] Create `.env.development.example`:
  - DJANGO_SETTINGS_MODULE=voyah.settings.development
  - SECRET_KEY (example)
- [ ] Create `.env.stage.example`:
  - All staging configuration variables
  - Database, Redis, Email, Sentry, Security settings
- [ ] Create `.env.production.example`:
  - All production configuration variables
  - Strict security settings

### Step 4: Create Setup Scripts
- [ ] Create `scripts/` directory
- [ ] Create `scripts/setup_development.sh`:
  - Create virtual environment
  - Install requirements/development.txt
  - Run migrations
  - Offer to create superuser
- [ ] Create `scripts/setup_stage.sh`:
  - Check for .env.stage file
  - Install requirements/stage.txt
  - Run migrations with stage settings
  - Collect static files
- [ ] Create `scripts/setup_production.sh`:
  - Check for .env.production file
  - Install requirements/production.txt
  - Run migrations with production settings
  - Collect static files
  - Run security checks
- [ ] Make all scripts executable: `chmod +x scripts/*.sh`

### Step 5: Update Run Scripts
- [ ] Update `run.sh`:
  - Set DJANGO_SETTINGS_MODULE=voyah.settings.development
  - Run migrations
  - Collect static files
  - Start development server
- [ ] Update `run.bat`:
  - Same as run.sh but for Windows

### Step 6: Update URL Configuration
- [ ] Edit `voyah/urls.py`:
  - Add conditional Debug Toolbar URLs for development
  ```python
  if settings.DEBUG:
      try:
          import debug_toolbar
          urlpatterns = [
              path('__debug__/', include(debug_toolbar.urls)),
          ] + urlpatterns
      except ImportError:
          pass
  ```

---

## 📋 PHASE 2: Code Quality & Testing Configuration

### Step 7: Create/Enhance .gitignore
- [ ] Create or enhance `.gitignore` with:
  - Python bytecode: `*.pyc`, `*.pyo`, `__pycache__/`
  - Virtual environments: `venv/`, `env/`, `.venv/`
  - Django: `*.log`, `db.sqlite3`, `/static/`, `/media/`, `logs/`
  - Environment variables: `.env`, `.env.local`, `.env.*.local`
  - IDE: `.vscode/`, `.idea/`, `*.swp`, `.DS_Store`
  - Testing: `.coverage`, `.coverage.*`, `htmlcov/`, `.pytest_cache/`, `coverage.xml`, `.cache/`, `test-results/`, `*.cover`
  - Distribution: `dist/`, `build/`, `*.egg-info/`
  - MyPy: `.mypy_cache/`, `.dmypy.json`
  - Ruff: `.ruff_cache/`
  - Pylint: `pylint-report.txt`, `.pylint.d/`
  - Bandit: `bandit-report.json`, `.bandit/`
  - Pre-commit: `.pre-commit-cache/`
  - Black: `.black/`
  - Documentation: `docs/_build/`, `site/`
  - Database backups: `db.sqlite3.backup.*`
  - Node: `node_modules/`, `npm-debug.log`
  - Jupyter: `.ipynb_checkpoints`
  - Celery: `celerybeat-schedule`, `celerybeat.pid`
  - Compiled translations: `*.mo`, `*.pot`

### Step 8: Create Pre-commit Configuration
- [ ] Create `.pre-commit-config.yaml`:
  - Add pre-commit-hooks repo (trailing whitespace, EOF, YAML/JSON checks, large files, merge conflicts)
  - Add black hook (line-length=100)
  - Add isort hook (profile=black, line-length=100)
  - Add flake8 hook (max-line-length=100, extend-ignore=E203,W503)
  - Add bandit hook (exclude tests and migrations)
  - Add django-upgrade hook (target Django version)
  - Add prettier for YAML/Markdown
  - Add detect-secrets hook

### Step 9: Create Pytest Configuration
- [ ] Create `pytest.ini`:
  - Set DJANGO_SETTINGS_MODULE = voyah.settings.development
  - Configure test discovery patterns
  - Set testpaths (home, search, tests)
  - Add addopts: -v, -ra, --showlocals, --strict-markers, --strict-config
  - Configure coverage: --cov, --cov-report=html/term/xml, --cov-fail-under=80
  - Add --reuse-db for faster tests
  - Define markers: slow, integration, unit, smoke, django_db, wagtail, models, views, forms, api, admin
  - Configure logging (console and file)
  - Add coverage configuration sections

### Step 10: Create setup.cfg
- [ ] Create `setup.cfg`:
  - Add [metadata] section with project info
  - Add [flake8] section:
    - max-line-length = 100
    - max-complexity = 10
    - exclude patterns
    - extend-ignore = E203, W503, E501
    - per-file-ignores for __init__.py and settings
  - Add [isort] section:
    - profile = black
    - line_length = 100
    - known_django, known_wagtail, known_first_party
  - Add [coverage:run], [coverage:report], [coverage:html] sections
  - Add [mypy] section with Django plugin
  - Add [pylint] section with Django plugin
  - Add [bandit] section

### Step 11: Create pyproject.toml
- [ ] Create `pyproject.toml`:
  - Add [build-system] section
  - Add [project] section with metadata
  - Add [tool.black] section (line-length=100)
  - Add [tool.isort] section (black profile)
  - Add [tool.pytest.ini_options] section (comprehensive)
  - Add [tool.coverage.*] sections
  - Add [tool.mypy] section
  - Add [tool.bandit] section
  - Add [tool.pylint.*] sections
  - Add [tool.ruff] section (modern linter)
  - Add [tool.ruff.lint] section with rules

### Step 12: Create Secrets Baseline
- [ ] Create `.secrets.baseline`:
  - JSON file with detect-secrets configuration
  - List of plugins
  - Filters configuration
  - Empty results object

### Step 13: Create Makefile
- [ ] Create `Makefile` with targets:
  - help - Show all commands
  - install, install-dev, install-stage, install-prod
  - setup, setup-hooks
  - run, migrate, makemigrations, shell, shell-plus, createsuperuser, collectstatic
  - check, check-deploy
  - test, test-fast, test-unit, test-integration, test-watch
  - coverage, coverage-open
  - lint, lint-flake8, lint-pylint, lint-ruff
  - format, format-check
  - type-check, security, secrets
  - pre-commit, pre-commit-update
  - quality (run all checks)
  - clean, clean-db
  - build, docker-build, docker-run
  - db-reset, db-backup
  - docs, info, requirements
  - dev (complete setup), ci (CI checks)
  - Add colored output for better UX

---

## 📋 PHASE 3: Documentation

### Step 14: Create Environment Documentation
- [ ] Create `ENVIRONMENTS.md`:
  - Overview of all environments
  - Detailed setup instructions for each
  - Database configuration examples
  - Redis/caching setup
  - Email configuration
  - Security settings explanation
  - Deployment examples (Gunicorn, systemd, nginx)
  - Troubleshooting section

### Step 15: Create Setup Summary
- [ ] Create `ENVIRONMENT_SETUP_SUMMARY.md`:
  - What was created overview
  - Features by environment comparison table
  - Quick start commands
  - Migration path from single settings

### Step 16: Create Quick Reference
- [ ] Create `QUICK_REFERENCE.md`:
  - Common commands for each environment
  - Installation commands
  - Testing commands
  - Deployment commands
  - Useful one-liners

### Step 17: Create Code Quality Documentation
- [ ] Create `CODE_QUALITY_SETUP.md`:
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

### Step 18: Create Configuration Summary
- [ ] Create `CONFIG_FILES_SUMMARY.md`:
  - Files created overview
  - Quick start commands
  - Configuration overview
  - Common workflows
  - Tool configuration summary table
  - Test markers usage
  - IDE integration tips
  - Troubleshooting

---

## 📋 PHASE 4: Core Models & Wagtail Setup

### Step 19: Create Core App
- [ ] Create core app: `python manage.py startapp core`
- [ ] Add `'core'` to INSTALLED_APPS in `settings/base.py` (before 'home')

### Step 20: Create Hero/Banner Blocks
- [ ] Create `core/models.py` with StreamField blocks:
  - **BannerBlock** - Static banner with:
    - Title, subtitle fields
    - Responsive images (desktop, tablet, mobile) using ImageChooserBlock
    - Height choices (small/medium/large/full)
    - Overlay opacity (IntegerBlock 0-100)
    - Text alignment and color choices
    - CTA fields (text, page link, external URL)
  - **SliderBlock** - Image carousel with:
    - Nested SlideBlock (StructBlock) with title, subtitle, images, CTA
    - ListBlock of slides (min 2, max 10)
    - Autoplay settings (BooleanBlock, IntegerBlock for speed)
    - Navigation options (show arrows, show dots)
    - Height, overlay, text alignment
  - **VideoBlock** - Video banner with:
    - Video URL (URLBlock for YouTube/Vimeo)
    - Poster image (ImageChooserBlock)
    - Title, subtitle, CTA overlay
    - Video settings (autoplay, loop, muted, controls)
    - Height, overlay, text alignment
  - **ParallaxBlock** - Parallax scrolling with:
    - Background image (ImageChooserBlock, large size)
    - Parallax speed choices (slow/medium/fast)
    - Title, subtitle, CTA
    - Height, overlay, text alignment

### Step 21: Create SEOMixin
- [ ] Create `SEOMixin` abstract model in `core/models.py`:
  - Add `og_image` (ForeignKey to wagtailimages.Image)
  - Add `twitter_card_type` (CharField with choices)
  - Add `canonical_url` (URLField)
  - Add `no_index` (BooleanField)
  - Add `no_follow` (BooleanField)
  - Add helper methods: `get_meta_title()`, `get_meta_description()`, `get_meta_image()`, `get_robots_tag()`
  - Add promote_panels with MultiFieldPanel organization
  - **Important**: Don't duplicate `seo_title` and `search_description` (Wagtail Page already has these)

### Step 22: Create BasePage
- [ ] Create `BasePage` abstract model in `core/models.py`:
  - Inherit from `SEOMixin` and `Page`
  - Add `hero` StreamField with all 4 blocks (BannerBlock, SliderBlock, VideoBlock, ParallaxBlock)
  - Set `max_num=1`, `blank=True`, `null=True`, `use_json_field=True`
  - Add helper methods: `has_hero()`, `get_hero_type()`, `get_hero_data()`
  - Organize content_panels (include hero field)
  - Combine promote_panels (Page.promote_panels + SEOMixin.promote_panels)

### Step 23: Update HomePage
- [ ] Update `home/models.py`:
  - Import `BasePage` from `core.models`
  - Change `HomePage` to inherit from `BasePage` instead of `Page`
  - Add `body` StreamField for page content (heading, paragraph, image, html blocks)
  - Set `use_json_field=True` for StreamFields
  - Update content_panels: `BasePage.content_panels + [FieldPanel('body')]`
  - Add verbose_name in Meta

### Step 24: Create Template Directory
- [ ] Create `voyah/templates/blocks/` directory
- [ ] This will hold block templates (banner_block.html, slider_block.html, etc.)

### Step 25: Create Migrations
- [ ] Run migrations for core app: `python manage.py makemigrations core`
- [ ] Run migrations for home app: `python manage.py makemigrations home`
- [ ] Apply migrations: `python manage.py migrate`
- [ ] Verify migrations applied successfully

### Step 26: Create Core Models Documentation
- [ ] Create `CORE_MODELS_SETUP.md`:
  - Overview of core app structure
  - Documentation for all 4 hero blocks
  - SEOMixin and BasePage usage guide
  - Usage examples for different page types
  - Admin panel organization
  - Next steps (templates, CSS, JavaScript)
  - Customization tips
  - Verification checklist

- [ ] Create `HERO_BLOCKS_QUICK_REFERENCE.md`:
  - Overview of all 4 hero block types
  - Common settings and options table
  - Recommended image sizes
  - How to use in Wagtail admin
  - Best practices and guidelines
  - Troubleshooting tips
  - Common use cases

---

## 📋 PHASE 5: Verification & Final Steps

### Step 27: Verify File Structure
- [ ] Check all files exist:
  ```bash
  ls requirements/
  ls voyah/settings/
  ls scripts/
  ls core/
  ls voyah/templates/blocks/
  ls -la .gitignore .pre-commit-config.yaml pytest.ini setup.cfg pyproject.toml
  ```

### Step 28: Verify Configuration
- [ ] Test Makefile: `make help`
- [ ] Test settings import: `python -c "from voyah.settings import development"`
- [ ] Check scripts are executable: `ls -l scripts/*.sh`
- [ ] Test core models import: `python -c "from core.models import BasePage, BannerBlock; print('✓ Core models OK')"`
- [ ] Verify migrations: `python manage.py showmigrations core home`

### Step 29: Create Summary Documents
- [ ] Create `AUGMENT_SETUP_PROMPT.md` - Full prompt for future use
- [ ] Create `QUICK_SETUP_PROMPT.md` - Condensed prompt
- [ ] Create `SETUP_STEPS_CHECKLIST.md` - This document

### Step 30: Final Verification
- [ ] Run `make info` to check versions
- [ ] Run `make check` to verify Django configuration
- [ ] Optionally run `make quality` to test all tools
- [ ] Test in Wagtail admin (optional):
  - Start server: `make run`
  - Login to admin
  - Edit HomePage
  - Try adding a hero block
  - Verify all fields appear correctly

---

## 🎯 POST-SETUP TASKS

After completing all steps above:

1. **Install Pre-commit Hooks**:
   ```bash
   make setup-hooks
   ```

2. **Run Initial Quality Check**:
   ```bash
   make quality
   ```

3. **Create Initial Tests**:
   - Create test files in `home/tests/`
   - Write basic model, view, and form tests

4. **Configure IDE**:
   - Set Black as formatter
   - Set pytest as test runner
   - Enable format on save

5. **Initialize Git** (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial project setup with multi-environment config"
   ```

6. **Create First Superuser**:
   ```bash
   make createsuperuser
   ```

7. **Start Development**:
   ```bash
   make run
   ```

---

## 📊 SUMMARY STATISTICS

**Total Files Created**: ~30 files
**Total Directories Created**: 5 directories (requirements/, settings/, scripts/, core/, templates/blocks/)
**Total Files Modified**: 5 files (run.sh, run.bat, urls.py, settings/base.py, home/models.py)
**Total Documentation Pages**: 7 comprehensive guides
**Total Makefile Commands**: 40+ commands
**Total Configuration Tools**: 10+ tools configured
**Total Hero Blocks**: 4 types (Banner, Slider, Video, Parallax)
**Total Models**: 2 (SEOMixin, BasePage - both abstract)

---

## ✅ SUCCESS CRITERIA

Your setup is complete when:
- ✅ All files in checklist exist
- ✅ `make help` shows all commands
- ✅ `python -c "from voyah.settings import development"` works
- ✅ `make test` runs (even if no tests exist yet)
- ✅ `make format` formats code successfully
- ✅ `make run` starts the development server
- ✅ All documentation is readable and accurate

---

**Last Updated**: 2024-10-25
**Time to Complete**: ~30-45 minutes (manual) or ~5-10 minutes (with Augment)
**Difficulty**: Intermediate
**Maintenance**: Update when adding new tools or changing standards

