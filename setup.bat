@echo off

:: Check if Python 3.9 is installed
where python3.9 >nul 2>nul
if %errorlevel% neq 0 (
    echo Python 3.9 is not installed. Please install it.
    exit /b 1
)

:: Create a virtual environment
python3.9 -m venv venv

:: Activate the virtual environment
call venv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt

echo Setup complete. Activate the virtual environment using 'venv\Scripts\activate'.
