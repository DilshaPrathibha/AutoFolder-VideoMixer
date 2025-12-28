# Changelog

All notable changes to AutoFolder VideoMixer will be documented in this file.

## [1.0.0] - 2025-12-28

### 🎉 Initial Release

#### Added
- **Core Features**
  - Combine videos and images from folder into single MP4
  - Auto-normalize all media to 1280×720 @ 30fps
  - Convert images to video clips with custom duration
  - Loop media to reach fixed video length or combine once naturally
  - Multiple sorting options (name, date newest/oldest, random)
  - Live progress display during generation
  
- **Advanced Features**
  - Auto-watch folder mode - regenerate video when files change
  - Safe file deletion (moves to Recycle Bin instead of permanent delete)
  - Smart FFmpeg detection (bundled, system PATH, common locations)
  
- **User Interface**
  - Simple Tkinter GUI
  - Browse button for folder selection
  - Visual progress indicator
  - Error handling and user feedback
  
- **Technical**
  - Standalone Windows executable (no Python installation needed)
  - FFmpeg and FFprobe bundled in executable
  - Version number in application title
  - Automatic resource path detection for packaged/dev environments
  - User home directory defaults instead of hardcoded paths

#### Supported Formats
- **Videos**: MP4, MOV, AVI, MKV, WEBM, M4V
- **Images**: JPG, JPEG, PNG, WEBP

#### Output Specifications
- Resolution: 1280×720 (720p HD)
- Frame Rate: 30 FPS
- Codec: H.264 (libx264)
- Pixel Format: yuv420p
- Container: MP4

#### Documentation
- Complete README with installation and usage instructions
- Detailed BUILD.md for developers
- RELEASE.md for distribution guidance
- Quick start guide for end users
- Inno Setup installer script

#### Build System
- PyInstaller spec file for customized builds
- Requirements.txt for Python dependencies
- .gitignore for clean repository
- Automated build process

---

## [Unreleased]

### Planned Features
- Custom output resolution settings
- Audio track support
- Transition effects between clips
- Custom watermark overlay
- Batch processing multiple folders
- Command-line interface option
- Configuration file support
- Application icon
- Code signing
- Auto-update mechanism
- Mac and Linux support

---

## Release Notes Format

### Version Format
- **Major.Minor.Patch** (e.g., 1.0.0)
- Major: Breaking changes or significant new features
- Minor: New features, backwards compatible
- Patch: Bug fixes, minor improvements

### Categories
- **Added**: New features
- **Changed**: Changes to existing features
- **Deprecated**: Features to be removed
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security improvements

---

**Note**: This project follows [Semantic Versioning](https://semver.org/).
