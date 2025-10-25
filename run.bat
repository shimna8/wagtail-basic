@echo off
REM Wagtail Project Quick Start Script for Windows

echo.
echo ========================================
echo   Wagtail Project - Quick Start
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install/update dependencies
echo Installing dependencies...
pip install -q -r requirements.txt

REM Set development settings
set DJANGO_SETTINGS_MODULE=mywagtailproject.settings.development

REM Run migrations
echo Running migrations...
python manage.py migrate --noinput

REM Collect static files
echo Collecting static files...
python manage.py collectstatic --noinput -q

echo.
echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo Starting development server...
echo Access the site at: http://127.0.0.1:8000/
echo Access admin at: http://127.0.0.1:8000/admin/
echo.

REM Start development server
python manage.py runserver

