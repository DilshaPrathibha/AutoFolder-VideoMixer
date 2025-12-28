@echo off
REM Quick launcher for AutoFolder VideoMixer
REM This script launches the built executable

echo.
echo ========================================
echo   AutoFolder VideoMixer v1.0.0
echo ========================================
echo.

if exist "dist\AutoFolder-VideoMixer.exe" (
    echo Launching AutoFolder VideoMixer...
    echo.
    start "" "dist\AutoFolder-VideoMixer.exe"
    echo.
    echo Application launched successfully!
    echo You can close this window.
    echo.
) else (
    echo ERROR: AutoFolder-VideoMixer.exe not found in dist folder!
    echo.
    echo Please build the application first:
    echo   python -m PyInstaller AutoFolder-VideoMixer.spec
    echo.
    pause
)
