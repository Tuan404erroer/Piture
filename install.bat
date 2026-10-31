@echo off
echo ========================================
echo Kurzgesagt AI Generator - Installation
echo ========================================
echo.

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)

echo Python found!
python --version
echo.

REM Create virtual environment
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment!
        pause
        exit /b 1
    )
    echo Virtual environment created successfully!
) else (
    echo Virtual environment already exists.
)
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install PyTorch first
echo.
echo ========================================
echo Installing PyTorch...
echo ========================================
echo.
echo Detecting GPU...
nvidia-smi >nul 2>&1
if errorlevel 1 (
    echo No NVIDIA GPU detected. Installing CPU version...
    echo WARNING: CPU version will be VERY SLOW!
    pip install torch torchvision
) else (
    echo NVIDIA GPU detected! Installing CUDA version...
    echo.
    echo Choose CUDA version:
    echo 1. CUDA 11.8 (Recommended for RTX 2050)
    echo 2. CUDA 12.1 (Latest)
    echo 3. CPU only (No GPU)
    echo.
    choice /C 123 /M "Select option"
    
    if errorlevel 3 (
        echo Installing CPU version...
        pip install torch torchvision
    ) else if errorlevel 2 (
        echo Installing CUDA 12.1 version...
        pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
    ) else (
        echo Installing CUDA 11.8 version...
        pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
    )
)

if errorlevel 1 (
    echo.
    echo ERROR: PyTorch installation failed!
    echo Please check INSTALL_PYTORCH.md for manual installation
    pause
    exit /b 1
)

echo.
echo PyTorch installed successfully!

REM Install other requirements
echo.
echo Installing other dependencies...
echo This may take several minutes...
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Installation failed!
    echo Please check the error messages above
    pause
    exit /b 1
)

echo.
echo ========================================
echo Installation completed successfully!
echo ========================================
echo.
echo To run the app, execute: run.bat
echo Or manually: streamlit run app.py
echo.
pause
