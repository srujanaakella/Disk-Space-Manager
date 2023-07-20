import os
import shutil
import tkinter as tk
from tkinter import filedialog

class FileDeletionGUI(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("File Deletion GUI")
        self.geometry("500x300")

        self.label = tk.Label(self, text="Select the file or directory to delete:")
        self.label.pack(pady=10)

        self.path_var = tk.StringVar()
        self.path_entry = tk.Entry(self, textvariable=self.path_var, width=40)
        self.path_entry.pack(pady=5)

        self.browse_button = tk.Button(self, text="Browse", command=self.select_file_or_directory)
        self.browse_button.pack(pady=5)

        self.delete_button = tk.Button(self, text="Delete", command=self.delete_file_or_directory)
        self.delete_button.pack(pady=10)

        self.result_label = tk.Label(self, text="", font=("Helvetica", 12))
        self.result_label.pack()

    def select_file_or_directory(self):
        path = filedialog.askopenfilename()
        if path:
            self.path_var.set(path)

    def delete_file_or_directory(self):
        path = self.path_var.get()
        if not path:
            self.result_label.config(text="Please select a file or directory.", fg="red")
            return

        try:
            if os.path.isdir(path):
                shutil.rmtree(path)
                self.result_label.config(text=f"Directory '{path}' and all its contents deleted successfully.", fg="green")
            else:
                os.remove(path)
                self.result_label.config(text=f"File '{path}' deleted successfully.", fg="green")
        except Exception as e:
            self.result_label.config(text=f"Error deleting '{path}': {e}", fg="red")
