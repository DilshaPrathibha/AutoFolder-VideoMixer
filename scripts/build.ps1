# AutoFolder VideoMixer - PowerShell Build Script
# Enhanced version with more features

param(
    [Parameter(Mandatory=$false)]
    [ValidateSet('quick', 'clean', 'release', 'test')]
    [string]$Action = 'menu'
)

$ErrorActionPreference = "Stop"

# Colors
function Write-Success { Write-Host $args -ForegroundColor Green }
function Write-Info { Write-Host $args -ForegroundColor Cyan }
function Write-Error { Write-Host $args -ForegroundColor Red }
function Write-Warning { Write-Host $args -ForegroundColor Yellow }

# Get version from Python file
function Get-AppVersion {
    $content = Get-Content "ffmpeg-8.0.1-full_build\bin\AutoFolder.py" -Raw
    if ($content -match '__version__\s*=\s*"([^"]+)"') {
        return $Matches[1]
    }
    return "Unknown"
}

# Display header
function Show-Header {
    Clear-Host
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "  AutoFolder VideoMixer Build Script" -ForegroundColor Cyan
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Info "Current Version: $(Get-AppVersion)"
    Write-Host ""
}

# Quick rebuild
function Invoke-QuickBuild {
    Write-Info "[Building] Quick rebuild..."
    & ".venv\Scripts\python.exe" -m PyInstaller AutoFolder-VideoMixer.spec
    
    if ($LASTEXITCODE -eq 0) {
        Write-Success "`n✓ Build complete!"
        Write-Success "✓ Executable: dist\AutoFolder-VideoMixer.exe"
        
        $exe = Get-Item "dist\AutoFolder-VideoMixer.exe"
        Write-Info "✓ Size: $([math]::Round($exe.Length/1MB, 2)) MB"
        return $true
    } else {
        Write-Error "`n✗ Build failed!"
        return $false
    }
}

# Clean rebuild
function Invoke-CleanBuild {
    Write-Info "[Building] Clean rebuild..."
    & ".venv\Scripts\python.exe" -m PyInstaller --clean AutoFolder-VideoMixer.spec
    
    if ($LASTEXITCODE -eq 0) {
        Write-Success "`n✓ Clean build complete!"
        Write-Success "✓ Executable: dist\AutoFolder-VideoMixer.exe"
        
        $exe = Get-Item "dist\AutoFolder-VideoMixer.exe"
        Write-Info "✓ Size: $([math]::Round($exe.Length/1MB, 2)) MB"
        return $true
    } else {
        Write-Error "`n✗ Build failed!"
        return $false
    }
}

# Create release package
function New-ReleasePackage {
    $version = Get-AppVersion
    $folderName = "AutoFolder-VideoMixer-v$version"
    $zipName = "$folderName-Windows.zip"
    
    Write-Info "[1/4] Building executable..."
    if (-not (Invoke-CleanBuild)) {
        return $false
    }
    
    Write-Info "`n[2/4] Creating release folder..."
    if (Test-Path $folderName) {
        Remove-Item $folderName -Recurse -Force
    }
    New-Item -ItemType Directory -Path $folderName -Force | Out-Null
    
    Write-Info "[3/4] Copying files..."
    Copy-Item "dist\AutoFolder-VideoMixer.exe" -Destination "$folderName\" -Force
    Copy-Item "README.md" -Destination "$folderName\README.txt" -Force
    
    # Create Quick Start
    $quickStart = @"
================================================================================
                    AUTOFOLDER VIDEOMIXER v$version
                         Quick Start Guide
================================================================================

🚀 QUICK START: Double-click AutoFolder-VideoMixer.exe to launch!

📋 BASIC USAGE:
   1. Select input folder with images/videos
   2. Select output folder for final video
   3. Configure settings (video length, image duration, sort order)
   4. Click "Generate" and wait
   5. Your video is saved as combined_YYYYMMDD_HHMMSS.mp4

📂 SUPPORTED FILES:
   Videos: .mp4, .mov, .avi, .mkv, .webm, .m4v
   Images: .jpg, .jpeg, .png, .webp

⚙️ OUTPUT: 1280×720 @ 30fps MP4 (H.264)

💡 TIP: Enable "Auto combine when files change" for automatic regeneration!

📖 For detailed documentation, see README.txt

================================================================================
"@
    Set-Content -Path "$folderName\QUICK_START.txt" -Value $quickStart -Force
    
    Write-Info "[4/4] Creating ZIP package..."
    if (Test-Path $zipName) {
        Remove-Item $zipName -Force
    }
    Compress-Archive -Path $folderName -DestinationPath $zipName -Force
    
    Write-Success "`n========================================"
    Write-Success "  ✓ RELEASE PACKAGE COMPLETE!"
    Write-Success "========================================"
    Write-Host ""
    Write-Info "Version:  $version"
    Write-Info "Package:  $zipName"
    
    $zip = Get-Item $zipName
    Write-Info "Size:     $([math]::Round($zip.Length/1MB, 2)) MB"
    Write-Host ""
    
    return $true
}

# Test the executable
function Test-Executable {
    Write-Info "[Testing] Launching executable..."
    
    if (-not (Test-Path "dist\AutoFolder-VideoMixer.exe")) {
        Write-Error "✗ Executable not found! Build first."
        return
    }
    
    Write-Success "✓ Launching AutoFolder-VideoMixer.exe"
    Start-Process "dist\AutoFolder-VideoMixer.exe"
    Write-Info "✓ Application started (check for window)"
}

# Main menu
function Show-Menu {
    Show-Header
    
    Write-Host "What would you like to do?"
    Write-Host ""
    Write-Host "  [1] Quick Rebuild (fast, ~30 sec)" -ForegroundColor Yellow
    Write-Host "  [2] Full Rebuild (clean, ~60 sec)" -ForegroundColor Yellow
    Write-Host "  [3] Build + Create Release ZIP" -ForegroundColor Yellow
    Write-Host "  [4] Test Executable" -ForegroundColor Yellow
    Write-Host "  [5] View Current Version" -ForegroundColor Yellow
    Write-Host "  [6] Exit" -ForegroundColor Yellow
    Write-Host ""
    
    $choice = Read-Host "Enter your choice (1-6)"
    
    switch ($choice) {
        "1" { 
            Invoke-QuickBuild
            Read-Host "`nPress Enter to continue"
            Show-Menu
        }
        "2" { 
            Invoke-CleanBuild
            Read-Host "`nPress Enter to continue"
            Show-Menu
        }
        "3" { 
            New-ReleasePackage
            Read-Host "`nPress Enter to continue"
            Show-Menu
        }
        "4" { 
            Test-Executable
            Read-Host "`nPress Enter to continue"
            Show-Menu
        }
        "5" { 
            $version = Get-AppVersion
            Write-Host ""
            Write-Success "Current Version: $version"
            Write-Host ""
            if (Test-Path "ffmpeg-8.0.1-full_build\bin\AutoFolder.py") {
                Write-Info "Source: ffmpeg-8.0.1-full_build\bin\AutoFolder.py"
            }
            if (Test-Path "dist\AutoFolder-VideoMixer.exe") {
                $exe = Get-Item "dist\AutoFolder-VideoMixer.exe"
                Write-Info "Executable: $([math]::Round($exe.Length/1MB, 2)) MB"
                Write-Info "Modified: $($exe.LastWriteTime)"
            }
            Read-Host "`nPress Enter to continue"
            Show-Menu
        }
        "6" { 
            Write-Info "`nGoodbye!"
            exit 0
        }
        default { 
            Write-Warning "`nInvalid choice. Please try again."
            Start-Sleep -Seconds 1
            Show-Menu
        }
    }
}

# Main execution
try {
    switch ($Action) {
        'quick' {
            Show-Header
            Invoke-QuickBuild
        }
        'clean' {
            Show-Header
            Invoke-CleanBuild
        }
        'release' {
            Show-Header
            New-ReleasePackage
        }
        'test' {
            Show-Header
            Test-Executable
        }
        'menu' {
            Show-Menu
        }
    }
} catch {
    Write-Error "`n✗ Error: $_"
    Read-Host "`nPress Enter to exit"
    exit 1
}
