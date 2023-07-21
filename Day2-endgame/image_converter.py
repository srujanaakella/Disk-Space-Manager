from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog


class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Format Converter")
        self.root.geometry("400x200")

        self.input_label = tk.Label(root, text="Select Input Directory:")
        self.input_label.pack(pady=10)

        self.input_entry = tk.Entry(root, width=40)
        self.input_entry.pack()

        self.browse_input_button = tk.Button(root, text="Browse", command=self.browse_input_directory)
        self.browse_input_button.pack(pady=5)

        self.output_label = tk.Label(root, text="Select Output Directory:")
        self.output_label.pack(pady=10)

        self.output_entry = tk.Entry(root, width=40)
        self.output_entry.pack()

        self.browse_output_button = tk.Button(root, text="Browse", command=self.browse_output_directory)
        self.browse_output_button.pack(pady=5)

        self.convert_button = tk.Button(root, text="Convert to JPG", command=self.convert_to_jpg)
        self.convert_button.pack(pady=20)

    def browse_input_directory(self):
        input_directory = filedialog.askdirectory()
        if input_directory:
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(tk.END, input_directory)

    def browse_output_directory(self):
        output_directory = filedialog.askdirectory()
        if output_directory:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(tk.END, output_directory)

    def convert_to_jpg(self):
        input_dir = self.input_entry.get()
        output_dir = self.output_entry.get()

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for filename in os.listdir(input_dir):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".jpg")

            try:
                with Image.open(input_path) as img:
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    img.save(output_path, format='JPEG')
            except Exception as e:
                print(f"Error converting {filename}: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConverterApp(root)
    root.mainloop()
