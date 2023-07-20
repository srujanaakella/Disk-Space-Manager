
from files_visualizer import FileSystemTree, visualize, filedialog
import tkinter as tk
from tkinter import filedialog
import os
import math
import pygame
import sys
from tkinter import filedialog
from typing import List, Tuple, Optional

def open_directory():
    directory = filedialog.askdirectory()
    if directory:
        file_tree = FileSystemTree(directory)
        visualize(file_tree)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("File System Visualizer")
    root.geometry("400x100")

    visualize_button = tk.Button(root, text="Visualize", command=open_directory)
    visualize_button.pack(pady=10)

    root.mainloop()