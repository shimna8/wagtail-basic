#!/bin/bash
# Staging Environment Setup Script

echo "Setting up Staging Environment..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install staging requirements
echo "Installing staging requirements..."
pip install --upgrade pip
pip install -r requirements/stage.txt

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.stage.example .env
    echo "⚠️  Please edit .env file with your staging credentials!"
    exit 1
fi

# Create logs directory
echo "Creating logs directory..."
mkdir -p logs

# Set Django settings module
export DJANGO_SETTINGS_MODULE=mywagtailproject.settings.stage

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser (optional)
echo ""
echo "Do you want to create a superuser? (y/n)"
read -r response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    python manage.py createsuperuser
fi

echo ""
echo "✅ Staging environment setup complete!"
echo ""
echo "To start the staging server with Gunicorn, run:"
echo "  source venv/bin/activate"
echo "  gunicorn mywagtailproject.wsgi:application --env DJANGO_SETTINGS_MODULE=mywagtailproject.settings.stage --bind 0.0.0.0:8000"

