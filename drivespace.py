import psutil
import tkinter as tk
from tkinter import font

def get_disk_space():
    drives = psutil.disk_partitions(all=True)
    disk_space_info = {}

    for drive in drives:
        drive_letter = drive.device.split(":")[0].upper()
        disk_usage = psutil.disk_usage(drive.mountpoint)
        total_space = _format_bytes(disk_usage.total)
        used_space = _format_bytes(disk_usage.used)
        free_space = _format_bytes(disk_usage.free)
        disk_space_info[drive_letter] = {
            "total": total_space,
            "used": used_space,
            "free": free_space,
        }

    return disk_space_info

def _format_bytes(bytes_val):
    for unit in ['', 'KB', 'MB', 'GB', 'TB']:
        if bytes_val < 1024.0:
            return f"{bytes_val:.2f} {unit}"
        bytes_val /= 1024.0

def display_disk_space():
    disk_space_info = get_disk_space()
    root = tk.Tk()
    root.title("Disk Space Information")
    root.geometry("400x300")

    title_font = font.Font(family="Helvetica", size=16, weight="bold")
    space_font = font.Font(family="Helvetica", size=12)

    title_label = tk.Label(root, text="Disk Space Information", font=title_font)
    title_label.pack(pady=10)

    for drive_letter, space_info in disk_space_info.items():
        label_text = (
            f"Drive {drive_letter}:\n"
            f"Total space: {space_info['total']}\n"
            f"Used space: {space_info['used']}\n"
            f"Free space: {space_info['free']}\n"
        )
        space_label = tk.Label(root, text=label_text, font=space_font)
        space_label.pack()

    root.mainloop()

if __name__ == "__main__":
    display_disk_space()
