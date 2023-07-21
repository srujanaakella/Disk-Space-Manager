import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import fastparquet as fp
import shutil

def browse_directory():
    global input_directory
    input_directory = filedialog.askdirectory()
    entry_directory.delete(0, tk.END)
    entry_directory.insert(tk.END, input_directory)

def convert_to_orc():
    try:
        input_dir = entry_directory.get()
        if not os.path.exists(input_dir):
            raise ValueError("Invalid input directory path")

        output_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
        os.makedirs(output_dir, exist_ok=True)

        for root, _, files in os.walk(input_dir):
            for filename in files:
                if filename.lower().endswith('.csv'):
                    file_path = os.path.join(root, filename)
                    data = pd.read_csv(file_path)
                    output_file = os.path.join(output_dir, os.path.splitext(filename)[0] + '.orc')
                    fp.write(output_file, data)

        status_label.config(text="Conversion successful! CSV files saved in Downloads.")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("CSV to ORC Converter")

# Create and place widgets
label_directory = tk.Label(root, text="Select Directory:")
label_directory.pack(pady=10)

entry_directory = tk.Entry(root, width=50)
entry_directory.pack(pady=5)

button_browse = tk.Button(root, text="Browse", command=browse_directory)
button_browse.pack(pady=5)

button_convert = tk.Button(root, text="Convert to ORC", command=convert_to_orc)
button_convert.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack(pady=5)

root.mainloop()
