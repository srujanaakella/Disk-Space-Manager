import os
import tkinter as tk
from tkinter import filedialog, ttk

FILE_EXTENSIONS = {
    "Audio": [".aif", ".cda", ".mid", ".midi", ".mp3",
              ".mpa", ".ogg", ".wav", ".wma", ".wpl"],
    "Executable": [".apk", ".bat", ".bin", ".cgi", ".pl",
                   ".com", ".exe", ".gadget", ".jar", ".wsf"],
    "Image": [".ai", ".bmp", ".gif", ".ico", ".jpeg", ".jpg",
              ".png", ".ps", ".psd", ".svg", ".tif", ".tiff"],
    "Presentation": [".key", ".odp", ".pps", ".ppt", ".pptx"],
    "Spreadsheet": [".ods", ".xlr", ".xls", ".xlsx"],
    "Video": [".3g2", ".3gp", ".avi", ".flv", ".h264", ".m4v",
              ".mkv", ".mov", ".mp4", ".mpg", ".mpeg", ".rm",
              ".swf", ".vob", ".wmv"],
    "Document": [".doc", ".docx", ".pdf", ".rtf", ".tex",
                 ".txt", ".wks", ".wps", ".wpd"],
    "Source Code": [".c", ".class", ".cpp", ".cs", ".h", ".py",
                    ".java", ".sh", ".swift", ".vb", ".v",
                    ".css", ".js", ".php", ".htm", ".html"]
}

def select_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        directory_var.set(directory_path)

def display_files():
    directory_path = directory_var.get()
    file_type = file_type_var.get()

    if file_type not in FILE_EXTENSIONS:
        file_list.delete(0, tk.END)
        file_list.insert(tk.END, "Invalid file type.")
        total_space_label.config(text="Total Space: ")
        return

    extensions = FILE_EXTENSIONS[file_type]
    if not os.path.exists(directory_path):
        file_list.delete(0, tk.END)
        file_list.insert(tk.END, "Directory not found.")
        total_space_label.config(text="Total Space: ")
        return

    file_list.delete(0, tk.END)
    total_space = 0
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)
        if os.path.isfile(filepath) and os.path.splitext(filename)[1].lower() in extensions:
            file_list.insert(tk.END, filename)
            total_space += os.path.getsize(filepath)

    total_space_label.config(text=f"Total Space: {format_bytes(total_space)}")

def format_bytes(bytes_val):
    for unit in ['', 'KB', 'MB', 'GB', 'TB']:
        if bytes_val < 1024.0:
            return f"{bytes_val:.2f} {unit}"
        bytes_val /= 1024.0

if __name__ == "__main__":
    root = tk.Tk()
    root.title("File Selector")
    root.geometry("500x400")

    directory_frame = tk.Frame(root)
    directory_frame.pack(pady=10)

    directory_label = tk.Label(directory_frame, text="Select Directory:")
    directory_label.pack(side=tk.LEFT)

    directory_var = tk.StringVar()
    directory_entry = tk.Entry(directory_frame, textvariable=directory_var, width=30)
    directory_entry.pack(side=tk.LEFT)

    browse_button = tk.Button(directory_frame, text="Browse", command=select_directory)
    browse_button.pack(side=tk.LEFT)

    file_type_label = tk.Label(root, text="Select file type:")
    file_type_label.pack(pady=5)

    file_type_var = tk.StringVar()
    file_type_combobox = ttk.Combobox(root, textvariable=file_type_var, values=list(FILE_EXTENSIONS.keys()), state="readonly")
    file_type_combobox.pack()

    enter_button = tk.Button(root, text="Enter", command=display_files)
    enter_button.pack(pady=10)

    file_list = tk.Listbox(root, width=50, height=15)
    file_list.pack(pady=10)

    total_space_label = tk.Label(root, text="Total Space: ")
    total_space_label.pack()

    root.mainloop()
