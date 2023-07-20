
from files_visualizer import FileSystemTree, visualize, filedialog
import tkinter as tk
from tkinter import filedialog
import os
import math
import pygame
import sys
from tkinter import filedialog
from typing import List, Tuple, Optional
from free_space import DiskSpaceGUI

def open_directory():
    directory = filedialog.askdirectory()
    if directory:
        file_tree = FileSystemTree(directory)
        visualize(file_tree)

def check_free():
    disk_space_gui = DiskSpaceGUI()
    disk_space_gui.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("File System Manager")
    root.geometry("400x100")

    visualize_button = tk.Button(root, text="Visualize", command=open_directory)
    visualize_button.pack(pady=10)

    free_button = tk.Button(root,text="Show free space", command=check_free)
    free_button.pack(pady=10)

    root.mainloop()
