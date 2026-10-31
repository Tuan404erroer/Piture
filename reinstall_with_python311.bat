@echo off
echo ========================================
echo Reinstall with Python 3.11
echo ========================================
echo.

echo Checking Python 3.11...
py -3.11 --version
if errorlevel 1 (
    echo ERROR: Python 3.11 not found!
    echo Please install Python 3.11 from python.org
    pause
    exit /b 1
)

echo.
echo Removing old venv...
if exist venv (
    rmdir /s /q venv
    echo Old venv removed.
)

echo.
echo Creating new venv with Python 3.11...
py -3.11 -m venv venv

echo.
echo Activating venv...
call venv\Scripts\activate

echo.
echo Upgrading pip...
python -m pip install --upgrade pip

echo.
echo ========================================
echo Installing PyTorch with CUDA 11.8
echo (for RTX 2050)
echo ========================================
echo.

pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118

if errorlevel 1 (
    echo.
    echo CUDA version failed. Trying CPU version...
    pip install torch torchvision
)

echo.
echo ========================================
echo Installing other packages...
echo ========================================
echo.

pip install streamlit
pip install diffusers
pip install transformers
pip install accelerate
pip install safetensors
pip install Pillow
pip install numpy
pip install scipy

echo.
echo ========================================
echo Running system check...
echo ========================================
echo.

python check_system.py

echo.
echo ========================================
echo Installation completed!
echo ========================================
echo.
echo Now you can run: run.bat
echo.
pause
