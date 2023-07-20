import psutil
import tkinter as tk
from tkinter import font

def get_disk_space():
    drives = psutil.disk_partitions(all=True)
    disk_space_info = {}

    for drive in drives:
        drive_letter = drive.device.split(":")[0].upper()
        disk_usage = psutil.disk_usage(drive.mountpoint)
        total_space = disk_usage.total
        used_space = disk_usage.used
        free_space = disk_usage.free
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
    drives = list(disk_space_info.keys())

    root = tk.Tk()
    root.title("Disk Space Information")
    root.geometry("600x400")

    title_font = font.Font(family="Helvetica", size=16, weight="bold")
    space_font = font.Font(family="Helvetica", size=12)

    title_label = tk.Label(root, text="Disk Space Information", font=title_font)
    title_label.pack(pady=10)

    for drive in drives:
        total_space = disk_space_info[drive]["total"]
        used_space = disk_space_info[drive]["used"]
        free_space = disk_space_info[drive]["free"]

        frame = tk.Frame(root)
        frame.pack(pady=5)

        label_drive = tk.Label(frame, text=f"Drive {drive}:", font=space_font)
        label_drive.pack(side=tk.LEFT)

        canvas = tk.Canvas(frame, width=300, height=30)
        canvas.pack(side=tk.LEFT)

        total_width = total_space
        used_percentage = (used_space / total_space) * 100
        used_width = (total_width / 100) * used_percentage

        canvas.create_rectangle(0, 0, total_width / 1024, 30, fill='blue')
        canvas.create_rectangle(0, 0, used_width / 1024, 30, fill='green')

        label_used_percentage = tk.Label(frame, text=f"Used: {used_percentage:.1f}%", font=space_font)
        label_used_percentage.pack(side=tk.LEFT, padx=10)

        label_total = tk.Label(frame, text=f"Total: {_format_bytes(total_space)}", font=space_font)
        label_total.pack(side=tk.LEFT, padx=10)

        label_used = tk.Label(frame, text=f"Used: {_format_bytes(used_space)}", font=space_font)
        label_used.pack(side=tk.LEFT, padx=10)

        label_free = tk.Label(frame, text=f"Free: {_format_bytes(free_space)}", font=space_font)
        label_free.pack(side=tk.LEFT, padx=10)

    root.mainloop()

if __name__ == "__main__":
    display_disk_space()
