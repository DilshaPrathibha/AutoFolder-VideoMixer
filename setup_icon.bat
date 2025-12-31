@echo off
echo ================================================
echo AutoFolder-VideoMixer Icon Setup
echo ================================================
echo.

if not exist "app_icon.png" (
    echo ERROR: app_icon.png not found!
    echo.
    echo Please save the attached image as 'app_icon.png' in this directory first.
    echo.
    pause
    exit /b 1
)

echo Step 1: Converting PNG to ICO...
".venv\Scripts\python.exe" create_icon.py

if not exist "icon.ico" (
    echo ERROR: Icon conversion failed!
    pause
    exit /b 1
)

echo.
echo Step 2: Building application with icon...
".venv\Scripts\python.exe" -m PyInstaller AutoFolder-VideoMixer.spec --clean

echo.
echo ================================================
echo Build complete!
echo The executable with the new icon is in: dist\AutoFolder-VideoMixer.exe
echo ================================================
pause
