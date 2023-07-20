from __future__ import annotations
import os
import math
import pygame
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
from typing import List, Tuple, Optional

# ... (Rest of the script remains unchanged)

def get_files_sorted_by_size_and_extension(directory: str, threshold_mb: int = 100) -> List[Tuple[str, int]]:
    files_and_sizes = []
    threshold_bytes = threshold_mb * 1024 * 1024  # Convert threshold to bytes

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            if file_size >= threshold_bytes:
                files_and_sizes.append((filename, file_size))

    # Sort the list of files by size (descending order) and then by extension (alphabetical order)
    files_and_sizes.sort(key=lambda x: (-x[1], os.path.splitext(x[0])[1]))
    return files_and_sizes

def select_directory_and_show_large_files():
    directory_path = filedialog.askdirectory()
    if directory_path:
        file_info_label.config(text=f"Selected directory: {directory_path}")

        large_files = get_files_sorted_by_size_and_extension(directory_path, threshold_mb=100)
        if large_files:
            status = "\n".join(f"{file}: {size} bytes" for file, size in large_files)
        else:
            status = "No large files (>= 100 MB) found in the directory."

        status_label.config(text=status)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("File System Visualizer")
    root.geometry("400x400")

    label = tk.Label(root, text="Select Directory:")
    label.pack(pady=5)

    select_button = tk.Button(root, text="Select", command=select_directory_and_show_large_files)
    select_button.pack(pady=5)

    file_info_label = tk.Label(root, text="", wraplength=350)
    file_info_label.pack(pady=5)

    status_label = tk.Label(root, text="")
    status_label.pack(pady=5)

    root.mainloop()
