from __future__ import annotations
import os
import math
import pygame
import sys
import tkinter as tk
from tkinter import filedialog
from typing import List, Tuple, Optional

DIMENSIONS = (1024, 576)

FILE_EXTENSIONS = {
    "Audio": [".aif", ".cda", ".mid", ".midi", ".mp3", ".mpa", ".ogg", ".wav", ".wma", ".wpl"],
    "Executable": [".apk", ".bat", ".bin", ".cgi", ".pl", ".com", ".exe", ".gadget", ".jar", ".wsf"],
    "Image": [".ai", ".bmp", ".gif", ".ico", ".jpeg", ".jpg", ".png", ".ps", ".psd", ".svg", ".tif", ".tiff"],
    "Presentation": [".key", ".odp", ".pps", ".ppt", ".pptx"],
    "Spreadsheet": [".ods", ".xlr", ".xls", ".xlsx"],
    "Video": [".3g2", ".3gp", ".avi", ".flv", ".h264", ".m4v", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg", ".rm", ".swf", ".vob", ".wmv"],
    "Document": [".doc", ".docx", ".pdf", ".rtf", ".tex", ".txt", ".wks", ".wps", ".wpd"],
    "Source Code": [".c", ".class", ".cpp", ".cs", ".h", ".py", ".java", ".sh", ".swift", ".vb", ".v", ".css", ".js", ".php", ".htm", ".html"]
}

FILE_COLORS = {
    "Executable": (51, 107, 135),
    "Source Code": (144, 175, 197),
    "Video": (255, 66, 14),
    "Image": (204, 56, 32),
    "Audio": (249, 136, 102),
    "Document": (89, 130, 52),
    "Presentation": (128, 189, 158),
    "Spreadsheet": (137, 218, 89),
    "Other File": (125, 68, 39)
}

LARGE_SIZE_THRESHOLD = 100000000  # 100 MB

def is_large_file_or_directory(item_path: str) -> bool:
    if os.path.isfile(item_path):
        file_size = os.path.getsize(item_path)
    else:
        file_size = sum(os.path.getsize(os.path.join(dirpath, filename)) for dirpath, _, filenames in os.walk(item_path) for filename in filenames)

    return file_size > LARGE_SIZE_THRESHOLD

def get_file_type(file_path: str) -> str:
    _, extension = os.path.splitext(file_path)
    for category, extensions in FILE_EXTENSIONS.items():
        if extension.lower() in extensions:
            return category    
        
def show_large_status(item_path: str) -> None:
    is_large = is_large_file_or_directory(item_path)
    status = "large" if is_large else "not large"
    status_label.config(text=f"The selected item is {status}.")   

def select_directory_or_file():
    item_path = filedialog.askopenfilename()
    if not item_path:
        item_path = filedialog.askdirectory()

    if item_path:
        file_type = get_file_type(item_path)
        is_large = is_large_file_or_directory(item_path)

        file_info_label.config(text=f"Selected item: {item_path}\nFile type: {file_type}")
        show_large_status(item_path)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("File System Visualizer")
    root.geometry("400x200")

    label = tk.Label(root, text="Select Directory or File:")
    label.pack(pady=5)

    select_button = tk.Button(root, text="Select", command=select_directory_or_file)
    select_button.pack(pady=5)

    file_info_label = tk.Label(root, text="", wraplength=350)
    file_info_label.pack(pady=5)

    status_label = tk.Label(root, text="")
    status_label.pack(pady=5)

    root.mainloop()