@echo off
echo ========================================
echo Kurzgesagt AI Image Generator
echo ========================================
echo.

REM Activate virtual environment if exists
if exist venv\Scripts\activate.bat (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
)

REM Check if streamlit is installed
python -c "import streamlit" 2>nul
if errorlevel 1 (
    echo ERROR: Streamlit not found!
    echo Please run: pip install -r requirements.txt
    pause
    exit /b 1
)

REM Run the app
echo Starting Kurzgesagt AI Generator...
echo.
python web_app.py

pause
