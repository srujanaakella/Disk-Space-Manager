import psutil
import tkinter as tk
from tkinter import ttk

class DiskSpaceGUI(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Free Disk Space")
        self.geometry("400x150")

        self.disk_space_label = tk.Label(self, text="Free Disk Space:", font=("Arial", 14, "bold"))
        self.disk_space_label.pack(pady=10)

        style = ttk.Style(self)
        style.theme_use("default")
        style.configure("DiskSpace.Horizontal.TProgressbar", thickness=20, troughcolor="#EAEAEA", background="#1ABC9C", troughrelief="flat", bordercolor="#1ABC9C")
        self.progressbar = ttk.Progressbar(self, orient="horizontal", mode="determinate", length=300, style="DiskSpace.Horizontal.TProgressbar")
        self.progressbar.pack()

        self.update_disk_space()

    def update_disk_space(self):
        try:
            usage = psutil.disk_usage("/")
            total_space = usage.total
            free_space = usage.free
            used_space = total_space - free_space
            free_space_percentage = (free_space / total_space) * 100

            self.disk_space_label.config(text=f"Free Disk Space: {free_space_percentage:.2f}%")
            self.progressbar["value"] = free_space_percentage
        except Exception as e:
            self.disk_space_label.config(text="Error: Unable to retrieve disk space information")

        self.after(5000, self.update_disk_space)  # Update every 5 seconds
