@echo off
echo Starting PE Reviewer...
echo.

REM Check if virtual environment exists
if not exist venv (
    echo ERROR: Virtual environment not found!
    echo Please run setup.bat first.
    echo.
    pause
    exit /b 1
)

REM Activate virtual environment and run the application
call venv\Scripts\activate.bat
python reviewcode.py

REM Keep window open if there's an error
if %errorlevel% neq 0 (
    echo.
    echo Application exited with an error.
    pause
)
