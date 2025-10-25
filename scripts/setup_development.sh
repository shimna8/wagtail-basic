#!/bin/bash
# Development Environment Setup Script

echo "Setting up Development Environment..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install development requirements
echo "Installing development requirements..."
pip install --upgrade pip
pip install -r requirements/development.txt

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    cp .env.development.example .env
fi

# Run migrations
echo "Running migrations..."
export DJANGO_SETTINGS_MODULE=mywagtailproject.settings.development
python manage.py migrate

# Create superuser (optional)
echo ""
echo "Do you want to create a superuser? (y/n)"
read -r response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    python manage.py createsuperuser
fi

echo ""
echo "✅ Development environment setup complete!"
echo ""
echo "To start the development server, run:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver --settings=mywagtailproject.settings.development"
echo ""
echo "Or simply run: ./run.sh"

