import os
import sys
import subprocess
import time
import tempfile
import random
import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from send2trash import send2trash
import webbrowser

__version__ = "1.1.0"

# ================= RESOURCE PATH HELPER =================
def get_resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ================= DEFAULT PATHS =================
# Use user's home directory instead of hardcoded paths
DEFAULT_INPUT_FOLDER  = os.path.join(os.path.expanduser("~"), "Videos")
DEFAULT_OUTPUT_FOLDER = os.path.join(os.path.expanduser("~"), "Videos", "AutoFolder_Output")

# Try to find FFmpeg in common locations
def find_ffmpeg():
    """Attempt to locate FFmpeg executable"""
    # First check same directory as script (since we're in bin folder with ffmpeg)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    same_dir_ffmpeg = os.path.join(script_dir, "ffmpeg.exe")
    same_dir_ffprobe = os.path.join(script_dir, "ffprobe.exe")
    
    if os.path.exists(same_dir_ffmpeg) and os.path.exists(same_dir_ffprobe):
        return same_dir_ffmpeg, same_dir_ffprobe
    
    # Check bundled bin folder (for packaged app)
    bundled_ffmpeg = get_resource_path(os.path.join("bin", "ffmpeg.exe"))
    bundled_ffprobe = get_resource_path(os.path.join("bin", "ffprobe.exe"))
    
    if os.path.exists(bundled_ffmpeg) and os.path.exists(bundled_ffprobe):
        return bundled_ffmpeg, bundled_ffprobe
    
    # Check system PATH
    import shutil
    system_ffmpeg = shutil.which("ffmpeg")
    system_ffprobe = shutil.which("ffprobe")
    
    if system_ffmpeg and system_ffprobe:
        return system_ffmpeg, system_ffprobe
    
    # Fallback to common installation paths
    common_paths = [
        r"C:\ffmpeg\bin\ffmpeg.exe",
        r"C:\ffmpeg\ffmpeg-8.0.1-full_build\bin\ffmpeg.exe",
        r"C:\Program Files\ffmpeg\bin\ffmpeg.exe",
    ]
    
    for path in common_paths:
        if os.path.exists(path):
            ffprobe = path.replace("ffmpeg.exe", "ffprobe.exe")
            if os.path.exists(ffprobe):
                return path, ffprobe
    
    return None, None

FFMPEG_PATH, FFPROBE_PATH = find_ffmpeg()
# ================================================

# ================= SETTINGS ======================
DEFAULT_IMAGE_DURATION = 1.5
TARGET_W = 1280
TARGET_H = 720
TARGET_FPS = "30"
AUTO_CHECK_INTERVAL_MS = 3000
# ================================================

VIDEO_EXTS = (".mp4", ".mov", ".avi", ".mkv", ".webm", ".m4v")
IMAGE_EXTS = (".jpg", ".jpeg", ".png", ".webp")

ASPECT_SAFE_FILTER = (
    f"scale={TARGET_W}:{TARGET_H}:force_original_aspect_ratio=decrease,"
    f"pad={TARGET_W}:{TARGET_H}:(ow-iw)/2:(oh-ih)/2"
)

ORDER_NAME = "Sort by name"
ORDER_DATE_NEW = "Sort by date (newest first)"
ORDER_DATE_OLD = "Sort by date (oldest first)"
ORDER_RANDOM = "Random"


# ------------------------------------------------

def list_media_files(folder, order_mode):
    if not os.path.isdir(folder):
        return []

    files = [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.lower().endswith(VIDEO_EXTS + IMAGE_EXTS)
    ]

    if order_mode == ORDER_RANDOM:
        random.shuffle(files)
        return files
    if order_mode == ORDER_DATE_NEW:
        return sorted(files, key=os.path.getmtime, reverse=True)
    if order_mode == ORDER_DATE_OLD:
        return sorted(files, key=os.path.getmtime)

    return sorted(files, key=lambda x: os.path.basename(x).lower())


def get_video_duration(path):
    try:
        r = subprocess.run(
            [
                FFPROBE_PATH, "-v", "error",
                "-show_entries", "format=duration",
                "-of", "default=noprint_wrappers=1:nokey=1",
                path
            ],
            capture_output=True, text=True, check=True
        )
        return float(r.stdout.strip())
    except:
        return 0.0


def estimate_total_duration(files, image_duration):
    total = 0.0
    for f in files:
        total += image_duration if f.lower().endswith(IMAGE_EXTS) else get_video_duration(f)
    return total


def normalize_video(input_video, out_dir):
    out = os.path.join(
        out_dir,
        os.path.splitext(os.path.basename(input_video))[0] + "_norm.mp4"
    )

    subprocess.run([
        FFMPEG_PATH, "-y",
        "-err_detect", "ignore_err",
        "-i", input_video,
        "-vf", ASPECT_SAFE_FILTER,
        "-r", TARGET_FPS,
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        out
    ], check=True)

    return out


def image_to_video(image_path, out_dir, image_duration):
    out = os.path.join(
        out_dir,
        os.path.splitext(os.path.basename(image_path))[0] + "_img.mp4"
    )

    subprocess.run([
        FFMPEG_PATH, "-y",
        "-loop", "1",
        "-i", image_path,
        "-t", str(image_duration),
        "-vf", ASPECT_SAFE_FILTER,
        "-r", TARGET_FPS,
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        out
    ], check=True)

    return out, image_duration


def build_clips(files, temp_dir, image_duration, progress_cb):
    clips = []
    total = len(files)

    for i, f in enumerate(files, start=1):
        progress_cb(i, total, "Processing media")

        if f.lower().endswith(IMAGE_EXTS):
            clip, dur = image_to_video(f, temp_dir, image_duration)
        else:
            clip = normalize_video(f, temp_dir)
            dur = get_video_duration(clip)

        if dur > 0:
            clips.append((clip, dur))

    return clips


def build_clips_fixed(files, temp_dir, minutes, image_duration, progress_cb):
    target_seconds = minutes * 60
    normalized = build_clips(files, temp_dir, image_duration, progress_cb)

    clips, total = [], 0
    while total < target_seconds:
        for clip, dur in normalized:
            clips.append((clip, dur))
            total += dur
            if total >= target_seconds:
                break

    return clips


def write_concat_list(clips, list_file):
    with open(list_file, "w", encoding="utf-8") as f:
        for path, _ in clips:
            f.write(f"file '{path.replace('\\', '/')}'\n")


def final_concat(list_file, output):
    subprocess.run([
        FFMPEG_PATH, "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", list_file,
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-r", TARGET_FPS,
        "-movflags", "+faststart",
        output
    ], check=True)


# ================= GUI ======================

class App:
    def __init__(self, root):
        root.title(f"AutoFolder VideoMixer v{__version__}")
        root.resizable(False, False)
        
        # Set window icon
        try:
            icon_path = get_resource_path('icon.ico')
            if os.path.exists(icon_path):
                root.iconbitmap(icon_path)
        except Exception as e:
            pass  # Icon is optional, continue without it
        
        # Check if FFmpeg is available
        if not FFMPEG_PATH or not FFPROBE_PATH:
            messagebox.showerror(
                "FFmpeg Not Found",
                "FFmpeg and FFprobe are required but not found.\n\n"
                "Please install FFmpeg and ensure it's in your system PATH,\n"
                "or place ffmpeg.exe and ffprobe.exe in a 'bin' folder next to this application.\n\n"
                "Download from: https://ffmpeg.org/download.html"
            )
            root.destroy()
            return

        frame = ttk.Frame(root, padding=14)
        frame.grid(row=0, column=0)

        self.input_var = tk.StringVar(value=DEFAULT_INPUT_FOLDER)
        self.output_var = tk.StringVar(value=DEFAULT_OUTPUT_FOLDER)
        self.order_var = tk.StringVar(value=ORDER_NAME)

        self.length_mode_var = tk.StringVar(value="Natural")
        self.natural_var = tk.BooleanVar(value=True)  # Default to natural mode
        self.auto_var = tk.BooleanVar()
        self.delete_var = tk.BooleanVar()
        self.delete_var.trace_add("write", self.confirm_delete)
        self.auto_var.trace_add("write", self.check_auto_natural)
        self.length_mode_var.trace_add("write", self.on_length_mode_change)
        self.dont_ask_delete = False  # Flag for "don't ask again"
        self.confirming_delete = False  # Flag to prevent recursive dialog calls
        self.has_generated_once = False  # Flag to track if Generate button has been clicked

        # ----- Input folder -----
        ttk.Label(frame, text="Input folder:").grid(row=0, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.input_var, width=42).grid(row=0, column=1)
        ttk.Button(frame, text="Browse", command=self.pick_input).grid(row=0, column=2, padx=6)

        # ----- Output folder -----
        ttk.Label(frame, text="Output folder:").grid(row=1, column=0, sticky="w", pady=6)
        ttk.Entry(frame, textvariable=self.output_var, width=42).grid(row=1, column=1, pady=6)
        ttk.Button(frame, text="Browse", command=self.pick_output).grid(row=1, column=2, padx=6)

        # ----- Video length mode (dropdown on left, time input on right) -----
        ttk.Label(frame, text="Video length mode:").grid(row=2, column=0, sticky="w")
        
        # Create a sub-frame for the dropdown and entry
        length_frame = ttk.Frame(frame)
        length_frame.grid(row=2, column=1, columnspan=2, sticky="w")
        
        # Dropdown menu
        self.length_mode_combo = ttk.Combobox(
            length_frame,
            textvariable=self.length_mode_var,
            values=["Natural", "Custom"],
            state="readonly",
            width=18
        )
        self.length_mode_combo.grid(row=0, column=0, padx=(0, 8))
        
        # Time input entry
        self.minutes_entry = ttk.Entry(length_frame, width=20)
        self.minutes_entry.grid(row=0, column=1)
        self.minutes_entry.bind("<FocusIn>", self.on_minutes_click)
        # Initialize with "Click to calculate..." since default mode is Natural
        self.minutes_entry.insert(0, "Click to calculate...")
        self.minutes_entry.config(state="readonly")
        
        self.saved_minutes = ""

        # ----- Image duration -----
        ttk.Label(frame, text="Image duration (seconds):").grid(row=3, column=0, sticky="w", pady=6)
        self.image_duration_entry = ttk.Entry(frame, width=28)
        self.image_duration_entry.insert(0, str(DEFAULT_IMAGE_DURATION))
        self.image_duration_entry.grid(row=3, column=1, sticky="w", pady=6)

        # ----- Order -----
        ttk.Label(frame, text="Order:").grid(row=5, column=0, sticky="w")
        ttk.Combobox(
            frame,
            textvariable=self.order_var,
            values=[ORDER_NAME, ORDER_DATE_NEW, ORDER_DATE_OLD, ORDER_RANDOM],
            state="readonly",
            width=26
        ).grid(row=5, column=1, sticky="w")

        # ----- Auto + delete -----
        ttk.Checkbutton(frame, text="Auto combine when files change", variable=self.auto_var)\
            .grid(row=6, column=0, columnspan=3, sticky="w", pady=(10, 4))

        ttk.Checkbutton(
            frame,
            text="Delete source files after combine (Recycle Bin)",
            variable=self.delete_var
        ).grid(row=7, column=0, columnspan=3, sticky="w", pady=4)

        # ----- Progress -----
        self.progress_label = ttk.Label(frame, text="")
        self.progress_label.grid(row=8, column=0, columnspan=3, sticky="w", pady=(10, 2))
        
        # ----- Auto-monitoring status indicator -----
        self.auto_status_label = ttk.Label(frame, text="", font=('Segoe UI', 8), foreground="#666666")
        self.auto_status_label.grid(row=9, column=0, columnspan=3, sticky="w", pady=(2, 6))

        # ----- Buttons -----
        btns = ttk.Frame(frame)
        btns.grid(row=10, column=0, columnspan=3, sticky="e", pady=(10, 0))

        ttk.Button(btns, text="Generate", command=self.run).grid(row=0, column=0, padx=6)
        ttk.Button(btns, text="Exit", command=root.destroy).grid(row=0, column=1)

        # ----- Creator Info -----
        creator_frame = ttk.Frame(frame)
        creator_frame.grid(row=11, column=0, columnspan=3, pady=(15, 0))
        
        ttk.Separator(frame, orient='horizontal').grid(row=12, column=0, columnspan=3, sticky='ew', pady=(10, 8))
        
        # Creator info in one line with clickable name
        creator_container = ttk.Frame(frame)
        creator_container.grid(row=13, column=0, columnspan=3)
        
        ttk.Label(creator_container, text="Created by: ", font=('Segoe UI', 8)).pack(side='left')
        
        # Creator name (clickable mailto link)
        name_label = tk.Label(
            creator_container, 
            text="Dilsha Prathibha", 
            font=('Segoe UI', 8, 'bold'),
            cursor='hand2'
        )
        name_label.pack(side='left')
        name_label.bind("<Button-1>", lambda e: webbrowser.open("mailto:dilshaprathibha@gmail.com"))

        root.bind("<Return>", lambda e: self.run())

        self.last_snapshot = set()
        self.schedule_auto_check(root)

    def confirm_delete(self, *_):
        # Prevent recursive calls when we programmatically change the checkbox
        if self.confirming_delete:
            return
            
        if self.delete_var.get():
            # Skip confirmation if user chose "don't ask again"
            if self.dont_ask_delete:
                return
            
            # Set flag to prevent recursive calls
            self.confirming_delete = True
            
            # Immediately uncheck the box - it will only be rechecked if user clicks Yes
            self.delete_var.set(False)
            
            # Force GUI update to show unchecked state immediately
            self.delete_var._root.update_idletasks()
            
            # Create custom dialog with "Don't ask again" checkbox
            dialog = tk.Toplevel()
            dialog.title("Warning")
            dialog.resizable(False, False)
            dialog.transient()
            dialog.grab_set()
            
            # Center the dialog
            dialog.geometry("400x180")
            dialog.update_idletasks()
            x = (dialog.winfo_screenwidth() // 2) - (400 // 2)
            y = (dialog.winfo_screenheight() // 2) - (180 // 2)
            dialog.geometry(f"400x180+{x}+{y}")
            
            # Warning icon and message
            frame = ttk.Frame(dialog, padding=20)
            frame.pack(fill='both', expand=True)
            
            message = tk.Label(
                frame,
                text="⚠️ Warning: Source files will be deleted after combining!\n\n"
                     "Files will be moved to the Recycle Bin.",
                justify='left',
                wraplength=350,
                font=('Segoe UI', 9)
            )
            message.pack(pady=(0, 15))
            
            # "Don't ask again" checkbox
            dont_ask_var = tk.BooleanVar()
            dont_ask_check = ttk.Checkbutton(
                frame,
                text="Don't show this warning again",
                variable=dont_ask_var
            )
            dont_ask_check.pack(anchor='w', pady=(0, 15))
            
            # Buttons
            btn_frame = ttk.Frame(frame)
            btn_frame.pack()
            
            result = {'value': False}
            
            def on_ok():
                result['value'] = True
                if dont_ask_var.get():
                    self.dont_ask_delete = True
                dialog.destroy()
            
            def on_close():
                result['value'] = False
                dialog.destroy()
            
            # Handle window close button (X) - cancel action
            dialog.protocol("WM_DELETE_WINDOW", on_close)
            
            ttk.Button(btn_frame, text="OK", command=on_ok, width=15).pack()
            
            # Wait for dialog to close
            dialog.wait_window()
            
            # Only check the box if user clicked "OK"
            if result['value']:
                self.delete_var.set(True)
            
            # Reset flag
            self.confirming_delete = False

    def check_auto_natural(self, *_):
        """Auto-enable 'Natural' mode if final video length is empty and auto-combine is checked"""
        if self.auto_var.get():
            # Check if minutes entry is empty
            minutes_value = self.minutes_entry.get().strip()
            if not minutes_value:
                self.length_mode_var.set("Natural")
                self.natural_var.set(True)

    def pick_input(self):
        folder = filedialog.askdirectory()
        if folder:
            self.input_var.set(folder)
            self.update_estimate()

    def pick_output(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_var.set(folder)

    def set_progress(self, current, total, text):
        percent = int((current / total) * 100) if total else 0
        self.progress_label.config(text=f"{text}: {current}/{total} ({percent}%)")
        self.progress_label.update_idletasks()

    def on_length_mode_change(self, *_):
        """Called when video length mode dropdown changes"""
        mode = self.length_mode_var.get()
        
        if mode == "Natural":
            # Natural mode - show "Click to calculate..."
            self.natural_var.set(True)
            if str(self.minutes_entry.cget("state")) != "readonly":
                self.saved_minutes = self.minutes_entry.get()
            self.minutes_entry.config(state="normal")
            self.minutes_entry.delete(0, tk.END)
            self.minutes_entry.insert(0, "Click to calculate...")
            self.minutes_entry.config(state="readonly")
        else:
            # Custom mode - enable manual input
            self.natural_var.set(False)
            self.minutes_entry.config(state="normal")
            self.minutes_entry.delete(0, tk.END)
            if self.saved_minutes:
                self.minutes_entry.insert(0, self.saved_minutes)
            else:
                # Show placeholder
                self.minutes_entry.insert(0, "Enter minutes...")
                self.minutes_entry.config(foreground="gray")
                # Clear placeholder on focus
                def clear_placeholder(e):
                    if self.minutes_entry.get() == "Enter minutes...":
                        self.minutes_entry.delete(0, tk.END)
                        self.minutes_entry.config(foreground="black")
                self.minutes_entry.bind("<FocusIn>", clear_placeholder, add="+")
            self.minutes_entry.focus()

    def on_minutes_click(self, event):
        """Called when user clicks on the minutes field"""
        if self.natural_var.get():
            # Natural mode is on - calculate estimate
            # Show "calculating..." immediately
            self.minutes_entry.config(state="normal")
            self.minutes_entry.delete(0, tk.END)
            self.minutes_entry.insert(0, "Calculating...")
            self.minutes_entry.config(state="readonly")
            self.minutes_entry.update_idletasks()  # Force GUI update
            
            # Perform calculation
            self.calculate_estimate()

    def calculate_estimate(self):
        """Calculate and display estimated video length"""
        try:
            image_duration = float(self.image_duration_entry.get())
        except:
            return

        files = list_media_files(self.input_var.get(), self.order_var.get())
        total_sec = estimate_total_duration(files, image_duration)
        minutes = total_sec / 60

        self.minutes_entry.config(state="normal")
        self.minutes_entry.delete(0, tk.END)
        self.minutes_entry.insert(0, f"Estimated: {minutes:.2f}")
        self.minutes_entry.config(state="readonly")

    def schedule_auto_check(self, root):
        root.after(AUTO_CHECK_INTERVAL_MS, lambda: self.auto_check(root))

    def auto_check(self, root):
        if self.auto_var.get() and self.has_generated_once:
            self.auto_status_label.config(text="🟢 Auto-monitoring active - watching for file changes...")
            current_files = set(list_media_files(self.input_var.get(), self.order_var.get()))
            if current_files and current_files != self.last_snapshot:
                self.last_snapshot = current_files
                self.auto_status_label.config(text="🔄 Auto-monitoring: Processing changes...")
                self.run()
                self.auto_status_label.config(text="🟢 Auto-monitoring active - watching for file changes...")
        else:
            self.auto_status_label.config(text="")
        self.schedule_auto_check(root)

    def run(self):
        # Mark that Generate button has been clicked at least once
        self.has_generated_once = True
        
        input_folder = self.input_var.get()
        output_folder = self.output_var.get()

        files = list_media_files(input_folder, self.order_var.get())
        if not files:
            return

        try:
            image_duration = float(self.image_duration_entry.get())
            if image_duration <= 0:
                raise ValueError
        except:
            messagebox.showerror("Error", "Invalid image duration.")
            return

        natural = self.natural_var.get()

        if not natural:
            try:
                minutes = float(self.minutes_entry.get())
                if minutes <= 0:
                    raise ValueError
            except:
                messagebox.showerror("Error", "Invalid minutes.")
                return

        with tempfile.TemporaryDirectory() as temp_dir:
            clips = (
                build_clips(files, temp_dir, image_duration, self.set_progress)
                if natural
                else build_clips_fixed(files, temp_dir, minutes, image_duration, self.set_progress)
            )

            os.makedirs(output_folder, exist_ok=True)
            ts = time.strftime("%Y%m%d_%H%M%S")
            list_file = os.path.join(output_folder, f"list_{ts}.txt")
            out_video = os.path.join(output_folder, f"combined_{ts}.mp4")

            self.set_progress(len(files), len(files), "Combining")
            write_concat_list(clips, list_file)
            final_concat(list_file, out_video)

            if self.delete_var.get():
                try:
                    deleted_count = 0
                    failed_files = []
                    for f in files:
                        try:
                            # Normalize path to handle any path issues
                            file_path = os.path.normpath(f)
                            if os.path.exists(file_path):
                                send2trash(file_path)
                                deleted_count += 1
                            else:
                                failed_files.append((os.path.basename(f), "File not found"))
                        except Exception as e:
                            failed_files.append((os.path.basename(f), str(e)))
                    
                    # Show result
                    if failed_files:
                        error_msg = f"Deleted {deleted_count} files.\n\nFailed to delete {len(failed_files)} files:\n"
                        for fname, error in failed_files[:5]:  # Show first 5 errors
                            error_msg += f"\n{fname}: {error}"
                        if len(failed_files) > 5:
                            error_msg += f"\n... and {len(failed_files) - 5} more"
                        messagebox.showwarning("Partial Deletion", error_msg)
                except Exception as e:
                    messagebox.showerror("Delete Error", f"Error deleting files: {str(e)}")

            self.progress_label.config(text="Done ✔")
            messagebox.showinfo("Success", f"Video created:\n{out_video}")


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
