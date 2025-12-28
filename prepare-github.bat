@echo off
REM ============================================
REM Prepare Repository for GitHub Upload
REM ============================================

echo.
echo ========================================
echo   Preparing for GitHub Upload
echo ========================================
echo.

REM Step 1: Create src folder
echo [1/5] Creating src folder...
if not exist "src" mkdir src

REM Step 2: Copy source code
echo [2/5] Copying source code...
copy "ffmpeg-8.0.1-full_build\bin\AutoFolder.py" "src\AutoFolder.py" >nul
if errorlevel 1 (
    echo ERROR: Could not copy AutoFolder.py
    pause
    exit /b 1
)

REM Step 3: Create scripts folder
echo [3/5] Organizing scripts...
if not exist "scripts" mkdir scripts
move build.bat scripts\ >nul 2>&1
move build.ps1 scripts\ >nul 2>&1
move run.bat scripts\ >nul 2>&1

REM Step 4: Clean up
echo [4/5] Cleaning build artifacts...
if exist "build" rmdir /s /q "build" >nul 2>&1
if exist "dist" rmdir /s /q "dist" >nul 2>&1
if exist "AutoFolder-VideoMixer-v*" rmdir /s /q "AutoFolder-VideoMixer-v*" >nul 2>&1
del *.zip >nul 2>&1
del BUILD_SUCCESS.md >nul 2>&1

REM Step 5: Update spec file
echo [5/5] Updating build configuration...
powershell -Command "(Get-Content 'AutoFolder-VideoMixer.spec') -replace 'ffmpeg-8.0.1-full_build/bin/AutoFolder.py', 'src/AutoFolder.py' | Set-Content 'AutoFolder-VideoMixer.spec'"

echo.
echo ========================================
echo   ✓ Repository Ready for GitHub!
echo ========================================
echo.
echo Next steps:
echo   1. Review files with: git status
echo   2. Commit: git add . ^&^& git commit -m "Initial commit"
echo   3. Add remote: git remote add origin YOUR_REPO_URL
echo   4. Push: git push -u origin main
echo.
echo See GITHUB_SETUP.md for detailed instructions
echo.
pause
