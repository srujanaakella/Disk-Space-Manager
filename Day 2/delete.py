
import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from send2trash import send2trash

class FileDeletionGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Deletion GUI")
        self.geometry("500x250")

        self.label = tk.Label(self, text="Select the file or directory to delete:")
        self.label.pack(pady=10)

        self.path_var = tk.StringVar()
        self.path_entry = tk.Entry(self, textvariable=self.path_var, width=40)
        self.path_entry.pack(pady=5)

        self.browse_button = tk.Button(self, text="Browse", command=self.select_file_or_directory)
        self.browse_button.pack(pady=5)

        self.permanent_delete_var = tk.IntVar()
        self.permanent_delete_checkbox = tk.Checkbutton(self, text="Delete Permanently", variable=self.permanent_delete_var)
        self.permanent_delete_checkbox.pack(pady=5)

        #self.is_directory_var = tk.IntVar()
        #self.directory_checkbox = tk.Checkbutton(self, text="Delete Directory", variable=self.is_directory_var)
        #self.directory_checkbox.pack(pady=5)

        self.delete_button = tk.Button(self, text="Delete", command=self.delete_file_or_directory)
        self.delete_button.pack(pady=10)

    def select_file_or_directory(self):
        path = filedialog.askopenfilename()
        if path:
            self.path_var.set(path)

    def delete_file_or_directory(self):
        path = self.path_var.get()
        if not path:
            messagebox.showerror("Error", "Please select a file or directory.")
            return

        if not os.path.exists(path):
            messagebox.showerror("Error", "The selected file or directory does not exist.")
            return

        permanent_delete = self.permanent_delete_var.get() == 1
        is_directory = self.is_directory_var.get() == 1

        try:
            if not permanent_delete:
                send2trash(path)
                messagebox.showinfo("Deleted", f"'{path}' moved to Recycle Bin.")
            else:
                if is_directory:
                    shutil.rmtree(path)
                else:
                    os.remove(path)
                messagebox.showinfo("Deleted", f"'{path}' deleted permanently.")
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting '{path}': {e}")

