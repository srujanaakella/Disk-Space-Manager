import os
import shutil
import tkinter as tk
from tkinter import filedialog

class FileDeletionGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Deletion GUI")
        self.geometry("400x200")

        self.label = tk.Label(self, text="Select the directory to delete:")
        self.label.pack(pady=10)

        self.directory_var = tk.StringVar()
        self.directory_entry = tk.Entry(self, textvariable=self.directory_var, width=30)
        self.directory_entry.pack(pady=5)

        self.browse_button = tk.Button(self, text="Browse", command=self.select_directory)
        self.browse_button.pack(pady=5)

        self.delete_button = tk.Button(self, text="Delete Directory", command=self.delete_directory)
        self.delete_button.pack(pady=10)

        self.result_label = tk.Label(self, text="", font=("Helvetica", 12))
        self.result_label.pack()

    def select_directory(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            self.directory_var.set(directory_path)

    def delete_directory(self):
        directory = self.directory_var.get()
        if not directory:
            self.result_label.config(text="Please select a directory.", fg="red")
            return

        try:
            shutil.rmtree(directory)
            self.result_label.config(text=f"Directory '{directory}' and all its contents deleted successfully.", fg="green")
        except Exception as e:
            self.result_label.config(text=f"Error deleting directory '{directory}': {e}", fg="red")

