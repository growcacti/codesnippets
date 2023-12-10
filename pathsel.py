import tkinter as tk
from tkinter import filedialog, ttk

def browse_path(entry):
    directory = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, directory)
    if directory not in path_list:
        path_list.append(directory)
        path_combo['values'] = path_list

def select_path(entry, event):
    entry.delete(0, tk.END)
    entry.insert(0, path_combo.get())

app = tk.Tk()
app.title("Path Selector")

path_list = []

# Origin path widgets
origin_label = tk.Label(app, text="Origin Path:")
origin_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
origin_entry = tk.Entry(app, width=50)
origin_entry.grid(row=0, column=1, padx=5, pady=5)
origin_browse_button = tk.Button(app, text="Browse", command=lambda: browse_path(origin_entry))
origin_browse_button.grid(row=0, column=2, padx=5, pady=5)

# Destination path widgets
destination_label = tk.Label(app, text="Destination Path:")
destination_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
destination_entry = tk.Entry(app, width=50)
destination_entry.grid(row=1, column=1, padx=5, pady=5)
destination_browse_button = tk.Button(app, text="Browse", command=lambda: browse_path(destination_entry))
destination_browse_button.grid(row=1, column=2, padx=5, pady=5)

# Dropdown for stored paths
path_combo = ttk.Combobox(app, values=path_list)
path_combo.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky=tk.EW)
path_combo.bind("<<ComboboxSelected>>", lambda event: select_path(origin_entry, event))

app.mainloop()
