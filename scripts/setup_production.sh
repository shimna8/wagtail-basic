#!/bin/bash
# Production Environment Setup Script

echo "Setting up Production Environment..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install production requirements
echo "Installing production requirements..."
pip install --upgrade pip
pip install -r requirements/production.txt

# Check for .env file
if [ ! -f ".env" ]; then
    echo "❌ ERROR: .env file not found!"
    echo "Please create .env file with your production credentials."
    echo "You can use .env.production.example as a template:"
    echo "  cp .env.production.example .env"
    echo "  nano .env  # Edit with your credentials"
    exit 1
fi

# Create logs directory
echo "Creating logs directory..."
mkdir -p logs

# Set Django settings module
export DJANGO_SETTINGS_MODULE=voyah.settings.production

# Run Django deployment checks
echo "Running Django deployment checks..."
python manage.py check --deploy

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo ""
echo "✅ Production environment setup complete!"
echo ""
echo "⚠️  SECURITY CHECKLIST:"
echo "  - Ensure SECRET_KEY is set to a random string"
echo "  - Verify DEBUG=False in .env"
echo "  - Check ALLOWED_HOSTS is configured correctly"
echo "  - Ensure database credentials are secure"
echo "  - Configure HTTPS and SSL settings"
echo "  - Set up Sentry for error tracking"
echo "  - Configure regular database backups"
echo ""
echo "To start the production server with Gunicorn, run:"
echo "  source venv/bin/activate"
echo "  gunicorn voyah.wsgi:application \\"
echo "    --env DJANGO_SETTINGS_MODULE=voyah.settings.production \\"
echo "    --bind 0.0.0.0:8000 \\"
echo "    --workers 4 \\"
echo "    --timeout 60 \\"
echo "    --access-logfile logs/access.log \\"
echo "    --error-logfile logs/error.log"

