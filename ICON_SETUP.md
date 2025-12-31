# Icon Setup Instructions

To set the icon for AutoFolder-VideoMixer:

## Steps:

1. **Save the attached image** (the orange folder with magic wand icon) as `app_icon.png` in the project root directory:
   `D:\github Clone\AutoFolder-VideoMixer\app_icon.png`

2. **Run the icon conversion script**:
   - Open PowerShell in the project directory
   - Run: `& ".venv\Scripts\python.exe" create_icon.py`
   
   This will create `icon.ico` with multiple sizes for Windows compatibility.

3. **Update the spec file** (ALREADY DONE):
   - The `AutoFolder-VideoMixer.spec` file has been updated to use `icon='icon.ico'`

4. **Update the Python code** (ALREADY DONE):
   - The `src\AutoFolder.py` file now includes code to set the window icon

5. **Rebuild the application**:
   ```powershell
   & ".venv\Scripts\python.exe" -m PyInstaller AutoFolder-VideoMixer.spec --clean
   ```

## Result:

After these steps:
- ✓ The executable file icon in Windows File Explorer will show your custom icon
- ✓ The window title bar icon will show your custom icon when the app is running
- ✓ The taskbar icon will show your custom icon

## Quick Command (after saving app_icon.png):

```powershell
& ".venv\Scripts\python.exe" create_icon.py
& ".venv\Scripts\python.exe" -m PyInstaller AutoFolder-VideoMixer.spec --clean
```
