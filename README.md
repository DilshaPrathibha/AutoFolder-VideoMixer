# 🎬 AutoFolder VideoMixer

AutoFolder VideoMixer is a **Windows desktop application** that automatically converts and combines **videos and images from a folder into a single MP4 video**.  
It is designed for fast, repeatable video creation without manual editing.

Perfect for content creators, automation workflows, digital signage, and batch video generation.

---

## ✨ Features

- 📁 Combine **videos + images** from a folder
- 🖼️ Convert images into video clips with custom duration
- 🎞️ Normalize all media to:
  - 1280×720 resolution
  - 30 FPS
  - MP4 (H.264, yuv420p)
- 🔄 Loop media to reach a **fixed video length**
- ▶️ Or combine media **once until it naturally ends**
- 🔀 Sort media by:
  - Name
  - Date (newest / oldest)
  - Random order
- 👀 **Auto-watch folder** and regenerate video when files change
- 🗑️ Optional **safe deletion** of source files (Recycle Bin)
- 📊 Live progress display
- 🖱️ Simple, lightweight Tkinter GUI

---

## 🧠 How It Works (User View)

1. Select an **input folder** with images and videos  
2. Select an **output folder**
3. Choose:
   - Final video length **OR**
   - “Combine until media ends”
4. Set image duration (seconds)
5. Choose media order
6. Click **Generate**
7. Get a ready-to-use MP4 video

No timeline editing. No manual cuts. Just drop files and go.

---

## 📂 Supported Formats

### Videos
- MP4
- MOV
- AVI
- MKV
- WEBM
- M4V

### Images
- JPG / JPEG
- PNG
- WEBP

---

## ⚙️ Requirements

- **Windows**
- **Python 3.8+**
- **FFmpeg (Full Build)**  
- Python packages:
  ```bash
  pip install send2trash
