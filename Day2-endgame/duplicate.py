# import os
# import hashlib
# import tkinter as tk
# from tkinter import filedialog, messagebox

# def get_file_hash(file_path, block_size=65536):
#     hasher = hashlib.sha256()
#     with open(file_path, "rb") as file:
#         while True:
#             data = file.read(block_size)
#             if not data:
#                 break
#             hasher.update(data)
#     return hasher.hexdigest()

# def find_duplicate_files(directory):
#     file_hashes = {}
#     duplicate_files = []

#     for dirpath, _, filenames in os.walk(directory):
#         for filename in filenames:
#             file_path = os.path.join(dirpath, filename)
#             file_hash = get_file_hash(file_path)
#             if file_hash in file_hashes:
#                 duplicate_files.append((os.path.basename(file_hashes[file_hash]), file_hashes[file_hash]))
#                 duplicate_files.append((os.path.basename(file_path), file_path))
#             else:
#                 file_hashes[file_hash] = file_path

#     return duplicate_files

# def delete_file(file_path):
#     try:
#         if os.path.exists(file_path):
#             os.remove(file_path)
#             return True
#         else:
#             return False
#     except Exception as e:
#         return False

# class DuplicateFilesGUI(tk.Toplevel):
#     def __init__(self):
#         super().__init__()
#         self.title("Duplicate Files Finder")
#         self.geometry("800x600")

#         self.label = tk.Label(self, text="Select a directory to find duplicate files:")
#         self.label.pack(pady=10)

#         self.directory_var = tk.StringVar()
#         self.directory_entry = tk.Entry(self, textvariable=self.directory_var, width=40)
#         self.directory_entry.pack(pady=5)

#         self.browse_button = tk.Button(self, text="Browse", command=self.select_directory)
#         self.browse_button.pack(pady=5)

#         self.find_button = tk.Button(self, text="Find Duplicate Files", command=self.find_duplicates)
#         self.find_button.pack(pady=10)

#         self.result_frame = tk.Frame(self)
#         self.result_frame.pack()

#         self.result_text = tk.Text(self.result_frame, wrap="word", width=60, height=15)
#         self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#         self.scrollbar = tk.Scrollbar(self.result_frame, command=self.result_text.yview)
#         self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
#         self.result_text.config(yscrollcommand=self.scrollbar.set)

#         self.delete_button = tk.Button(self, text="Delete Selected", command=self.delete_selected_duplicates)
#         self.delete_button.pack(pady=5)

#         self.duplicate_pairs = []
#         self.checkboxes = []

#     def select_directory(self):
#         selected_directory = filedialog.askdirectory()
#         if selected_directory:
#             self.directory_var.set(selected_directory)

#     def find_duplicates(self):
#         directory = self.directory_var.get()
#         if not directory:
#             messagebox.showerror("Error", "Please select a directory.")
#             return

#         if not os.path.isdir(directory):
#             messagebox.showerror("Error", "Invalid directory path.")
#             return

#         self.result_text.delete(1.0, tk.END)
#         self.duplicate_pairs = find_duplicate_files(directory)

#         if not self.duplicate_pairs:
#             self.result_text.insert(tk.END, "No duplicate files found.")
#         else:
#             self.checkboxes = []
#             for i, (file1, file2) in enumerate(self.duplicate_pairs, start=1):
#                 var = tk.IntVar()
#                 checkbox = tk.Checkbutton(self.result_text, text=f"{file1} -- {file2}", variable=var, onvalue=1, offvalue=0)
#                 checkbox.pack(anchor=tk.W)
#                 self.checkboxes.append((var, file1, file2))

#     def delete_selected_duplicates(self):
#         selected_indices = [i for i, (var, _, _) in enumerate(self.checkboxes) if var.get() == 1]

#         if selected_indices:
#             confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete the selected duplicates?")
#             if confirm:
#                 for index in selected_indices:
#                     file_to_delete = self.duplicate_pairs[index][0]
#                     full_path_to_delete = self.duplicate_pairs[index][1]
#                     if delete_file(full_path_to_delete):
#                         self.result_text.insert(tk.END, f"Deleted: {file_to_delete}\n")
#                     else:
#                         self.result_text.insert(tk.END, f"Error: Unable to delete {file_to_delete}\n")

#                 self.find_duplicates()  # Refresh the duplicate list

#                 # Remove checkboxes from the result text
#                 for checkbox in self.result_text.winfo_children():
#                     checkbox.pack_forget()

# # if __name__ == "__main__":
# #     duplicate_files_gui = DuplicateFilesGUI()
# #     duplicate_files_gui.mainloop()


import os
import hashlib
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

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
                duplicate_files.append((os.path.basename(file_hashes[file_hash]), os.path.basename(file_path)))
            else:
                file_hashes[file_hash] = file_path

    return duplicate_files

def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        else:
            return False
    except Exception as e:
        return False

class DuplicateFilesGUI(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Duplicate Files Finder")
        self.geometry("800x600")

        self.label = tk.Label(self, text="Select a directory to find duplicate files:")
        self.label.pack(pady=10)

        self.directory_var = tk.StringVar()
        self.directory_entry = tk.Entry(self, textvariable=self.directory_var, width=40)
        self.directory_entry.pack(pady=5)

        self.browse_button = tk.Button(self, text="Browse", command=self.select_directory)
        self.browse_button.pack(pady=5)

        self.find_button = tk.Button(self, text="Find Duplicate Files", command=self.find_duplicates)
        self.find_button.pack(pady=10)

        self.result_frame = tk.Frame(self)
        self.result_frame.pack()

        self.result_text = tk.Text(self.result_frame, wrap="word", width=60, height=15)
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.result_frame, command=self.result_text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.config(yscrollcommand=self.scrollbar.set)

        self.delete_button = tk.Button(self, text="Delete Selected", command=self.delete_selected_duplicates)
        self.delete_button.pack(pady=5)

        self.duplicate_pairs = []
        self.checkboxes = []

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

        self.result_text.delete(1.0, tk.END)
        self.duplicate_pairs = find_duplicate_files(directory)

        if not self.duplicate_pairs:
            self.result_text.insert(tk.END, "No duplicate files found.")
        else:
            self.checkboxes = []
            for i, (file1, file2) in enumerate(self.duplicate_pairs, start=1):
                var = tk.IntVar()
                checkbox = tk.Checkbutton(self.result_text, text=f"{file1} -- {file2}", variable=var, onvalue=1, offvalue=0)
                checkbox.pack(anchor=tk.W)
                self.checkboxes.append((var, file1, file2))

    def delete_selected_duplicates(self):
        selected_indices = [i for i, (var, _, _) in enumerate(self.checkboxes) if var.get() == 1]

        if selected_indices:
            confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete the selected duplicates?")
            if confirm:
                directory = self.directory_var.get()
                for index in selected_indices:
                    file_to_delete = self.duplicate_pairs[index][0]
                    full_path_to_delete = os.path.join(directory, file_to_delete)
                    if delete_file(full_path_to_delete):
                        self.result_text.insert(tk.END, f"Deleted: {file_to_delete}\n")
                    else:
                        self.result_text.insert(tk.END, f"Error: Unable to delete {file_to_delete}\n")

                # Re-scan the directory for duplicates after deletion
                self.find_duplicates()

                # Remove checkboxes from the result text
                for checkbox in self.result_text.winfo_children():
                    checkbox.destroy()


    