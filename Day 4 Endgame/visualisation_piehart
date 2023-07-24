from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
import matplotlib.pyplot as plt
import customtkinter as ctk
from tkinter import ttk
import tkinter as tk
from math import *
import os
import time

FILE_EXTENSIONS = {
    "Audio": [".aif", ".cda", ".mid", ".midi", ".mp3", ".mpa", ".ogg", ".wav", ".wma", ".wpl"],
    "Executable": [".apk", ".bat", ".bin", ".cgi", ".pl", ".com", ".exe", ".gadget", ".jar", ".wsf"],
    "Image": [".ai", ".bmp", ".gif", ".ico", ".jpeg", ".jpg", ".png", ".ps", ".psd", ".svg", ".tif", ".tiff"],
    "Presentation": [".key", ".odp", ".pps", ".ppt", ".pptx"],
    "Spreadsheet": [".ods", ".xlr", ".xls", ".xlsx"],
    "Video": [".3g2", ".3gp", ".avi", ".flv", ".h264", ".m4v", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg", ".rm", ".swf", ".vob", ".wmv"],
    "Document": [".doc", ".docx", ".pdf", ".rtf", ".tex", ".txt", ".wks", ".wps", ".wpd"],
    "Source Code": [".c", ".class", ".cpp", ".cs", ".h", ".py", ".java", ".sh", ".swift", ".vb", ".v", ".css", ".js", ".php", ".htm", ".html"]
}

FILE_COLORS= {

    "Executable": (0,0,1),
    "Source Code": (0,1,1),
    "Video": (1, 1, 0),
    "Image": (1,0,0),
    "Audio": (1, 0.75, 0.8),
    "Document": (0,1,0),
    "Presentation": (1,0.5,0),
    "Spreadsheet": (0,0.5,0),
    "Other File": (0.5,0,0.5)

}

class DiskSpaceVisualizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Disk Space Visualizer")
        self.root.geometry("1500x1500")

        self.main_frame = tk.Frame(self.root, background= "lightblue")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.directory_path = tk.StringVar()
        self.file_sizes = {}
        self.fig, self.ax = plt.subplots(figsize = (20,10))  # Create a Figure and Axes objects

        self.create_widgets()

    def get_directory_path(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            self.directory_path.set(directory_path)
            self.calculate_file_sizes(directory_path)

    def calculate_file_sizes(self, directory_path):
        start_time = time.time()
        self.file_sizes = {file_type: 0 for file_type in FILE_EXTENSIONS}
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_extension = os.path.splitext(file)[1].lower()
                for file_type, extensions in FILE_EXTENSIONS.items():
                    if file_extension in extensions:
                        self.file_sizes[file_type] += os.path.getsize(os.path.join(root, file))
                        break

        self.update_pie_chart()

        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time
        print(f"Time taken to run: {elapsed_time:.4f} seconds")

    def update_pie_chart(self):
        labels = []
        sizes = []
        colors = []
        total_size = 0
        for file_type, size in self.file_sizes.items():
            if size > 0:
                labels.append(file_type)
                sizes.append(size)
                colors.append(FILE_COLORS.get(file_type, FILE_COLORS["Other File"]))
                total_size += size

        self.ax.clear() 
        wedges, texts, autotexts = self.ax.pie(sizes, colors=colors, autopct='', startangle=90)
        self.ax.axis('equal')
        title_font = {'family': 'Montserrat', 'size': 16}

        self.ax.set_title("File Type Distribution")


        legend_labels = [f"{label} - {size/(1024**2):.2f} MB" for label, size in zip(labels, sizes)]
        self.ax.legend(legend_labels, loc="lower right", bbox_to_anchor=(1, 0.5), prop={'size': 8})

        self.canvas.draw()


    def create_widgets(self):
        directory_frame = ttk.Frame(self.root)
        directory_frame.pack(pady=10)

        ttk.Label(directory_frame, text="Select Directory:", font = ("Montserrat", 13)).pack(side=tk.LEFT)
        ttk.Entry(directory_frame, textvariable=self.directory_path, width=50, state="readonly").pack(side=tk.LEFT)
        ctk.CTkButton(directory_frame, text="Browse", command=self.get_directory_path).pack(side=tk.LEFT)

        self.pie_frame = ttk.Frame(self.root)
        self.pie_frame.pack(pady=20)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.pie_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()


# if __name__ == "__main__":
#     root = tk.Toplevel()
#     root.title("Disk Space Visualizer")
#     root.geometry("1500x1500")

#     visualizer = DiskSpaceVisualizerGUI(root)
#     root.mainloop()
