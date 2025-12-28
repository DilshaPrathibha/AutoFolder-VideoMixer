@echo off
REM ============================================
REM AutoFolder VideoMixer - Build Script
REM Quick rebuild after making code changes
REM ============================================

setlocal enabledelayedexpansion

echo.
echo ========================================
echo   AutoFolder VideoMixer Build Script
echo ========================================
echo.

REM Get version from Python file
for /f "tokens=2 delims==" %%a in ('findstr "__version__" "ffmpeg-8.0.1-full_build\bin\AutoFolder.py"') do (
    set VERSION_LINE=%%a
)
set VERSION=%VERSION_LINE:"=%
set VERSION=%VERSION: =%

echo Current Version: %VERSION%
echo.

REM Ask user what to do
echo What would you like to do?
echo.
echo [1] Quick Rebuild (rebuild exe only)
echo [2] Full Rebuild (clean + rebuild)
echo [3] Build + Create Release ZIP
echo [4] Exit
echo.
choice /c 1234 /n /m "Enter your choice (1-4): "

if errorlevel 4 goto :EOF
if errorlevel 3 goto full_release
if errorlevel 2 goto full_build
if errorlevel 1 goto quick_build

:quick_build
echo.
echo [1/1] Building executable...
".venv\Scripts\python.exe" -m PyInstaller AutoFolder-VideoMixer.spec
if errorlevel 1 (
    echo.
    echo ERROR: Build failed!
    pause
    exit /b 1
)
echo.
echo ✓ Build complete!
echo ✓ Executable: dist\AutoFolder-VideoMixer.exe
goto end

:full_build
echo.
echo [1/1] Clean building executable...
".venv\Scripts\python.exe" -m PyInstaller --clean AutoFolder-VideoMixer.spec
if errorlevel 1 (
    echo.
    echo ERROR: Build failed!
    pause
    exit /b 1
)
echo.
echo ✓ Clean build complete!
echo ✓ Executable: dist\AutoFolder-VideoMixer.exe
goto end

:full_release
echo.
echo [1/3] Clean building executable...
".venv\Scripts\python.exe" -m PyInstaller --clean AutoFolder-VideoMixer.spec
if errorlevel 1 (
    echo.
    echo ERROR: Build failed!
    pause
    exit /b 1
)

echo [2/3] Creating release folder...
if exist "AutoFolder-VideoMixer-v%VERSION%" rmdir /s /q "AutoFolder-VideoMixer-v%VERSION%"
mkdir "AutoFolder-VideoMixer-v%VERSION%"
copy "dist\AutoFolder-VideoMixer.exe" "AutoFolder-VideoMixer-v%VERSION%\" >nul
copy "README.md" "AutoFolder-VideoMixer-v%VERSION%\README.txt" >nul

REM Create Quick Start guide
echo Creating QUICK_START.txt...
(
echo ================================================================================
echo                     AUTOFOLDER VIDEOMIXER v%VERSION%
echo                          Quick Start Guide
echo ================================================================================
echo.
echo QUICK START: Double-click AutoFolder-VideoMixer.exe to launch
echo.
echo 1. Select input folder with your images/videos
echo 2. Select output folder for the result
echo 3. Configure settings and click Generate
echo.
echo For detailed instructions, see README.txt
echo ================================================================================
) > "AutoFolder-VideoMixer-v%VERSION%\QUICK_START.txt"

echo [3/3] Creating ZIP package...
powershell -Command "Compress-Archive -Path 'AutoFolder-VideoMixer-v%VERSION%' -DestinationPath 'AutoFolder-VideoMixer-v%VERSION%-Windows.zip' -Force"

echo.
echo ========================================
echo   ✓ RELEASE PACKAGE COMPLETE!
echo ========================================
echo.
echo Version: %VERSION%
echo Package: AutoFolder-VideoMixer-v%VERSION%-Windows.zip
echo.
dir "AutoFolder-VideoMixer-v%VERSION%-Windows.zip" | findstr "AutoFolder"
goto end

:end
echo.
echo ========================================
echo.
echo Want to test the executable?
choice /c YN /n /m "Launch AutoFolder-VideoMixer.exe now? (Y/N): "
if errorlevel 2 goto :done
start "" "dist\AutoFolder-VideoMixer.exe"

:done
echo.
echo Done!
pause
