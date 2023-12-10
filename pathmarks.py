import tkinter as tk
from tkinter import filedialog, ttk
import json
import os
import sys
import subprocess

class PathSelector:
    def __init__(self, root):
        self.root = root
        root.title("Path Selector")
        self.pathlist=[]
        self.origin_label = tk.Label(root, text="Origin Path:")
        self.origin_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.origin_entry = tk.Entry(root, width=50)
        self.origin_entry.grid(row=0, column=1, padx=5, pady=5)
        self.origin_browse_button = tk.Button(root, text="Browse", command=lambda: self.browse_path(self.origin_entry))
        self.origin_browse_button.grid(row=0, column=2, padx=5, pady=5)

        # Destination path widgets
        self.destination_label = tk.Label(root, text="Destination Path:")
        self.destination_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.destination_entry = tk.Entry(root, width=50)
        self.destination_entry.grid(row=1, column=1, padx=5, pady=5)
        self.destination_browse_button = tk.Button(root, text="Browse", command=lambda: self.browse_path(self.destination_entry))
        self.destination_browse_button.grid(row=1, column=2, padx=5, pady=5)
      
        self.mark = tk.Button(root, text="List Path", command=self.insert_path)
        self.mark.grid(row=11, column=2, padx=5, pady=5)
        # Listbox to display paths
        self.pathlb = tk.Listbox(root)
        self.pathlb.grid(row=10, column=0, padx=5, pady=5, sticky=tk.NSEW)
        self.pathlb.bind("<Double-1>", self.select_path)
        self.open_button = tk.Button(root, text="Open File", command=self.load_paths)
        self.open_button.grid(row=12, column=0, padx=5, pady=5)
        self.save_button = tk.Button(root, text="Save File", command=self.save_paths)
        self.save_button.grid(row=12, column=1, padx=5, pady=5)

        # Populate the lb
        self.update_lb()
        self.paths_file = "paths.json"  # File to store paths
        

        self.open_button = tk.Button(root, text="Open in File Manager", command=self.open_in_file_manager)
        self.open_button.grid(row=11, column=0, padx=5, pady=5)
        self.pathlb.bind("<Double-1>", lambda event: self.open_in_file_manager())

    def browse_path(self, entry):
        directory = filedialog.askdirectory()
        if directory:
            entry.delete(0, tk.END)
            entry.insert(0, directory)
            if directory not in self.pathlist:
                self.pathlist.append(directory)
           
                self.update_lb()
               

    def select_path(self, entry, event):
        entry.delete(0, tk.END)
        selection = self.pathlb.curselection()
        if selection:
            selected_path = self.pathlb.get(selection[0])
            self.output_entry.insert(0, selected_path)

    def save_paths(self):
         file_paths = filedialog.asksaveasfilename(defaultextension=".json")
         if not file_paths:
             print(f"Saved file: {file_path}")  # Example action
         if os.path.exists(self.paths_file):
             self.paths = self.pathlb.get(0, tk.END)
             with open(self.paths_file, 'w') as file:
                 json.dump(self.pathlist, file)

    def load_paths(self):
        file_paths = filedialog.askopenfilename(defaultextension=".json")
        if not file_paths:
            # Here you can add code to handle the opened file
            print(f"Opened file: {file_path}")  # Example action

        if os.path.exists(self.paths_file):
            with open(self.paths_file, 'r') as file:
                self.pathlb.insert(tk.END,  json.load(file))
                return json.load(file)
        return []

    def update_lb(self):
        self.pathlb.delete(0, tk.END)
        for path in self.pathlist:
            self.pathlb.insert(tk.END, path)

    def insert_path(self):
        if len(self.origin_entry.get()) > 0:
            self.pathlb.insert(tk.END, self.origin_entry.get())
        elif len(self.destination_entry.get()) > 0:
            self.pathlb.insert(tk.END, self.destination_entry.get())

    def open_in_file_manager(self):
        selection = self.pathlb.curselection()
        if selection:
            path = self.pathlb.get(selection[0])
            self.open_path(path)

    def open_path(self, path):
        if sys.platform == 'win32':
            os.startfile(path)
        elif sys.platform == 'darwin':  # macOS
            subprocess.run(['open', path])
        else:  # Linux and other OS
            subprocess.run(['xdg-open', path])
root = tk.Tk()
app = PathSelector(root)
root.mainloop()
