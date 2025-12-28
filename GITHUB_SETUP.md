# 📤 GitHub Repository Setup Guide

## ✅ What to Upload to GitHub

### **INCLUDE (Source Code & Documentation):**

```
AutoFolder-VideoMixer/
├── .gitignore                          ✅ Include
├── README.md                           ✅ Include
├── BUILD.md                            ✅ Include
├── CHANGELOG.md                        ✅ Include
├── UPGRADE_GUIDE.md                    ✅ Include
├── DEV_WORKFLOW.md                     ✅ Include
├── RELEASE.md                          ✅ Include
├── UPGRADE_FLOWCHART.txt               ✅ Include
├── requirements.txt                    ✅ Include
├── AutoFolder-VideoMixer.spec          ✅ Include
├── installer.iss                       ✅ Include
├── build.bat                           ✅ Include
├── build.ps1                           ✅ Include
├── run.bat                             ✅ Include
└── src/                                ✅ Include
    └── AutoFolder.py                   ✅ Include (only the .py file!)
```

### **EXCLUDE (Binary Files & Build Artifacts):**

```
❌ .venv/                               (Virtual environment - users create their own)
❌ build/                               (Build artifacts - regenerated)
❌ dist/                                (Built executable - goes to Releases)
❌ ffmpeg-8.0.1-full_build/            (Too large - except AutoFolder.py)
❌ *.exe                                (Executables - goes to Releases)
❌ *.zip                                (Release packages - goes to Releases)
❌ AutoFolder-VideoMixer-v1.0.0/       (Release folder - temporary)
❌ __pycache__/                         (Python cache - regenerated)
```

---

## 🏗️ Recommended Repository Structure

### **Option 1: Simplified Structure (Recommended)**

```
AutoFolder-VideoMixer/
├── .gitignore
├── README.md
├── CHANGELOG.md
├── BUILD.md
├── UPGRADE_GUIDE.md
├── DEV_WORKFLOW.md
├── requirements.txt
├── AutoFolder-VideoMixer.spec
├── installer.iss
├── src/
│   └── AutoFolder.py              ← Only source code
├── scripts/
│   ├── build.bat
│   ├── build.ps1
│   └── run.bat
└── docs/
    ├── RELEASE.md
    └── UPGRADE_FLOWCHART.txt
```

### **Option 2: Current Structure (Also Good)**

Keep AutoFolder.py where it is:
```
AutoFolder-VideoMixer/
├── (documentation files)
├── AutoFolder-VideoMixer.spec
├── build.bat
├── build.ps1
└── ffmpeg-8.0.1-full_build/
    └── bin/
        └── AutoFolder.py          ← Only this file from ffmpeg folder
```

**Note in README:** "Users must download FFmpeg separately and place AutoFolder.py in the bin folder"

---

## 📋 Step-by-Step Upload Process

### **Step 1: Reorganize Files (Optional but Recommended)**

Move source code to cleaner location:

```powershell
# Create src folder
New-Item -ItemType Directory -Path "src" -Force

# Copy source code
Copy-Item "ffmpeg-8.0.1-full_build\bin\AutoFolder.py" -Destination "src\AutoFolder.py"

# Update .spec file to point to new location
# Change: 'ffmpeg-8.0.1-full_build/bin/AutoFolder.py'
# To:     'src/AutoFolder.py'
```

### **Step 2: Clean Up Before Committing**

```powershell
# Remove build artifacts
Remove-Item -Recurse -Force build, dist -ErrorAction SilentlyContinue

# Remove release folders
Remove-Item -Recurse -Force AutoFolder-VideoMixer-v* -ErrorAction SilentlyContinue

# Remove zip files
Remove-Item *.zip -ErrorAction SilentlyContinue

# The .gitignore will handle the rest
```

### **Step 3: Initialize Git (if not already done)**

```powershell
# Initialize repository
git init

# Check what will be committed
git status

# Add files (respects .gitignore)
git add .

# Check what's staged
git status
```

### **Step 4: First Commit**

```powershell
# Commit to local repository
git commit -m "Initial commit: AutoFolder VideoMixer v1.0.0

- Complete source code
- Build scripts and documentation
- PyInstaller configuration
- Inno Setup installer script"

# Tag the version
git tag -a v1.0.0 -m "Release version 1.0.0"
```

### **Step 5: Create GitHub Repository**

1. Go to https://github.com/new
2. **Repository name:** `AutoFolder-VideoMixer`
3. **Description:** "Automatically combines videos and images from a folder into a single MP4 video"
4. **Public** or **Private** - your choice
5. **Do NOT** initialize with README (you already have one)
6. Click **Create repository**

### **Step 6: Push to GitHub**

```powershell
# Add GitHub remote (replace with your username)
git remote add origin https://github.com/YOUR_USERNAME/AutoFolder-VideoMixer.git

# Push code
git branch -M main
git push -u origin main

# Push tags
git push --tags
```

### **Step 7: Create GitHub Release**

1. Go to your repository on GitHub
2. Click **Releases** → **Create a new release**
3. **Choose tag:** v1.0.0
4. **Release title:** AutoFolder VideoMixer v1.0.0
5. **Description:**
   ```markdown
   ## 🎉 Initial Release
   
   First stable release of AutoFolder VideoMixer!
   
   ### Features
   - Combine videos and images into single MP4
   - Auto-normalize to 720p @ 30fps
   - Multiple sorting options
   - Auto-watch folder mode
   - Safe file deletion (Recycle Bin)
   
   ### Downloads
   - Windows: Download the .zip file below
   - Extract and run AutoFolder-VideoMixer.exe
   - No installation required!
   
   ### Requirements
   - Windows 10/11 (64-bit)
   - FFmpeg bundled - no external dependencies!
   
   For build instructions, see [BUILD.md](BUILD.md)
   ```
6. **Upload files:** Drag your `AutoFolder-VideoMixer-v1.0.0-Windows.zip`
7. Click **Publish release**

---

## 📝 Update Your README

Add this to the top of README.md:

```markdown
# 🎬 AutoFolder VideoMixer

[![Release](https://img.shields.io/github/v/release/YOUR_USERNAME/AutoFolder-VideoMixer)](https://github.com/YOUR_USERNAME/AutoFolder-VideoMixer/releases)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows-blue)](https://github.com/YOUR_USERNAME/AutoFolder-VideoMixer)

Automatically combines videos and images from a folder into a single MP4 video.

[Download Latest Release](https://github.com/YOUR_USERNAME/AutoFolder-VideoMixer/releases/latest) | [Documentation](BUILD.md) | [Changelog](CHANGELOG.md)
```

---

## 🎯 Key Points

### ✅ **DO Upload:**
- **Source code** (.py files)
- **Documentation** (.md files)
- **Build scripts** (.bat, .ps1, .spec, .iss)
- **Requirements** (requirements.txt)
- **.gitignore** (to exclude binary files)

### ❌ **DON'T Upload:**
- **Executables** (.exe files) → Use GitHub Releases
- **FFmpeg binaries** (100+ MB) → Users download separately
- **Build artifacts** (build/, dist/) → Regenerated locally
- **Virtual environments** (.venv/) → Users create their own
- **ZIP packages** → Use GitHub Releases

### 📦 **For Distribution:**
- Upload **.exe** and **.zip** to **GitHub Releases** (not the repo)
- Each new version gets a new Release
- Users download from Releases page

---

## 🔄 Workflow After Initial Upload

### Making Updates:

```powershell
# 1. Make your changes
code src\AutoFolder.py

# 2. Test and build
.\build.bat

# 3. Update version and docs
# Edit: __version__ in AutoFolder.py
# Edit: CHANGELOG.md

# 4. Commit changes
git add .
git commit -m "Fixed bug in video duration (v1.0.1)"
git tag v1.0.1
git push
git push --tags

# 5. Create new GitHub Release
# Upload new .zip file to releases page
```

---

## 📊 Repository Size Comparison

| Item | Size | In Repo? |
|------|------|----------|
| Source code (.py) | ~30 KB | ✅ YES |
| Documentation | ~50 KB | ✅ YES |
| Build scripts | ~20 KB | ✅ YES |
| FFmpeg binaries | 100+ MB | ❌ NO (too large) |
| Built .exe | 163 MB | ❌ NO (use Releases) |
| Virtual environment | 50+ MB | ❌ NO (regenerated) |

**Total repo size with recommendations: ~500 KB** 🎉

---

## 💡 Pro Tips

1. **Keep repo small** - Only source code and docs
2. **Use Releases** - For distributing executables
3. **Tag versions** - Makes tracking easy
4. **Update CHANGELOG** - Users appreciate it
5. **Good README** - First impression matters
6. **License file** - Add MIT or your choice
7. **Topics** - Add tags: python, video-processing, ffmpeg, windows

---

## 🚀 Quick Command Summary

```powershell
# Clean up before committing
Remove-Item -Recurse build, dist, AutoFolder-VideoMixer-v*, *.zip -ErrorAction SilentlyContinue

# Check what will be committed
git status

# Commit everything (respects .gitignore)
git add .
git commit -m "Your commit message"

# Tag version
git tag v1.0.0

# Push to GitHub
git push origin main
git push --tags
```

---

## 📖 Suggested README Updates

Add to your README.md:

```markdown
## 🏗️ Building from Source

### Prerequisites
- Python 3.8+
- FFmpeg (download from https://ffmpeg.org/download.html)

### Build Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/AutoFolder-VideoMixer.git
   cd AutoFolder-VideoMixer
   ```

2. Create virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Place AutoFolder.py in FFmpeg bin folder:
   ```bash
   # Copy src\AutoFolder.py to your ffmpeg\bin\ folder
   ```

5. Build executable:
   ```bash
   .\build.bat
   # Choose option 2 (Full Rebuild)
   ```

For detailed build instructions, see [BUILD.md](BUILD.md)
```

---

## ✅ Final Checklist

Before pushing to GitHub:

- [ ] Updated .gitignore (excludes binaries)
- [ ] Source code in clean location
- [ ] README.md has download/build instructions
- [ ] CHANGELOG.md is up to date
- [ ] Removed build artifacts (build/, dist/)
- [ ] Removed FFmpeg binaries (too large)
- [ ] Removed .venv folder
- [ ] License file added (optional but recommended)
- [ ] All documentation files included
- [ ] Build scripts included
- [ ] Tested that others can clone and build

---

**Summary:** Upload only source code and docs (~500 KB). Put executables and FFmpeg in GitHub Releases for distribution!
