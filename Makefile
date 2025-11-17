.PHONY: help install install-dev install-stage install-prod setup test coverage lint format clean run migrate makemigrations shell createsuperuser collectstatic check pre-commit

# Default target
.DEFAULT_GOAL := help

# Variables
PYTHON := python
PIP := pip
MANAGE := $(PYTHON) manage.py
SETTINGS_DEV := --settings=voyah.settings.development
SETTINGS_STAGE := --settings=voyah.settings.stage
SETTINGS_PROD := --settings=voyah.settings.production

# Colors for output
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[1;33m
RED := \033[0;31m
NC := \033[0m # No Color

help: ## Show this help message
	@echo "$(BLUE)Available commands:$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-20s$(NC) %s\n", $$1, $$2}'

# Installation targets
install: ## Install base requirements
	@echo "$(YELLOW)Installing base requirements...$(NC)"
	$(PIP) install -r requirements/base.txt

install-dev: ## Install development requirements
	@echo "$(YELLOW)Installing development requirements...$(NC)"
	$(PIP) install -r requirements/development.txt
	@echo "$(GREEN)✓ Development requirements installed$(NC)"

install-stage: ## Install staging requirements
	@echo "$(YELLOW)Installing staging requirements...$(NC)"
	$(PIP) install -r requirements/stage.txt
	@echo "$(GREEN)✓ Staging requirements installed$(NC)"

install-prod: ## Install production requirements
	@echo "$(YELLOW)Installing production requirements...$(NC)"
	$(PIP) install -r requirements/production.txt
	@echo "$(GREEN)✓ Production requirements installed$(NC)"

# Setup targets
setup: install-dev ## Setup development environment
	@echo "$(YELLOW)Setting up development environment...$(NC)"
	$(MANAGE) migrate $(SETTINGS_DEV)
	@echo "$(GREEN)✓ Development environment ready$(NC)"
	@echo "$(BLUE)Run 'make createsuperuser' to create an admin user$(NC)"

setup-hooks: ## Install pre-commit hooks
	@echo "$(YELLOW)Installing pre-commit hooks...$(NC)"
	pre-commit install
	@echo "$(GREEN)✓ Pre-commit hooks installed$(NC)"

# Django management targets
run: ## Run development server
	@echo "$(BLUE)Starting development server...$(NC)"
	$(MANAGE) runserver $(SETTINGS_DEV)

migrate: ## Run database migrations (development)
	@echo "$(YELLOW)Running migrations...$(NC)"
	$(MANAGE) migrate $(SETTINGS_DEV)
	@echo "$(GREEN)✓ Migrations complete$(NC)"

makemigrations: ## Create new migrations (development)
	@echo "$(YELLOW)Creating migrations...$(NC)"
	$(MANAGE) makemigrations $(SETTINGS_DEV)

shell: ## Open Django shell (development)
	$(MANAGE) shell $(SETTINGS_DEV)

shell-plus: ## Open Django shell with extensions (development)
	$(MANAGE) shell_plus $(SETTINGS_DEV)

createsuperuser: ## Create a superuser (development)
	$(MANAGE) createsuperuser $(SETTINGS_DEV)

collectstatic: ## Collect static files (development)
	@echo "$(YELLOW)Collecting static files...$(NC)"
	$(MANAGE) collectstatic --noinput $(SETTINGS_DEV)
	@echo "$(GREEN)✓ Static files collected$(NC)"

check: ## Run Django system checks
	@echo "$(YELLOW)Running system checks...$(NC)"
	$(MANAGE) check $(SETTINGS_DEV)
	@echo "$(GREEN)✓ System checks passed$(NC)"

check-deploy: ## Run deployment checks (production)
	@echo "$(YELLOW)Running deployment checks...$(NC)"
	$(MANAGE) check --deploy $(SETTINGS_PROD)

# Testing targets
test: ## Run all tests
	@echo "$(YELLOW)Running tests...$(NC)"
	pytest

test-fast: ## Run tests without coverage
	@echo "$(YELLOW)Running fast tests...$(NC)"
	pytest --no-cov

test-unit: ## Run unit tests only
	@echo "$(YELLOW)Running unit tests...$(NC)"
	pytest -m unit

test-integration: ## Run integration tests only
	@echo "$(YELLOW)Running integration tests...$(NC)"
	pytest -m integration

test-watch: ## Run tests in watch mode
	@echo "$(YELLOW)Running tests in watch mode...$(NC)"
	pytest-watch

coverage: ## Generate coverage report
	@echo "$(YELLOW)Generating coverage report...$(NC)"
	pytest --cov --cov-report=html --cov-report=term
	@echo "$(GREEN)✓ Coverage report generated in htmlcov/$(NC)"

coverage-open: coverage ## Generate and open coverage report
	@echo "$(BLUE)Opening coverage report...$(NC)"
	@if command -v xdg-open > /dev/null; then \
		xdg-open htmlcov/index.html; \
	elif command -v open > /dev/null; then \
		open htmlcov/index.html; \
	else \
		echo "$(YELLOW)Please open htmlcov/index.html manually$(NC)"; \
	fi

# Code quality targets
lint: ## Run all linters
	@echo "$(YELLOW)Running linters...$(NC)"
	@echo "$(BLUE)→ Flake8$(NC)"
	flake8 .
	@echo "$(BLUE)→ Pylint$(NC)"
	pylint voyah home search || true
	@echo "$(GREEN)✓ Linting complete$(NC)"

lint-flake8: ## Run flake8 only
	@echo "$(YELLOW)Running flake8...$(NC)"
	flake8 .

lint-pylint: ## Run pylint only
	@echo "$(YELLOW)Running pylint...$(NC)"
	pylint voyah home search

lint-ruff: ## Run ruff linter
	@echo "$(YELLOW)Running ruff...$(NC)"
	ruff check .

format: ## Format code with black and isort
	@echo "$(YELLOW)Formatting code...$(NC)"
	@echo "$(BLUE)→ Black$(NC)"
	black .
	@echo "$(BLUE)→ isort$(NC)"
	isort .
	@echo "$(GREEN)✓ Code formatted$(NC)"

format-check: ## Check code formatting without changes
	@echo "$(YELLOW)Checking code formatting...$(NC)"
	black --check .
	isort --check-only .

type-check: ## Run type checking with mypy
	@echo "$(YELLOW)Running type checks...$(NC)"
	mypy .

security: ## Run security checks with bandit
	@echo "$(YELLOW)Running security checks...$(NC)"
	bandit -r . -c pyproject.toml

secrets: ## Scan for secrets
	@echo "$(YELLOW)Scanning for secrets...$(NC)"
	detect-secrets scan --baseline .secrets.baseline

# Pre-commit targets
pre-commit: ## Run pre-commit on all files
	@echo "$(YELLOW)Running pre-commit hooks...$(NC)"
	pre-commit run --all-files

pre-commit-update: ## Update pre-commit hooks
	@echo "$(YELLOW)Updating pre-commit hooks...$(NC)"
	pre-commit autoupdate

# Quality check (run all checks)
quality: format lint type-check security test ## Run all quality checks

# Clean targets
clean: ## Remove generated files
	@echo "$(YELLOW)Cleaning up...$(NC)"
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	rm -rf htmlcov/
	rm -rf dist/
	rm -rf build/
	@echo "$(GREEN)✓ Cleanup complete$(NC)"

clean-db: ## Remove SQLite database
	@echo "$(RED)Removing database...$(NC)"
	rm -f db.sqlite3
	@echo "$(GREEN)✓ Database removed$(NC)"

# Build targets
build: clean ## Build distribution packages
	@echo "$(YELLOW)Building distribution packages...$(NC)"
	$(PYTHON) -m build
	@echo "$(GREEN)✓ Build complete$(NC)"

# Docker targets (if using Docker)
docker-build: ## Build Docker image
	@echo "$(YELLOW)Building Docker image...$(NC)"
	docker build -t voyah .

docker-run: ## Run Docker container
	@echo "$(BLUE)Running Docker container...$(NC)"
	docker run -p 8000:8000 voyah

# Database targets
db-reset: clean-db migrate ## Reset database (WARNING: deletes all data)
	@echo "$(GREEN)✓ Database reset complete$(NC)"

db-backup: ## Backup SQLite database
	@echo "$(YELLOW)Backing up database...$(NC)"
	cp db.sqlite3 db.sqlite3.backup.$(shell date +%Y%m%d_%H%M%S)
	@echo "$(GREEN)✓ Database backed up$(NC)"

# Documentation targets
docs: ## Generate documentation
	@echo "$(YELLOW)Generating documentation...$(NC)"
	cd docs && make html
	@echo "$(GREEN)✓ Documentation generated$(NC)"

# Info targets
info: ## Show project information
	@echo "$(BLUE)Project Information:$(NC)"
	@echo "  Python version: $(shell $(PYTHON) --version)"
	@echo "  Django version: $(shell $(PYTHON) -c 'import django; print(django.get_version())')"
	@echo "  Wagtail version: $(shell $(PYTHON) -c 'import wagtail; print(wagtail.__version__)')"
	@echo "  Virtual env: $(VIRTUAL_ENV)"

requirements: ## Show installed packages
	@echo "$(BLUE)Installed packages:$(NC)"
	$(PIP) list

# All-in-one targets
dev: install-dev setup setup-hooks ## Complete development setup
	@echo "$(GREEN)✓ Development environment fully configured!$(NC)"
	@echo "$(BLUE)Run 'make run' to start the server$(NC)"

ci: format-check lint test ## Run CI checks (format, lint, test)
	@echo "$(GREEN)✓ All CI checks passed!$(NC)"

