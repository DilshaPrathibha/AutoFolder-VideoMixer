# 🔨 Development Workflow Cheat Sheet

## ⚡ Super Quick Reference

### Make a change and rebuild:
```powershell
# Edit code
code ffmpeg-8.0.1-full_build\bin\AutoFolder.py

# Rebuild (30 seconds)
.\build.bat
# Choose option 1

# Test
.\dist\AutoFolder-VideoMixer.exe
```

### Create new release:
```powershell
# Update version in AutoFolder.py
# Then run:
.\build.bat
# Choose option 3
```

---

## 🎯 Common Tasks

### 1. **Change Default Settings**
```python
# Edit: ffmpeg-8.0.1-full_build\bin\AutoFolder.py

# Example: Change default resolution
TARGET_W = 1920  # Change from 1280
TARGET_H = 1080  # Change from 720

# Example: Change default FPS
TARGET_FPS = "60"  # Change from "30"

# Example: Change default image duration
DEFAULT_IMAGE_DURATION = 3.0  # Change from 1.5
```

**Rebuild:** Quick (option 1) - Takes 30 seconds

---

### 2. **Add Supported File Formats**
```python
# Edit: ffmpeg-8.0.1-full_build\bin\AutoFolder.py

VIDEO_EXTS = (".mp4", ".mov", ".avi", ".mkv", ".webm", ".m4v", ".flv", ".wmv")
IMAGE_EXTS = (".jpg", ".jpeg", ".png", ".webp", ".bmp", ".gif")
```

**Rebuild:** Quick (option 1)

---

### 3. **Change Window Title or Layout**
```python
# Edit: ffmpeg-8.0.1-full_build\bin\AutoFolder.py

# In App.__init__:
root.title(f"My Custom VideoMixer v{__version__}")
```

**Rebuild:** Quick (option 1)

---

### 4. **Add New Feature**
```python
# Edit: ffmpeg-8.0.1-full_build\bin\AutoFolder.py

# 1. Update version
__version__ = "1.1.0"  # Feature = minor version bump

# 2. Add your new feature code
def my_new_feature():
    # Your code here
    pass

# 3. Integrate into GUI or processing logic
```

**Rebuild:** Full (option 2) - Takes 60 seconds  
**Also update:** CHANGELOG.md, README.md

---

### 5. **Fix a Bug**
```python
# Edit: ffmpeg-8.0.1-full_build\bin\AutoFolder.py

# 1. Update version
__version__ = "1.0.1"  # Bug fix = patch version bump

# 2. Fix the bug

# 3. Test thoroughly
```

**Rebuild:** Full (option 2)  
**Also update:** CHANGELOG.md

---

## 🔄 Build Script Options

### Option 1: Quick Rebuild
- **When:** Minor code changes, tweaks
- **Time:** ~30 seconds
- **Command:** `.\build.bat` → choice 1
- **Use for:**
  - Text changes
  - Logic fixes
  - UI adjustments
  - Settings changes

### Option 2: Full Rebuild
- **When:** Major changes, after errors
- **Time:** ~60 seconds
- **Command:** `.\build.bat` → choice 2
- **Use for:**
  - New features
  - Bug fixes
  - After build errors
  - Major refactoring

### Option 3: Build + Release
- **When:** Creating distribution
- **Time:** ~90 seconds
- **Command:** `.\build.bat` → choice 3
- **Creates:**
  - New .exe
  - Release folder
  - ZIP package ready to upload

---

## 🧪 Testing Workflow

### During Development (No Build)
```powershell
# Test Python directly - instant feedback
& ".venv\Scripts\python.exe" ffmpeg-8.0.1-full_build\bin\AutoFolder.py

# Make changes, test again immediately
# Only build when ready to distribute
```

### Test Built Executable
```powershell
# After building
.\dist\AutoFolder-VideoMixer.exe

# Or use build script
.\build.bat
# Choose option 4 (Test Executable)
```

---

## 📝 Version Numbering Guide

```python
__version__ = "MAJOR.MINOR.PATCH"

# Examples:
"1.0.0"  # Initial release
"1.0.1"  # Bug fix
"1.1.0"  # New feature added
"2.0.0"  # Major changes, breaking changes
```

**Rules:**
- **MAJOR** (2.0.0) - Breaking changes, major rewrite
- **MINOR** (1.1.0) - New features, backwards compatible  
- **PATCH** (1.0.1) - Bug fixes only

---

## 📦 What Changes Require Rebuild?

| Change Type | Requires Rebuild | Build Type |
|-------------|------------------|------------|
| Python code | ✅ YES | Quick |
| GUI layout | ✅ YES | Quick |
| Default settings | ✅ YES | Quick |
| New features | ✅ YES | Full |
| Bug fixes | ✅ YES | Full |
| Version number | ✅ YES | Quick |
| README.md | ❌ NO | - |
| CHANGELOG.md | ❌ NO | - |
| Documentation | ❌ NO | - |

---

## 🎨 Example: Adding Dark Mode

```python
# 1. Edit AutoFolder.py
__version__ = "1.1.0"  # New feature!

# 2. Add dark mode code
class App:
    def __init__(self, root):
        # ... existing code ...
        
        # Add dark mode option
        self.dark_mode_var = tk.BooleanVar()
        ttk.Checkbutton(
            frame, 
            text="Dark Mode", 
            variable=self.dark_mode_var,
            command=self.toggle_dark_mode
        ).grid(...)
    
    def toggle_dark_mode(self):
        if self.dark_mode_var.get():
            # Apply dark theme
            self.root.config(bg='#2b2b2b')
        else:
            # Apply light theme
            self.root.config(bg='white')

# 3. Rebuild
.\build.bat  # Choose option 2 (Full)

# 4. Test
.\dist\AutoFolder-VideoMixer.exe

# 5. Update docs
# - Update CHANGELOG.md: Added dark mode
# - Update README.md: Mention dark mode feature

# 6. Create release
.\build.bat  # Choose option 3
```

---

## 🐛 Debugging Tips

### Build Fails?
```powershell
# Clean everything and rebuild
Remove-Item -Recurse -Force build, dist
.\build.bat  # Choose option 2
```

### Test specific function?
```python
# Add at bottom of AutoFolder.py:
if __name__ == "__main__":
    # Test your function
    result = my_function()
    print(result)
```
```powershell
# Run directly
& ".venv\Scripts\python.exe" ffmpeg-8.0.1-full_build\bin\AutoFolder.py
```

### FFmpeg issues?
```python
# Add debug output
print(f"FFmpeg path: {FFMPEG_PATH}")
print(f"FFprobe path: {FFPROBE_PATH}")
```

---

## 📊 Typical Development Session

```powershell
# 1. Start coding
code ffmpeg-8.0.1-full_build\bin\AutoFolder.py

# 2. Test changes quickly (no build)
& ".venv\Scripts\python.exe" ffmpeg-8.0.1-full_build\bin\AutoFolder.py

# 3. Refine and test multiple times (still no build needed)
# ... make changes ...
# ... test again ...
# ... repeat ...

# 4. When satisfied, update version
# __version__ = "1.0.1"

# 5. Do final build
.\build.bat  # Choose option 2

# 6. Test the executable
.\dist\AutoFolder-VideoMixer.exe

# 7. If good, create release
.\build.bat  # Choose option 3

# 8. Commit to git
git add .
git commit -m "Fixed video duration bug (v1.0.1)"
git tag v1.0.1
git push --tags
```

---

## 🚀 PowerShell Build Script Commands

```powershell
# Interactive menu (recommended)
.\build.ps1

# Direct commands
.\build.ps1 -Action quick      # Quick rebuild
.\build.ps1 -Action clean      # Clean rebuild
.\build.ps1 -Action release    # Build + package
.\build.ps1 -Action test       # Test exe
```

---

## 💡 Pro Tips

1. **Always test Python directly first** - faster iteration
2. **Only build when distributing** - save time
3. **Use Quick Rebuild for small changes** - 2x faster
4. **Tag versions in git** - easy to track releases
5. **Keep CHANGELOG updated** - users appreciate it
6. **Test on clean machine** - catch missing dependencies

---

## 📚 File Locations Quick Reference

```
Your project structure:
├── ffmpeg-8.0.1-full_build/bin/
│   └── AutoFolder.py           ← Edit this file
├── build.bat                   ← Quick build script
├── build.ps1                   ← PowerShell build script
├── AutoFolder-VideoMixer.spec  ← Build configuration
├── dist/
│   └── AutoFolder-VideoMixer.exe  ← Built executable
└── .venv/                      ← Python environment
```

---

## 🎯 Summary

**To apply changes to the .exe file:**

1. Edit `AutoFolder.py`
2. Run `.\build.bat` (choose option 1 or 2)
3. Test `.\dist\AutoFolder-VideoMixer.exe`
4. Done! (30-60 seconds total)

**It's that simple!** Every change in the .py file automatically goes into the .exe when you rebuild.

---

**Ready to make your first change?**
1. Open `ffmpeg-8.0.1-full_build\bin\AutoFolder.py`
2. Change something small (like the window title)
3. Run `.\build.bat` and choose option 1
4. See your change in the .exe!
