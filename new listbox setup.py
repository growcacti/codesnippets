import os
import tkinter as tk
from tkinter import filedialog

class YourApp:  # Replace with your actual class name
    # ... initialization and other methods ...

    def setup_listbox(self):
        # Assuming self.lb is your ListBox
        self.lb.bind('<<ListboxSelect>>', self.on_select)

    def on_select(self, event=None):
        # Get selected index
        selected_index = self.lb.curselection()
        if selected_index:
            file_name = self.lb.get(selected_index[0])
            self.load_file_content(file_name)

    def load_file_content(self, file_name):
        try:
            with open(file_name, 'r') as file:
                content = file.read()
                self.textwidget.delete('1.0', tk.END)
                self.textwidget.insert(tk.END, content)
        except IOError as e:
            print(f"Error opening file: {e}")

    # ... other methods like makedirlist, newdirlist, listing ...

# rest of your class and application setup...
