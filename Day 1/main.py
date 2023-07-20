from files_visualizer import FileSystemTree, visualize, filedialog
import tkinter as tk
import customtkinter as ctk
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
from disk_space import DiskSpaceVisualizer

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

def disk_space():
    disk_space_visualisation = DiskSpaceVisualizer()
    disk_space_visualisation.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("File System Manager")
    root.geometry("500x450")
    root.configure(bg="lightblue")

    header_label = tk.Label(root, text="Disk Space Manager", font=("Montserrat", 25, "bold"), bg="lightblue")
    header_label.pack(pady=10)

    content_label = tk.Label(root, text="A GUI application of all functions to manage your disk space.", 
                             bg="lightblue", font=("Montserrat", 13,))
    content_label.pack(pady=10)

    free_button = ctk.CTkButton(root,text="Display Disk Space", command=disk_space, font= ("Montserrat", 13))
    free_button.pack(padx=10,pady=10)

    visualize_button = ctk.CTkButton(root, text="Visualize Files", command=open_directory, font= ("Montserrat", 13))
    visualize_button.pack(padx=10,pady=10)

    duplicate_button=ctk.CTkButton(root,text="Find Duplicate Files",command=check_dup, font= ("Montserrat", 13))
    duplicate_button.pack(padx=10,pady=10)

    delete_button=ctk.CTkButton(root,text="Delete Files",command=file_del, font= ("Montserrat", 13))
    delete_button.pack(padx=10,pady=10)

    sametype_button=ctk.CTkButton(root,text="Find File Type",command=same_file, font= ("Montserrat", 13))
    sametype_button.pack(pady=10)

    root.mainloop()
