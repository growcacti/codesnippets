import os
import tkinter as tk
from tkinter import Listbox, Entry, Button, Label, Radiobutton, StringVar, Spinbox, Checkbutton, IntVar, filedialog

class FileRenamerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bulk File Renaming Tool")

        # Entry widget for directory path
        self.entry_label = Label(root, text="Directory Path:")
        self.entry_label.grid(row=0, column=0, columnspan=2)
        self.entry = Entry(root, width=40)
        self.entry.grid(row=0, column=2, columnspan=2)
      
        # Button to list files
        self.list_button = Button(root, text="List Files", command=self.list_files)
        self.list_button.grid(row=1, column=0, columnspan=2)
        self.browse_button = Button(root, text="Browse", command=self.browse_directory)
        self.browse_button.grid(row=1, column=2, columnspan=2)
        # Listbox to display original filenames
        self.original_file_listbox = Listbox(root, width=40, height=10)
        self.original_file_listbox.grid(row=2, column=0, columnspan=2)

        # Listbox to display renamed filenames
        self.renamed_file_listbox = Listbox(root, width=40, height=10)
        self.renamed_file_listbox.grid(row=2, column=2, columnspan=2)

        # Entry widget for specifying the new extension
        self.extension_label = Label(root, text="New Extension:")
        self.extension_label.grid(row=3, column=0, columnspan=2)
        self.extension_entry = Entry(root, width=10)
        self.extension_entry.grid(row=3, column=2, columnspan=2)
        self.extension_entry.insert(0, ".txt")  # Default extension

        # Spinbox for specifying characters to remove
        self.characters_label = Label(root, text="Characters to Remove:")
        self.characters_label.grid(row=4, column=0, columnspan=2)
        self.characters_spinbox = Spinbox(root, from_=0, to=100, width=5)
        self.characters_spinbox.grid(row=4, column=2, columnspan=2)

        # Entry widget for adding prefix/suffix
        self.prefix_suffix_label = Label(root, text="Prefix/Suffix:")
        self.prefix_suffix_label.grid(row=5, column=0, columnspan=2)
        self.prefix_suffix_entry = Entry(root, width=40)
        self.prefix_suffix_entry.grid(row=5, column=2, columnspan=2)

        # Radiobuttons for adding prefix/suffix
        self.add_option = StringVar()
        self.add_option.set("prefix")  # Default is prefix
        self.add_option_label = Label(root, text="Add as:")
        self.add_option_label.grid(row=6, column=0, columnspan=4)
        self.add_prefix_radio = Radiobutton(root, text="Prefix", variable=self.add_option, value="prefix")
        self.add_suffix_radio = Radiobutton(root, text="Suffix", variable=self.add_option, value="suffix")
        self.add_prefix_radio.grid(row=7, column=0)
        self.add_suffix_radio.grid(row=7, column=1)

        # Checkbutton for enumerating files
        self.enumerate_var = IntVar()
        self.enumerate_checkbox = Checkbutton(root, text="Enumerate Files", variable=self.enumerate_var)
        self.enumerate_checkbox.grid(row=8, column=0, columnspan=4)

        # Button to rename files
        self.rename_button = Button(root, text="Rename Files", command=self.rename_files)
        self.rename_button.grid(row=9, column=0, columnspan=4)

    def list_files(self):
        directory = self.entry.get()
        if os.path.exists(directory) and os.path.isdir(directory):
            files = os.listdir(directory)
            self.original_file_listbox.delete(0, tk.END)
            self.renamed_file_listbox.delete(0, tk.END)
            for file in files:
                self.original_file_listbox.insert(tk.END, file)
                self.renamed_file_listbox.insert(tk.END, file)
        else:
            self.original_file_listbox.delete(0, tk.END)
            self.renamed_file_listbox.delete(0, tk.END)
            self.original_file_listbox.insert(tk.END, "Directory does not exist")
    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, directory)
            self.original_file_listbox.delete(0, tk.END)
            self.renamed_file_listbox.delete(0, tk.END)
            if os.path.exists(directory) and os.path.isdir(directory):
                for file in os.listdir(directory):
                    self.original_file_listbox.insert(tk.END, file)
                    self.renamed_file_listbox.insert(tk.END, file)
            else:
                self.original_file_listbox.delete(0, tk.END)
                self.renamed_file_listbox.delete(0, tk.END)
                self.original_file_listbox.insert(tk.END, "Directory does not exist")


    def rename_files(self):
        directory = self.entry.get()
        new_extension = self.extension_entry.get()
        characters_to_remove = int(self.characters_spinbox.get())
        prefix_suffix = self.prefix_suffix_entry.get()
        add_option = self.add_option.get()
        enumerate_files = self.enumerate_var.get()

        if os.path.exists(directory) and os.path.isdir(directory):
            for i, old_name in enumerate(self.original_file_listbox.get(0, tk.END)):
                file_extension = os.path.splitext(old_name)[-1]
                base_name = os.path.splitext(old_name)[0]
                
                if enumerate_files:
                    new_name = f"{prefix_suffix}{i + 1}{new_extension}"
                else:
                    if add_option == "prefix":
                        new_name = f"{prefix_suffix}{base_name[characters_to_remove:]}{new_extension}"
                    else:  # add_option == "suffix"
                        new_name = f"{base_name[characters_to_remove:]}{prefix_suffix}{new_extension}"
                
                os.rename(os.path.join(directory, old_name), os.path.join(directory, new_name))
            self.list_files()
        else:
            self.original_file_listbox.delete(0, tk.END)
            self.renamed_file_listbox.delete(0, tk.END)
            self.original_file_listbox.insert(tk.END, "Directory does not exist")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileRenamerApp(root)
    root.mainloop()
