#!/bin/bash

# Wagtail Project Quick Start Script

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  Wagtail Project - Quick Start${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}Virtual environment not found. Creating...${NC}"
    python3 -m venv venv
fi

# Activate virtual environment
echo -e "${YELLOW}Activating virtual environment...${NC}"
source venv/bin/activate

# Install/update dependencies
echo -e "${YELLOW}Installing dependencies...${NC}"
pip install -q -r requirements.txt

# Set development settings
export DJANGO_SETTINGS_MODULE=voyah.settings.development

# Run migrations
echo -e "${YELLOW}Running migrations...${NC}"
python manage.py migrate --noinput

# Collect static files
echo -e "${YELLOW}Collecting static files...${NC}"
python manage.py collectstatic --noinput -q

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}  Setup Complete!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo -e "${BLUE}Starting development server...${NC}"
echo -e "${BLUE}Access the site at: http://127.0.0.1:8000/${NC}"
echo -e "${BLUE}Access admin at: http://127.0.0.1:8000/admin/${NC}"
echo ""

# Start development server
python manage.py runserver

