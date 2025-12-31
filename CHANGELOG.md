# Changelog

All notable changes to AutoFolder VideoMixer will be documented in this file.

## [1.1.0] - 2025-12-31

### 🎨 UI/UX Improvements

#### Added
- **Custom Application Icon**: Professional folder icon with magic wand
  - Visible in Windows File Explorer
  - Displayed in application window title bar
  - Shows in Windows taskbar
- **Smart Video Length Mode Dropdown**: 
  - "Natural" mode (default): Combine until media ends
  - "Custom" mode: Manual duration input
  - Improved UI layout on single row
- **Auto-Monitoring Status Indicator**: 
  - Real-time status display when auto-combine is active
  - Shows "🟢 Auto-monitoring active - watching for file changes..."
  - Shows "🔄 Auto-monitoring: Processing changes..." during processing
- **On-Demand Duration Calculation**: 
  - Click-to-calculate estimated video length
  - Shows "Calculating..." progress indicator
  - Improves performance by calculating only when needed

#### Enhanced
- **File Deletion Confirmation Dialog**:
  - "Don't ask again" checkbox for user preference
  - Only checks deletion option if user confirms "Yes"
  - Simplified to single OK button for warnings
- **Auto-Combine Behavior**:
  - Now requires clicking "Generate" button at least once before auto-monitoring starts
  - Prevents unwanted automatic processing on startup
  - Auto-enables "Natural" mode if video length is empty
- **Creator Information**:
  - Clickable name with mailto: link (opens email client)
  - Clean, professional one-line layout
- **Layout Improvements**:
  - Fixed overlapping progress and status labels
  - Better spacing between UI elements
  - Separate rows for progress and monitoring status

#### Fixed
- File deletion path normalization (handles Windows path issues)
- Icon bundling in executable (icon.ico properly embedded)
- Placeholder text behavior in Custom mode input field

### Technical
- Added Pillow library for icon conversion
- Improved icon resource handling with get_resource_path()
- Enhanced error messages for file deletion failures

---

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
