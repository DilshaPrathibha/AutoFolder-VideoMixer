# 🔨 Build Instructions for AutoFolder VideoMixer

This document explains how to build AutoFolder VideoMixer as a standalone Windows executable.

## Prerequisites

1. **Python 3.8+** installed
2. **PyInstaller** installed: `pip install pyinstaller`
3. **Dependencies** installed: `pip install send2trash`
4. **FFmpeg** (optional - can be bundled or required separately)

---

## 📦 Build Options

### Option 1: Simple One-File Executable (Recommended for Quick Builds)

```powershell
# Basic build without FFmpeg bundled
pyinstaller --onefile --windowed --name "AutoFolder-VideoMixer" AutoFolder.py

# With custom icon (if you have icon.ico)
pyinstaller --onefile --windowed --name "AutoFolder-VideoMixer" --icon=icon.ico AutoFolder.py
```

**Output:** Single `.exe` file in `dist/` folder  
**Note:** Users must have FFmpeg installed on their system or in PATH

---

### Option 2: Bundle FFmpeg in Executable

```powershell
# Download FFmpeg first from https://ffmpeg.org/download.html
# Extract ffmpeg.exe and ffprobe.exe to a location

pyinstaller --onefile --windowed ^
  --name "AutoFolder-VideoMixer" ^
  --icon=icon.ico ^
  --add-binary "C:\path\to\ffmpeg.exe;bin" ^
  --add-binary "C:\path\to\ffprobe.exe;bin" ^
  AutoFolder.py
```

**Output:** Single `.exe` with embedded FFmpeg  
**Pros:** Everything in one file, no external dependencies  
**Cons:** Large file size (~100+ MB)

---

### Option 3: FFmpeg in Separate Folder (Recommended for Distribution)

```powershell
# Build without bundling FFmpeg
pyinstaller --onefile --windowed --name "AutoFolder-VideoMixer" --icon=icon.ico AutoFolder.py

# Then manually create this structure:
# AutoFolder-VideoMixer.exe
# bin/
#   ├── ffmpeg.exe
#   └── ffprobe.exe
```

**Output:** Smaller `.exe` + `bin` folder  
**Pros:** Smaller download, easier to update FFmpeg separately  
**Cons:** Multiple files to distribute

---

### Option 4: Using the Spec File (Advanced Customization)

```powershell
# Edit AutoFolder-VideoMixer.spec to customize build settings
pyinstaller AutoFolder-VideoMixer.spec
```

The spec file allows fine-grained control over:
- Data files inclusion
- Import hooks
- UPX compression
- Runtime options

---

## 🚀 Creating an Installer

### Using Inno Setup (Professional Installer)

1. **Download Inno Setup**: https://jrsoftware.org/isinfo.php
2. **Edit `installer.iss`**:
   - Update `MyAppPublisher` with your name
   - Update `MyAppURL` with your GitHub URL
   - Generate a unique GUID for `AppId` (use https://guidgenerator.com)
   - Uncomment FFmpeg lines if bundling

3. **Build the executable first**:
   ```powershell
   pyinstaller AutoFolder-VideoMixer.spec
   ```

4. **Compile installer**:
   - Open `installer.iss` in Inno Setup Compiler
   - Click **Build** > **Compile**
   - Installer will be created in `installer_output/`

**Output:** Professional Windows installer (`.exe`)

---

## 📋 Complete Release Checklist

### Before Building:
- [ ] Update `__version__` in `AutoFolder.py`
- [ ] Test application thoroughly
- [ ] Create/update `icon.ico` (256x256 recommended)
- [ ] Update `README.md` with latest features
- [ ] Add `LICENSE.txt` file (MIT, GPL, etc.)

### Build Process:
- [ ] Clean previous builds: `rmdir /s /q build dist`
- [ ] Build executable: `pyinstaller AutoFolder-VideoMixer.spec`
- [ ] Test the `.exe` on a clean Windows machine
- [ ] Create installer (optional): Compile `installer.iss`

### FFmpeg Options:
Choose one:
- [ ] Bundle FFmpeg in executable (large file)
- [ ] Include FFmpeg in `bin/` folder (medium size)
- [ ] Require users to install FFmpeg (smallest size, document in README)

### Distribution:
- [ ] Create GitHub Release
- [ ] Upload executable/installer
- [ ] Include FFmpeg or instructions
- [ ] Write release notes
- [ ] Update README with download link

---

## 🧪 Testing Your Build

### On Your Development Machine:
```powershell
cd dist
.\AutoFolder-VideoMixer.exe
```

### On a Clean Machine (Important!):
1. Copy `.exe` (and `bin/` folder if applicable) to a test machine
2. Test without Python installed
3. Test without FFmpeg in PATH (if not bundled)
4. Test all features:
   - File selection
   - Video generation
   - Auto-watch mode
   - Delete option

---

## 📝 Common Build Issues

### "Module not found" errors
```powershell
# Add missing module to spec file hiddenimports:
hiddenimports=['tkinter', 'send2trash'],
```

### Large executable size
- Remove `--onefile` flag for folder-based distribution
- Use UPX compression (enabled in spec file)
- Don't bundle FFmpeg in executable

### FFmpeg not found after packaging
- Check that `find_ffmpeg()` function works correctly
- Ensure FFmpeg is in correct location relative to `.exe`
- Test on machine without FFmpeg in system PATH

### Antivirus false positives
- Submit `.exe` to antivirus vendors
- Sign your executable with code signing certificate
- Build on clean machine without development tools

---

## 🔐 Optional: Code Signing

For professional releases, consider code signing:

1. Purchase code signing certificate (e.g., from DigiCert, Sectigo)
2. Sign the executable:
   ```powershell
   signtool sign /f certificate.pfx /p password /t http://timestamp.digicert.com dist\AutoFolder-VideoMixer.exe
   ```

Benefits:
- No "Unknown Publisher" warnings
- Builds trust with users
- Prevents antivirus false positives

---

## 📦 Quick Build Commands

### Development Build (Fast):
```powershell
pyinstaller --onefile --windowed --name "AutoFolder-VideoMixer" AutoFolder.py
```

### Production Build (Optimized):
```powershell
pyinstaller AutoFolder-VideoMixer.spec
```

### Full Installer Build:
```powershell
# 1. Build executable
pyinstaller AutoFolder-VideoMixer.spec

# 2. Open installer.iss in Inno Setup and compile
# Or use command line:
iscc installer.iss
```

---

## 📚 Additional Resources

- **PyInstaller Documentation**: https://pyinstaller.org/
- **Inno Setup Documentation**: https://jrsoftware.org/ishelp/
- **FFmpeg Downloads**: https://ffmpeg.org/download.html
- **Icon Generator**: https://convertico.com/

---

## 💡 Tips for Distribution

1. **Include README**: Always include usage instructions
2. **Virus Scan**: Scan your build before distributing
3. **Test Broadly**: Test on Windows 10 and 11
4. **Document Requirements**: Clearly state Windows version requirements
5. **Provide Examples**: Include sample images/videos for testing
6. **Update Regularly**: Keep FFmpeg and dependencies updated

---

**Questions or issues?** Open an issue on GitHub!
