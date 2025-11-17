# Setup Documentation Index

This project includes comprehensive setup documentation for creating production-ready Django/Wagtail projects with multi-environment configuration and code quality tools.

---

## 📚 Documentation Overview

### For Future Projects (Augment Prompts)

#### 1. **QUICK_SETUP_PROMPT.md** ⚡
**Best for**: Fast project setup

A condensed, copy-paste ready prompt for Augment that creates the entire setup in 5-10 minutes.

**Use when**:
- You want to quickly set up a new project
- You're familiar with the setup and don't need detailed explanations
- You trust the default configurations

**Size**: ~2.6 KB (very concise)

---

#### 2. **AUGMENT_SETUP_PROMPT.md** 📘
**Best for**: Detailed, controlled setup

A comprehensive prompt with full specifications, explanations, and verification checklist.

**Use when**:
- Setting up your first project with this configuration
- You need to understand what each component does
- You want to customize specific parts
- You need a reference for what should be created

**Size**: ~9.9 KB (detailed)

**Includes**:
- Complete specifications for all files
- Detailed configuration standards
- Comprehensive verification checklist
- Usage tips and customization guide

---

#### 3. **SETUP_STEPS_CHECKLIST.md** ✅
**Best for**: Manual setup or learning

A step-by-step checklist organized in 4 phases with 22 detailed steps.

**Use when**:
- You want to set up manually (without Augment)
- You need to understand the process in detail
- You're learning how to configure Django/Wagtail projects
- You want to customize heavily during setup

**Size**: ~13 KB (very detailed)

**Includes**:
- 4 phases: Multi-Environment, Code Quality, Documentation, Verification
- 22 main steps with detailed sub-tasks
- Post-setup tasks
- Success criteria
- Time estimates

---

## 🚀 Quick Start Guide

### Option 1: Fast Setup with Augment (Recommended)

1. Open **QUICK_SETUP_PROMPT.md**
2. Copy the entire prompt section
3. Paste into Augment
4. Wait 5-10 minutes
5. Verify setup:
   ```bash
   make help
   python -c "from voyah.settings import development"
   ```
6. Start developing:
   ```bash
   make dev
   make run
   ```

### Option 2: Detailed Setup with Augment

1. Open **AUGMENT_SETUP_PROMPT.md**
2. Review and customize if needed
3. Copy the prompt section
4. Paste into Augment
5. Wait 5-10 minutes
6. Use the included checklist to verify
7. Start developing

### Option 3: Manual Setup

1. Open **SETUP_STEPS_CHECKLIST.md**
2. Follow each step in order
3. Check off items as you complete them
4. Takes 30-45 minutes
5. Verify using success criteria
6. Start developing

---

## 📋 What Gets Created

### Multi-Environment Setup
- **Requirements**: `requirements/` with base, development, stage, production
- **Settings**: `settings/` with base, development, stage, production
- **Environment Templates**: `.env.*.example` files
- **Setup Scripts**: `scripts/setup_*.sh` for each environment

### Code Quality & Testing
- **Configuration Files**: `.gitignore`, `.pre-commit-config.yaml`, `pytest.ini`, `setup.cfg`, `pyproject.toml`
- **Tools Configured**: Black, isort, Flake8, Ruff, Pytest, Coverage, MyPy, Pylint, Bandit, detect-secrets
- **Makefile**: 40+ convenient commands
- **Secrets Baseline**: `.secrets.baseline`

### Documentation
- **ENVIRONMENTS.md**: Complete environment guide
- **ENVIRONMENT_SETUP_SUMMARY.md**: Quick summary
- **QUICK_REFERENCE.md**: Command reference
- **CODE_QUALITY_SETUP.md**: Tool usage guide
- **CONFIG_FILES_SUMMARY.md**: Configuration overview

---

## 🎯 Configuration Standards

All setups use these standards:

| Setting | Value |
|---------|-------|
| Line Length | 100 characters |
| Code Formatter | Black |
| Import Sorter | isort (Black profile) |
| Linter | Flake8 + Ruff |
| Test Framework | pytest + pytest-django |
| Coverage Minimum | 80% |
| Python Version | 3.10+ |
| Django Version | 5.1+ |
| Wagtail Version | 6.3+ |

---

## 🛠️ Environment Features

### Development
- SQLite database
- Django Debug Toolbar
- Console email backend
- Dummy cache
- Verbose logging
- DEBUG=True

### Staging
- PostgreSQL database
- Redis cache
- SMTP email
- Sentry integration
- Configurable security
- File logging

### Production
- PostgreSQL with pooling
- Redis with compression
- WhiteNoise static files
- Full security headers
- Sentry integration
- Rotating logs
- Gunicorn WSGI server
- DEBUG=False

---

## 📊 File Statistics

**Total Files Created**: ~25 files
**Total Directories**: 3 (requirements/, settings/, scripts/)
**Total Documentation**: 5 comprehensive guides
**Makefile Commands**: 40+ commands
**Tools Configured**: 10+ tools

---

## ✅ Verification Commands

After setup, verify everything works:

```bash
# Check file structure
ls requirements/ voyah/settings/ scripts/

# Test Makefile
make help

# Verify settings import
python -c "from voyah.settings import development"

# Check project info
make info

# Run system checks
make check

# (Optional) Run all quality checks
make quality
```

---

## 🎓 Learning Path

### Beginner
1. Start with **SETUP_STEPS_CHECKLIST.md**
2. Follow each step manually
3. Understand what each file does
4. Takes longer but you learn more

### Intermediate
1. Use **AUGMENT_SETUP_PROMPT.md**
2. Review the specifications
3. Let Augment create the files
4. Study the created files afterward

### Advanced
1. Use **QUICK_SETUP_PROMPT.md**
2. Quick setup in minutes
3. Customize as needed
4. Focus on building features

---

## 🔄 Maintenance

### Updating the Prompts

When you discover improvements:

1. Update **SETUP_STEPS_CHECKLIST.md** first (source of truth)
2. Update **AUGMENT_SETUP_PROMPT.md** with new specifications
3. Update **QUICK_SETUP_PROMPT.md** with condensed version
4. Test the prompts on a new project
5. Update version numbers and dates

### Version Control

Keep these documents in your project template repository:
```bash
git add AUGMENT_SETUP_PROMPT.md QUICK_SETUP_PROMPT.md SETUP_STEPS_CHECKLIST.md
git commit -m "Update setup documentation"
```

---

## 💡 Tips & Best Practices

### Using with Augment

1. **Copy the entire prompt** - Don't modify while copying
2. **Wait for completion** - Don't interrupt Augment
3. **Verify immediately** - Check files were created correctly
4. **Customize after** - Make changes after initial setup

### Customization

Common customizations:
- Change line length (default: 100)
- Adjust coverage threshold (default: 80%)
- Add/remove specific tools
- Modify environment names
- Add project-specific requirements

### Troubleshooting

If setup fails:
1. Check Augment completed all steps
2. Verify file permissions on scripts
3. Check Python/Django/Wagtail versions
4. Review error messages carefully
5. Consult the detailed documentation

---

## 📞 Support

### Documentation Files

- **ENVIRONMENTS.md** - Environment configuration help
- **CODE_QUALITY_SETUP.md** - Tool usage help
- **CONFIG_FILES_SUMMARY.md** - Quick reference
- **QUICK_REFERENCE.md** - Command reference

### Common Issues

**Settings import fails**:
```bash
# Check DJANGO_SETTINGS_MODULE
echo $DJANGO_SETTINGS_MODULE

# Try explicit import
python -c "from voyah.settings.development import *"
```

**Makefile not working**:
```bash
# Check make is installed
make --version

# Try running commands directly
python manage.py runserver --settings=voyah.settings.development
```

**Pre-commit hooks failing**:
```bash
# Update hooks
pre-commit autoupdate

# Run manually to see errors
pre-commit run --all-files
```

---

## 🎉 Success Criteria

Your setup is complete when:

✅ All files from checklist exist  
✅ `make help` shows all commands  
✅ Settings import works  
✅ `make test` runs successfully  
✅ `make format` formats code  
✅ `make run` starts server  
✅ All documentation is readable  

---

## 📈 Next Steps After Setup

1. **Install pre-commit hooks**: `make setup-hooks`
2. **Run quality checks**: `make quality`
3. **Create initial tests**: Write tests in `home/tests/`
4. **Configure IDE**: Set Black formatter, pytest runner
5. **Create superuser**: `make createsuperuser`
6. **Start development**: `make run`
7. **Read documentation**: Review all .md files

---

## 📅 Maintenance Schedule

- **Weekly**: Update pre-commit hooks (`make pre-commit-update`)
- **Monthly**: Review and update dependencies
- **Quarterly**: Review and update documentation
- **Yearly**: Update Python/Django/Wagtail versions

---

**Last Updated**: 2024-10-25  
**Version**: 1.0.0  
**Compatible With**: Django 5.1+, Wagtail 6.3+, Python 3.10+  
**Maintained By**: Your Team  

---

## 📄 License

These setup documents are part of your project and follow your project's license.

---

**Happy Coding! 🚀**

