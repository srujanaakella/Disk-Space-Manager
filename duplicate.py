import os
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox

def get_file_hash(file_path, block_size=65536):
    hasher = hashlib.sha256()
    with open(file_path, "rb") as file:
        while True:
            data = file.read(block_size)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

def find_duplicate_files(directory):
    file_hashes = {}
    duplicate_files = []

    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_hash = get_file_hash(file_path)
            if file_hash in file_hashes:
                duplicate_files.append((file_path, file_hashes[file_hash]))
            else:
                file_hashes[file_hash] = file_path

    return duplicate_files

class DuplicateFilesGUI(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Duplicate Files Finder")
        self.geometry("500x300")

        self.label = tk.Label(self, text="Select a directory to find duplicate files:")
        self.label.pack(pady=10)

        self.directory_var = tk.StringVar()
        self.directory_entry = tk.Entry(self, textvariable=self.directory_var, width=40)
        self.directory_entry.pack(pady=5)

        self.browse_button = tk.Button(self, text="Browse", command=self.select_directory)
        self.browse_button.pack(pady=5)

        self.find_button = tk.Button(self, text="Find Duplicate Files", command=self.find_duplicates)
        self.find_button.pack(pady=10)

        self.result_text = tk.Text(self, wrap="word", width=60, height=10)
        self.result_text.pack()

    def select_directory(self):
        selected_directory = filedialog.askdirectory()
        if selected_directory:
            self.directory_var.set(selected_directory)

    def find_duplicates(self):
        directory = self.directory_var.get()
        if not directory:
            messagebox.showerror("Error", "Please select a directory.")
            return

        if not os.path.isdir(directory):
            messagebox.showerror("Error", "Invalid directory path.")
            return

        duplicate_files = find_duplicate_files(directory)
        if not duplicate_files:
            self.result_text.insert(tk.END, "No duplicate files found.")
        else:
            self.result_text.insert(tk.END, "Duplicate files:\n")
            for file1, file2 in duplicate_files:
                self.result_text.insert(tk.END, f"{file1} -- {file2}\n")

if __name__ == "__main__":
    duplicate_files_gui = DuplicateFilesGUI()
    duplicate_files_gui.mainloop()
