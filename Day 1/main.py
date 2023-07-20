
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
from duplicate import DuplicateFilesGUI
from delete import FileDeletionGUI
from same_type import FileSelectorGUI

def open_directory():
    directory = filedialog.askdirectory()
    if directory:
        file_tree = FileSystemTree(directory)
        visualize(file_tree)

def check_free():
    disk_space_gui = DiskSpaceGUI()
    disk_space_gui.mainloop()

def check_dup():
    duplicate_files_gui = DuplicateFilesGUI()
    duplicate_files_gui.mainloop()

def file_del():
    del_disk=FileDeletionGUI()
    del_disk.mainloop()

def same_file():
    file_selector_gui = FileSelectorGUI()
    file_selector_gui.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("File System Manager")
    root.geometry("300x500")

    visualize_button = tk.Button(root, text="Visualize", command=open_directory)
    visualize_button.pack(padx=10,pady=10)

    free_button = tk.Button(root,text="Show free space", command=check_free)
    free_button.pack(padx=10,pady=10)

    duplicate_button=tk.Button(root,text="Duplicates",command=check_dup)
    duplicate_button.pack(padx=10,pady=10)

    delete_button=tk.Button(root,text="Delete",command=file_del)
    delete_button.pack(padx=10,pady=10)

    sametype_button=tk.Button(root,text="Similar Files",command=same_file)
    sametype_button.pack(pady=10)

    root.mainloop()
