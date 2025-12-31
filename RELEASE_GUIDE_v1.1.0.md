# Release Guide for AutoFolder VideoMixer v1.1.0

## 📦 Pre-Release Checklist

✅ Version updated to 1.1.0 in:
- [x] `src/AutoFolder.py` (__version__ = "1.1.0")
- [x] `README.md` (download links and version footer)
- [x] `CHANGELOG.md` (new v1.1.0 section added)

✅ Executable built successfully:
- [x] `dist/AutoFolder-VideoMixer.exe` with v1.1.0

✅ Documentation updated:
- [x] README features list updated
- [x] CHANGELOG with all v1.1.0 changes

---

## 📋 Steps to Create GitHub Release

### Step 1: Prepare Release Package

1. **Create release folder:**
   ```powershell
   New-Item -ItemType Directory -Path "AutoFolder-VideoMixer-v1.1.0" -Force
   ```

2. **Copy files to release folder:**
   ```powershell
   Copy-Item "dist\AutoFolder-VideoMixer.exe" "AutoFolder-VideoMixer-v1.1.0\"
   Copy-Item "README.md" "AutoFolder-VideoMixer-v1.1.0\README.txt"
   Copy-Item "CHANGELOG.md" "AutoFolder-VideoMixer-v1.1.0\CHANGELOG.txt"
   ```

3. **Create quick start guide:**
   Create `AutoFolder-VideoMixer-v1.1.0\QUICK_START.txt` with:
   ```
   🎬 AutoFolder VideoMixer v1.1.0 - Quick Start
   
   1. Double-click AutoFolder-VideoMixer.exe
   2. Click "Browse" to select input folder (with videos/images)
   3. Click "Browse" to select output folder
   4. Choose video length mode:
      - Natural: Combine all media once
      - Custom: Set specific duration in minutes
   5. Click "Generate"
   6. Done! Your video is in the output folder
   
   NEW in v1.1.0:
   - Custom application icon
   - Smart video length mode dropdown
   - Auto-monitoring status indicator
   - Click to calculate estimated duration
   - Improved file deletion confirmation
   ```

4. **Create ZIP archive:**
   ```powershell
   Compress-Archive -Path "AutoFolder-VideoMixer-v1.1.0\*" -DestinationPath "AutoFolder-VideoMixer-v1.1.0-Windows.zip" -Force
   ```

---

### Step 2: Commit and Push Changes to GitHub

1. **Stage all changes:**
   ```bash
   git add .
   ```

2. **Commit with version message:**
   ```bash
   git commit -m "Release v1.1.0 - UI improvements, custom icon, smart video length mode"
   ```

3. **Create version tag:**
   ```bash
   git tag -a v1.1.0 -m "Version 1.1.0 - UI/UX improvements"
   ```

4. **Push to GitHub:**
   ```bash
   git push origin main
   git push origin v1.1.0
   ```

---

### Step 3: Create GitHub Release

1. **Go to GitHub Releases page:**
   - Navigate to: https://github.com/DilshaPrathibha/AutoFolder-VideoMixer/releases
   - Click "Draft a new release"

2. **Fill in release details:**
   - **Tag version:** Select `v1.1.0` from dropdown (or create new tag)
   - **Release title:** `AutoFolder VideoMixer v1.1.0 - UI/UX Improvements`
   
3. **Add release description:**
   ```markdown
   # 🎨 AutoFolder VideoMixer v1.1.0

   Major UI/UX improvements with custom icon, smart video length mode, and enhanced user experience!

   ## 🆕 What's New in v1.1.0

   ### UI/UX Enhancements
   - **🎨 Custom Application Icon**: Professional folder with magic wand icon
   - **🔄 Smart Video Length Mode**: Dropdown selector for Natural/Custom modes
   - **📊 Auto-Monitoring Indicator**: Shows real-time status when watching for file changes
   - **📏 On-Demand Calculation**: Click to calculate estimated video length
   - **✅ Improved Deletion Confirmation**: "Don't ask again" option with better UX
   - **🎯 Better Auto-Combine**: Only starts after first Generate click

   ### Bug Fixes
   - Fixed file deletion path normalization issues
   - Fixed overlapping progress and status labels
   - Improved icon bundling in executable

   ## 📥 Download

   **[⬇️ AutoFolder-VideoMixer-v1.1.0-Windows.zip](download link)**

   ### Installation
   1. Download the ZIP file above
   2. Extract to any folder
   3. Run `AutoFolder-VideoMixer.exe`
   4. No installation needed!

   ### Requirements
   - Windows 10/11 (64-bit)
   - No additional software needed (FFmpeg bundled)

   ## 📖 Full Changelog

   See [CHANGELOG.md](https://github.com/DilshaPrathibha/AutoFolder-VideoMixer/blob/main/CHANGELOG.md) for complete version history.

   ## 🐛 Known Issues

   None reported for v1.1.0

   ## 💬 Feedback

   Found a bug? Have a suggestion? Please [open an issue](https://github.com/DilshaPrathibha/AutoFolder-VideoMixer/issues)!

   ---

   **Previous Release**: [v1.0.0](https://github.com/DilshaPrathibha/AutoFolder-VideoMixer/releases/tag/v1.0.0)
   ```

4. **Upload release assets:**
   - Click "Attach binaries by dropping them here or selecting them"
   - Upload: `AutoFolder-VideoMixer-v1.1.0-Windows.zip`

5. **Publish release:**
   - Check "Set as the latest release"
   - Click "Publish release"

---

### Step 4: Verify Release

1. ✅ Check that v1.1.0 appears at: https://github.com/DilshaPrathibha/AutoFolder-VideoMixer/releases/latest
2. ✅ Download the ZIP and test the executable
3. ✅ Verify the download link works
4. ✅ Check that README badges update automatically

---

## 🎯 Quick Commands Summary

```powershell
# 1. Create release package
New-Item -ItemType Directory -Path "AutoFolder-VideoMixer-v1.1.0" -Force
Copy-Item "dist\AutoFolder-VideoMixer.exe" "AutoFolder-VideoMixer-v1.1.0\"
Copy-Item "README.md" "AutoFolder-VideoMixer-v1.1.0\README.txt"
Copy-Item "CHANGELOG.md" "AutoFolder-VideoMixer-v1.1.0\CHANGELOG.txt"
# Add QUICK_START.txt manually
Compress-Archive -Path "AutoFolder-VideoMixer-v1.1.0\*" -DestinationPath "AutoFolder-VideoMixer-v1.1.0-Windows.zip" -Force

# 2. Commit and push
git add .
git commit -m "Release v1.1.0 - UI improvements, custom icon, smart video length mode"
git tag -a v1.1.0 -m "Version 1.1.0 - UI/UX improvements"
git push origin main
git push origin v1.1.0

# 3. Create release on GitHub web interface
# https://github.com/DilshaPrathibha/AutoFolder-VideoMixer/releases/new
```

---

## 📝 Notes

- The ZIP file should be around 85-90 MB (includes FFmpeg)
- Release description supports markdown formatting
- GitHub automatically creates a source code archive
- Badge in README will auto-update to show v1.1.0

---

**Happy Releasing! 🚀**
