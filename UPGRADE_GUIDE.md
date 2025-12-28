# 🔄 Upgrade & Maintenance Guide

## Quick Answer: YES! It's Easy to Apply Changes

Whenever you modify the Python code, just rebuild the executable. It takes ~30-60 seconds.

---

## 🚀 Super Easy Method: Use the Build Script

Simply run:
```powershell
.\build.bat
```

**Choose an option:**
1. **Quick Rebuild** - Just rebuild (fast, 30 sec)
2. **Full Rebuild** - Clean build (slower, more thorough)
3. **Build + Release** - Creates new ZIP package automatically

That's it! Your changes are now in the .exe

---

## 📝 Detailed Upgrade Workflow

### Step 1: Edit Your Python Code
```powershell
# Open and edit the source file
notepad "ffmpeg-8.0.1-full_build\bin\AutoFolder.py"

# Or use VS Code
code "ffmpeg-8.0.1-full_build\bin\AutoFolder.py"
```

### Step 2: Update Version Number (Recommended)
```python
# In AutoFolder.py, change:
__version__ = "1.0.0"  # Old version
# To:
__version__ = "1.0.1"  # New version
```

**Version numbering:**
- `1.0.1` - Bug fix
- `1.1.0` - New feature
- `2.0.0` - Major change

### Step 3: Rebuild the Executable

**Option A: Use Build Script (Easiest)**
```powershell
.\build.bat
# Choose option 3 for full release package
```

**Option B: Manual Command**
```powershell
# Quick rebuild
& ".venv\Scripts\python.exe" -m PyInstaller AutoFolder-VideoMixer.spec

# OR clean rebuild (recommended after major changes)
& ".venv\Scripts\python.exe" -m PyInstaller --clean AutoFolder-VideoMixer.spec
```

### Step 4: Test
```powershell
.\dist\AutoFolder-VideoMixer.exe
```

### Step 5: Create New Release
```powershell
# Build script does this automatically, or manually:
.\build.bat
# Select option 3
```

---

## ⚡ Quick Reference

### Common Scenarios

#### 🐛 Fixed a Bug
```powershell
# 1. Fix the bug in AutoFolder.py
# 2. Change version: "1.0.0" → "1.0.1"
# 3. Run build script:
.\build.bat
# 4. Choose option 3 (Build + Release)
# 5. Upload new ZIP to GitHub
```

#### ✨ Added New Feature
```powershell
# 1. Add feature to AutoFolder.py
# 2. Change version: "1.0.1" → "1.1.0"
# 3. Update CHANGELOG.md
# 4. Run:
.\build.bat
# 5. Choose option 3
# 6. Update README.md if needed
# 7. Create GitHub release
```

#### 🔧 Changed Settings/Config
```powershell
# For minor tweaks, no version change needed
.\build.bat
# Choose option 1 (Quick Rebuild)
```

---

## 🎯 Full Upgrade Checklist

### Before Making Changes
- [ ] Test current version works
- [ ] Plan what you want to change
- [ ] Backup current working version

### Making Changes
- [ ] Edit `ffmpeg-8.0.1-full_build\bin\AutoFolder.py`
- [ ] Update `__version__` if releasing
- [ ] Test changes (run Python script directly first)

### Building New Version
- [ ] Run `.\build.bat` (option 3)
- [ ] Test the new .exe thoroughly
- [ ] Verify FFmpeg still works
- [ ] Test on clean Windows machine if possible

### Documentation
- [ ] Update `CHANGELOG.md` with changes
- [ ] Update `README.md` if features changed
- [ ] Update version in `installer.iss` if using

### Distribution
- [ ] Create GitHub release
- [ ] Tag with version (e.g., `v1.0.1`)
- [ ] Upload new ZIP file
- [ ] Write release notes

---

## 🧪 Testing Before Release

### Quick Test
```powershell
# Run the new executable
.\dist\AutoFolder-VideoMixer.exe

# Test basic functionality:
# 1. Launch app
# 2. Select folders
# 3. Generate a short test video
# 4. Verify output works
```

### Thorough Test
- [ ] Test with images only
- [ ] Test with videos only
- [ ] Test with mixed media
- [ ] Test all sort options
- [ ] Test auto-watch mode
- [ ] Test delete function
- [ ] Test on different Windows versions
- [ ] Test with large files
- [ ] Test with many files

---

## 🔧 Advanced: Editing During Development

### Run Python Script Directly (No Build Needed)
```powershell
# For quick testing during development
& ".venv\Scripts\python.exe" "ffmpeg-8.0.1-full_build\bin\AutoFolder.py"

# Make changes, run again immediately
# Only build .exe when ready to distribute
```

### Using Git for Version Control
```powershell
# Commit your changes
git add "ffmpeg-8.0.1-full_build\bin\AutoFolder.py"
git commit -m "Fixed bug in video duration calculation"
git tag v1.0.1
git push
git push --tags
```

---

## 📦 What Gets Rebuilt

When you run PyInstaller, it:
1. ✅ Reads your updated Python code
2. ✅ Bundles FFmpeg again
3. ✅ Includes all dependencies
4. ✅ Creates new .exe with ALL changes
5. ✅ Takes ~30-60 seconds

**Everything in the Python file goes into the .exe automatically!**

---

## 💡 Pro Tips

### 1. Keep Build Fast
- Use **Quick Rebuild** (option 1) for minor changes
- Only use **Full Rebuild** (option 2) when:
  - Changing dependencies
  - After errors
  - Major code restructuring

### 2. Version Management
```python
# Add version to output filename in AutoFolder.py:
out_video = os.path.join(output_folder, f"combined_v{__version__}_{ts}.mp4")
```

### 3. Auto-Update Checker (Future Enhancement)
```python
# Add to AutoFolder.py for auto-update notifications
def check_for_updates():
    # Check GitHub for newer version
    # Notify user if available
    pass
```

### 4. Keep Development Environment Ready
```powershell
# Always use the virtual environment
& ".venv\Scripts\python.exe" -m pip list  # Check installed packages
& ".venv\Scripts\python.exe" -m pip install --upgrade pyinstaller  # Update PyInstaller
```

---

## 🐞 Troubleshooting Build Issues

### Build Fails
```powershell
# Try clean build
rmdir /s /q build dist
.\build.bat
# Choose option 2
```

### Import Errors in Built .exe
```python
# Add to .spec file hiddenimports:
hiddenimports=['missing_module_name'],
```

### FFmpeg Not Found After Build
```python
# Check find_ffmpeg() function in AutoFolder.py
# Verify FFmpeg paths in .spec file
```

---

## 📊 Build Time Comparison

| Build Type | Time | When to Use |
|------------|------|-------------|
| Quick Rebuild | ~30 sec | Minor code changes |
| Full Rebuild | ~60 sec | After errors, major changes |
| Full Release | ~90 sec | Creating distribution package |

---

## 🎬 Quick Command Reference

```powershell
# Build everything (recommended)
.\build.bat

# Just rebuild exe (manual)
& ".venv\Scripts\python.exe" -m PyInstaller AutoFolder-VideoMixer.spec

# Test without building
& ".venv\Scripts\python.exe" "ffmpeg-8.0.1-full_build\bin\AutoFolder.py"

# Run the built exe
.\dist\AutoFolder-VideoMixer.exe

# Package for release (manual)
.\build.bat  # Choose option 3
```

---

## 🎯 Summary

**YES! It's incredibly easy:**

1. Edit `AutoFolder.py` 
2. Run `.\build.bat`
3. Choose option 3
4. Done! New .exe ready in ~60 seconds

**The .exe is automatically rebuilt with ALL your changes!**

No complicated configuration, no manual file copying, no complex build system. Just edit code → run build script → new executable ready!

---

**Next Steps:**
- Make your first change to test the workflow
- Try the build.bat script
- See how fast it rebuilds!
