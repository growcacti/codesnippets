import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory
import os
import datetime

def load_files(directory):
    for i in tree.get_children():
        tree.delete(i)
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            file_size = os.path.getsize(os.path.join(directory, file))
            file_mtime = os.path.getmtime(os.path.join(directory, file))
            file_date = datetime.datetime.fromtimestamp(file_mtime).strftime('%Y-%m-%d %H:%M:%S')
            file_type = os.path.splitext(file)[1] if os.path.splitext(file)[1] else 'None'
            tree.insert('', 'end', values=(file, file_type, file_size, file_date))

def select_directory():
    directory = askdirectory()
    if directory:  # Check if a directory was selected
        load_files(directory)

def sort_by(column, descending):
    data = [(tree.set(child, column), child) for child in tree.get_children('')]
    data.sort(reverse=descending)

    for i, item in enumerate(data):
        tree.move(item[1], '', i)

    tree.heading(column, command=lambda col=column: sort_by(col, not descending))

# Create the main window
root = tk.Tk()
root.title("File Explorer")

# Create the Treeview
tree = ttk.Treeview(root, columns=('Name', 'Type', 'Size', 'Date Modified'), show='headings')
tree.heading('Name', text='Name', command=lambda: sort_by('Name', False))
tree.heading('Type', text='Type', command=lambda: sort_by('Type', False))
tree.heading('Size', text='Size (bytes)', command=lambda: sort_by('Size', False))
tree.heading('Date Modified', text='Date Modified', command=lambda: sort_by('Date Modified', False))
tree.column('Name', width=150)
tree.column('Type', width=100)
tree.column('Size', width=100)
tree.column('Date Modified', width=150)
tree.pack(fill=tk.BOTH, expand=True)

# Button to choose directory
select_button = tk.Button(root, text="Select Directory", command=select_directory)
select_button.pack()

# Run the application
root.mainloop()
