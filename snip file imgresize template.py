import tkinter as tk
from tkinter import filedialog, simpledialog
from PIL import Image
import os



def multi_img_file_resizer(parent):
    infostr =""" the small app will resize every image in a folder to the same percentage,
    an example input is 0.30 is 30%"""
    def resize_images(input_folder, resize_factor):
        output_folder = os.path.join(input_folder, 'resized_output')
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for file in os.listdir(input_folder):
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(input_folder, file)
                try:
                    with Image.open(img_path) as img:
                        # Resizing the image
                        new_size = tuple(int(dim * resize_factor) for dim in img.size)
                        resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
                        # Saving the resized image
                        resized_img.save(os.path.join(output_folder, file))
                        print(f"Resized and saved: {file}")
                except Exception as e:
                    print(f"Error processing {file}: {e}")

    def select_folder():
        folder_selected = askdirectory()
        if folder_selected:
            resize_factor = simpledialog.askfloat("Resize Factor", "Enter resize factor (e.g., 0.8 for 80%):", minvalue=0.1, maxvalue=1.0)
            if resize_factor:
                resize_images(folder_selected, resize_factor)

    
    select_button = tk.Button(parent, text="Select Folder and Resize Images", command=select_folder)
    select_button.grid(row=8, column=1)
