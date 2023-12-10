import tkinter as tk
from tkinter import filedialog, ttk

class PathSelector:
    def __init__(self, root):
        self.root = root
        root.title("Path Selector")
        self.path_list = []

        # Origin path widgets
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

        # Dropdown for stored paths
        self.path_combo = ttk.Combobox(root, values=self.path_list)
        self.path_combo.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky=tk.EW)
        self.path_combo.bind("<<ComboboxSelected>>", lambda event: self.select_path(self.origin_entry, event))

    def browse_path(self, entry):
        directory = filedialog.askdirectory()
        if directory:
            entry.delete(0, tk.END)
            entry.insert(0, directory)
            if directory not in self.path_list:
                self.path_list.append(directory)
                self.path_combo['values'] = self.path_list

    def select_path(self, entry, event):
        entry.delete(0, tk.END)
        entry.insert(0, self.path_combo.get())

# Create the main application window
root = tk.Tk()
app = PathSelector(root)
root.mainloop()
