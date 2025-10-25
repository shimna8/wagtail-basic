# Quick Setup Prompt for Augment

A condensed version for quick copy-paste into Augment.

---

## 🚀 COPY THIS PROMPT:

```
Set up a complete Django/Wagtail project with multi-environment configuration and code quality tools:

1. MULTI-ENVIRONMENT SETUP:
   - Create requirements/ directory: base.txt, development.txt, stage.txt, production.txt
   - Create settings/ directory: base.py, development.py, stage.py, production.py
   - Create .env examples: .env.development.example, .env.stage.example, .env.production.example
   - Create setup scripts: scripts/setup_development.sh, scripts/setup_stage.sh, scripts/setup_production.sh
   - Update run.sh and run.bat to use development settings

2. CODE QUALITY CONFIGURATION:
   - .gitignore - Comprehensive patterns (include all tool caches: .mypy_cache/, .ruff_cache/, .pytest_cache/, .pylint.d/, .bandit/, .pre-commit-cache/, htmlcov/, coverage.xml, docs/_build/, db.sqlite3.backup.*)
   - .pre-commit-config.yaml - Hooks: black, isort, flake8, bandit, django-upgrade, detect-secrets
   - pytest.ini - Django integration, coverage (80% min), markers (unit, integration, slow, etc.)
   - setup.cfg - Flake8, isort, coverage, mypy, pylint, bandit
   - pyproject.toml - Modern config for all tools + Ruff
   - .secrets.baseline - For detect-secrets
   - Makefile - Commands: help, dev, run, test, coverage, format, lint, quality, clean (with colors)

3. CORE MODELS & WAGTAIL SETUP:
   - Create core/ app, add to INSTALLED_APPS
   - BannerBlock - Static banner with responsive images (desktop/tablet/mobile), height options, overlay, text alignment, CTA
   - SliderBlock - Image carousel (2-10 slides), autoplay, arrows/dots navigation, per-slide content
   - VideoBlock - YouTube/Vimeo embed, poster image, video controls, overlay content
   - ParallaxBlock - Parallax scrolling effect, speed control, large background image
   - SEOMixin - og_image, twitter_card_type, canonical_url, no_index, no_follow (don't duplicate seo_title/search_description)
   - BasePage - Abstract base with hero StreamField (max 1 block), inherits SEOMixin
   - Update HomePage to inherit from BasePage, add body StreamField
   - Create migrations and migrate
   - Create templates/blocks/ directory

4. DOCUMENTATION:
   - ENVIRONMENTS.md - Complete environment guide
   - ENVIRONMENT_SETUP_SUMMARY.md - Quick summary
   - QUICK_REFERENCE.md - Command reference
   - CODE_QUALITY_SETUP.md - Tool usage guide
   - CONFIG_FILES_SUMMARY.md - Configuration overview
   - CORE_MODELS_SETUP.md - Core models documentation
   - HERO_BLOCKS_QUICK_REFERENCE.md - Hero blocks quick reference

5. STANDARDS:
   - Line length: 100
   - Formatter: Black
   - Import sorter: isort (black profile)
   - Linter: Flake8 + Ruff
   - Testing: pytest + pytest-django
   - Coverage: 80% minimum
   - Python: 3.10+, Django: 5.1+, Wagtail: 6.3+

5. ENVIRONMENT FEATURES:
   - Development: SQLite, Debug Toolbar, console email, dummy cache
   - Staging: PostgreSQL, Redis, Sentry, configurable security
   - Production: PostgreSQL pooling, Redis compression, WhiteNoise, full security, Gunicorn

6. HERO BLOCK FEATURES:
   - Responsive images (desktop 1920x600, tablet 1024x600, mobile 768x600)
   - Height options (small 400px, medium 600px, large 800px, full screen)
   - Overlay opacity (0-100%), text alignment (L/C/R), text color (W/B)
   - CTA buttons with internal/external links
   - Slider: 2-10 slides, autoplay, navigation
   - Video: YouTube/Vimeo, poster image, controls
   - Parallax: Speed control, large backgrounds

Create all files with comprehensive configurations and provide a summary.
```

---

## ✅ QUICK VERIFICATION:

```bash
# Check structure
ls requirements/ mywagtailproject/settings/ scripts/

# Test Makefile
make help

# Verify settings
python -c "from mywagtailproject.settings import development"

# Start development
make dev
```

---

**Use this for**: Quick project setup when you don't need detailed explanations.
**Use AUGMENT_SETUP_PROMPT.md for**: Detailed setup with full specifications.

