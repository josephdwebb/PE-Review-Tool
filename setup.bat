@echo off
echo ========================================
echo PE Reviewer Setup Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python 3.8 or higher from python.org
    echo.
    pause
    exit /b 1
)

echo Python found:
python --version
echo.

REM Create virtual environment
echo Creating virtual environment...
if exist venv (
    echo Virtual environment already exists. Skipping creation.
) else (
    python -m venv venv
    echo Virtual environment created successfully!
)
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Install requirements
echo Installing required packages...
python -m pip install --upgrade pip
pip install -r requirements.txt
echo.

echo ========================================
echo Setup complete!
echo ========================================
echo.
echo To run the PE Reviewer:
echo   1. Double-click 'run.bat', OR
echo   2. Run these commands:
echo      venv\Scripts\activate.bat
echo      python reviewcode.py
echo.
echo Before running, make sure to:
echo   - Edit config.ini with your CSV file name
echo   - Place your CSV file in this folder
echo.
pause
