import os
import math
import tkinter as tk
from tkinter import filedialog, messagebox, IntVar
from typing import List, Tuple
import shutil

class FileVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File System Visualizer")
        self.root.geometry("400x400")

        self.label = tk.Label(root, text="Select Directory:")
        self.label.pack(pady=5)

        self.select_button = tk.Button(root, text="Select", command=self.select_directory_and_show_large_files)
        self.select_button.pack(pady=5)

        self.file_info_label = tk.Label(root, text="", wraplength=350)
        self.file_info_label.pack(pady=5)

        self.status_label = tk.Label(root, text="")
        self.status_label.pack(pady=5)

    def get_files_sorted_by_size_and_extension(self, directory: str, threshold_mb: int = 100) -> List[Tuple[str, int]]:
        files_and_sizes = []
        threshold_bytes = threshold_mb * 1024 * 1024  

        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)
                if file_size >= threshold_bytes:
                    files_and_sizes.append((filename, file_size))

        files_and_sizes.sort(key=lambda x: (-x[1], os.path.splitext(x[0])[1]))
        return files_and_sizes

    def delete_selected_files(self, selected_files: List[str], directory: str, permanent_delete: bool) -> int:
        total_cleared_space = 0
        for filename in selected_files:
            file_path = os.path.join(directory, filename)
            try:
                file_size = os.path.getsize(file_path)
                if permanent_delete:
                    os.remove(file_path)
                else:
                    self.move_to_recycle_bin(file_path)
                total_cleared_space += file_size
            except Exception as e:
                messagebox.showerror("Error", f"Error deleting file {filename}: {e}")
        return total_cleared_space

    def move_to_recycle_bin(self, file_path: str):
        try:
            # On macOS, use shutil.move to move the file to the Trash
            if os.name == 'posix':
                shutil.move(file_path, os.path.join('~', '.Trash', os.path.basename(file_path)))
        except Exception as e:
            raise Exception(f"Error moving file {file_path} to the recycle bin: {e}")

    def select_directory_and_show_large_files(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            self.file_info_label.config(text=f"Selected directory: {directory_path}")
            self.directory_path = directory_path

            large_files = self.get_files_sorted_by_size_and_extension(directory_path, threshold_mb=100)
            if large_files:
                status = "\n".join(f"{file}: {size} bytes" for file, size in large_files)
                self.status_label.config(text=status)

                # Add Checkbox for file selection
                self.selected_files_var = []
                self.selected_files_checkboxes = []
                for file, _ in large_files:
                    var = IntVar()
                    checkbox = tk.Checkbutton(self.root, text=file, variable=var)
                    self.selected_files_var.append(var)
                    self.selected_files_checkboxes.append((file, checkbox))
                    checkbox.pack(anchor="w")

                delete_button = tk.Button(self.root, text="Delete Selected", command=self.delete_selected_and_show_status)
                delete_button.pack(pady=5)
            else:
                self.status_label.config(text="No large files (>= 100 MB) found in the directory.")

    def delete_selected_and_show_status(self):
        selected_files = [file for (file, _), var in zip(self.selected_files_checkboxes, self.selected_files_var) if var.get() == 1]
        if selected_files:
            permanent_delete = messagebox.askyesno("Delete Permanently", "Do you want to delete the selected files permanently?")
            total_cleared_space = self.delete_selected_files(selected_files, self.directory_path, permanent_delete)
            messagebox.showinfo("Deleted", f"Selected files have been deleted.\nTotal space cleared: {self.format_bytes(total_cleared_space)}")
            self.select_directory_and_show_large_files()  # Refresh the file list after deletion
        else:
            messagebox.showinfo("No Files Selected", "Please select files to delete.")

    @staticmethod
    def format_bytes(size: int) -> str:
        power = 2**10
        n = 0
        power_labels = {0: '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
        while size > power:
            size /= power
            n += 1
        return f"{size:.2f} {power_labels[n]}B"

if __name__ == "__main__":
    root = tk.Tk()
    app = FileVisualizerApp(root)
    root.mainloop()
