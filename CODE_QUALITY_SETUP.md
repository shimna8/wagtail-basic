# Code Quality & Testing Setup

This document explains the code quality tools and testing configuration for the project.

## 📋 Configuration Files

### 1. `.gitignore`
Specifies files and directories that Git should ignore.

**Key exclusions:**
- Python bytecode and cache files
- Virtual environments
- Database files
- Static/media files
- Environment variables
- IDE files
- Test coverage reports

### 2. `.pre-commit-config.yaml`
Configures pre-commit hooks that run automatically before each commit.

**Hooks included:**
- **General checks**: trailing whitespace, file endings, YAML/JSON validation
- **Black**: Python code formatting
- **isort**: Import sorting
- **Flake8**: Code linting
- **Bandit**: Security vulnerability scanning
- **django-upgrade**: Django best practices
- **detect-secrets**: Prevent committing secrets

### 3. `pytest.ini`
Configuration for pytest testing framework.

**Features:**
- Django settings integration
- Test discovery patterns
- Coverage reporting (HTML, terminal, XML)
- Test markers for categorization
- Logging configuration
- Parallel test execution support

### 4. `setup.cfg`
Legacy configuration file for various Python tools.

**Configured tools:**
- Flake8 (linting)
- isort (import sorting)
- Black (formatting)
- Coverage (test coverage)
- MyPy (type checking)
- Pylint (code analysis)
- Bandit (security)

### 5. `pyproject.toml`
Modern Python project configuration (PEP 518).

**Configured tools:**
- Project metadata
- Black (formatting)
- isort (import sorting)
- Pytest (testing)
- Coverage (test coverage)
- MyPy (type checking)
- Bandit (security)
- Ruff (fast linting)

### 6. `.secrets.baseline`
Baseline file for detect-secrets to track known false positives.

## 🚀 Getting Started

### Install Pre-commit Hooks

```bash
# Install pre-commit (if not already installed)
pip install pre-commit

# Install the git hooks
pre-commit install

# (Optional) Run against all files
pre-commit run --all-files
```

### Install Development Dependencies

```bash
# Install all development tools
pip install -r requirements/development.txt

# Or install specific tools
pip install black isort flake8 pytest pytest-django pytest-cov
```

## 🧪 Running Tests

### Basic Test Execution

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest home/tests/test_models.py

# Run specific test function
pytest home/tests/test_models.py::test_homepage_creation

# Run tests matching a pattern
pytest -k "test_model"
```

### Test Markers

```bash
# Run only unit tests
pytest -m unit

# Run only integration tests
pytest -m integration

# Exclude slow tests
pytest -m "not slow"

# Run Wagtail-specific tests
pytest -m wagtail
```

### Coverage Reports

```bash
# Run tests with coverage
pytest --cov

# Generate HTML coverage report
pytest --cov --cov-report=html

# Open coverage report
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

## 🎨 Code Formatting

### Black (Code Formatter)

```bash
# Format all Python files
black .

# Check what would be formatted (dry run)
black --check .

# Format specific file
black myfile.py
```

### isort (Import Sorter)

```bash
# Sort imports in all files
isort .

# Check import sorting (dry run)
isort --check-only .

# Sort imports in specific file
isort myfile.py
```

### Combined Formatting

```bash
# Format code and sort imports
black . && isort .
```

## 🔍 Code Linting

### Flake8

```bash
# Lint all Python files
flake8

# Lint specific file
flake8 myfile.py

# Show statistics
flake8 --statistics
```

### Ruff (Modern, Fast Alternative)

```bash
# Install ruff
pip install ruff

# Lint all files
ruff check .

# Auto-fix issues
ruff check --fix .

# Format code (alternative to black)
ruff format .
```

### Pylint

```bash
# Analyze all Python files
pylint mywagtailproject home search

# Analyze specific file
pylint myfile.py

# Generate report
pylint --output-format=text mywagtailproject > pylint-report.txt
```

## 🔒 Security Scanning

### Bandit

```bash
# Scan for security issues
bandit -r .

# Scan with config from pyproject.toml
bandit -r . -c pyproject.toml

# Generate report
bandit -r . -f json -o bandit-report.json
```

### detect-secrets

```bash
# Scan for secrets
detect-secrets scan

# Update baseline
detect-secrets scan --baseline .secrets.baseline

# Audit findings
detect-secrets audit .secrets.baseline
```

## 📊 Type Checking

### MyPy

```bash
# Type check all files
mypy .

# Type check specific file
mypy myfile.py

# Generate HTML report
mypy --html-report mypy-report .
```

## 🔄 Pre-commit Hooks

### Manual Execution

```bash
# Run all hooks on staged files
pre-commit run

# Run all hooks on all files
pre-commit run --all-files

# Run specific hook
pre-commit run black --all-files
pre-commit run flake8 --all-files

# Update hook versions
pre-commit autoupdate
```

### Skip Hooks (When Needed)

```bash
# Skip all hooks for a commit
git commit --no-verify -m "commit message"

# Skip specific hook
SKIP=flake8 git commit -m "commit message"
```

## 📝 Writing Tests

### Test Structure

```python
# home/tests/test_models.py
import pytest
from django.test import TestCase
from home.models import HomePage

class TestHomePage(TestCase):
    """Tests for HomePage model."""
    
    def test_homepage_creation(self):
        """Test that a HomePage can be created."""
        page = HomePage(title="Test Home")
        page.save()
        assert page.title == "Test Home"

@pytest.mark.django_db
def test_homepage_with_pytest():
    """Test using pytest style."""
    page = HomePage.objects.create(title="Test")
    assert page.title == "Test"
```

### Test Markers

```python
import pytest

@pytest.mark.slow
def test_slow_operation():
    """This test takes a long time."""
    pass

@pytest.mark.integration
def test_api_integration():
    """Integration test for API."""
    pass

@pytest.mark.unit
def test_simple_function():
    """Simple unit test."""
    pass
```

## 🛠️ IDE Integration

### VS Code

Create `.vscode/settings.json`:

```json
{
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": false,
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    }
}
```

### PyCharm

1. Go to **Settings** → **Tools** → **Black**
2. Enable "Run Black on save"
3. Go to **Settings** → **Tools** → **Python Integrated Tools**
4. Set default test runner to "pytest"

## 📈 Continuous Integration

### GitHub Actions Example

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install -r requirements/development.txt
      - name: Run pre-commit
        run: pre-commit run --all-files
      - name: Run tests
        run: pytest --cov
      - name: Upload coverage
        uses: codecov/codecov-action@v3
```

## 🎯 Best Practices

1. **Always run tests before committing**
   ```bash
   pytest && git commit
   ```

2. **Format code automatically**
   ```bash
   black . && isort . && git add -u
   ```

3. **Check code quality**
   ```bash
   flake8 && pylint mywagtailproject
   ```

4. **Maintain test coverage above 80%**
   ```bash
   pytest --cov --cov-fail-under=80
   ```

5. **Use pre-commit hooks** - They catch issues before commit

6. **Write meaningful test names** - Use descriptive names that explain what is being tested

7. **Keep tests fast** - Mark slow tests with `@pytest.mark.slow`

8. **Test one thing at a time** - Each test should verify a single behavior

## 📚 Additional Resources

- [Black Documentation](https://black.readthedocs.io/)
- [isort Documentation](https://pycqa.github.io/isort/)
- [Flake8 Documentation](https://flake8.pycqa.org/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Pre-commit Documentation](https://pre-commit.com/)
- [Django Testing](https://docs.djangoproject.com/en/5.1/topics/testing/)
- [Wagtail Testing](https://docs.wagtail.org/en/stable/advanced_topics/testing.html)

