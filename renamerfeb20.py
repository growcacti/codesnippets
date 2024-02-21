

import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import os
import threading
class FileRenamerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Renamer Tool")
        self.root.geometry("1200x800")  # Adjust size as needed
        self.file_type_vars = {}
        self.orig_file = None
        self.org_ext = None
        self.use_hex_var = tk.BooleanVar()
        self.prefix_var = tk.BooleanVar()
        self.create_menu()
        self.create_widgets()
        folder_path = os.path.join("my_folder", "my_subfolder")
        self.path = os.getcwd()
        self.start_number = 0
    def create_widgets(self):
      
        self.tree_label_frame = ttk.LabelFrame(self.root, text="Directory Structure")
        self.tree_label_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")   
        self.tree_frame = tk.Frame(self.tree_label_frame)  # Parent is now tree_label_frame
        self.tree_frame.pack(fill="both", expand=True)
        self.tree = ttk.Treeview(self.tree_frame, columns=("Directory Structure",), show="tree")
        self.tree.pack(side="left", fill="both", expand=True)
        self.tree_scroll = tk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.set_yscrollcommand=self.tree_scroll.set
        self.tree_scroll.pack(side="right", fill="y")
        self.list_frame = tk.Frame(self.root)
        self.list_frame.grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky="nsew")
        self.scrollbar = tk.Scrollbar(root)
        self.scrollbar.grid(row=1,column=2)
        self.loading_label = tk.Label(self.root, text="Loading...")
        self.loading_label.grid(row=2, column=0, sticky="ew", padx=10, pady=10)
        self.loading_label.grid_remove()  # Hide it initially

        # Create two listboxes
        self.original_file_list = tk.Listbox(self.list_frame,width=30,height=20, yscrollcommand=self.on_listbox_scroll)
        self.changed_file_list= tk.Listbox(self.list_frame,width=30,height=20, yscrollcommand=self.on_listbox_scroll)
        self.original_file_list.grid(row=1, column=0,rowspan = 2,columnspan =2)
        self.changed_file_list.grid(row=1, column=2,rowspan=2,columnspan =2)

        self.scrollbar.config(command=self.on_scroll)

        self.root.grid_columnconfigure(1, weight=2)      
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

               # Original File List Label
        self.label = tk.Label(self.list_frame, text="Original File Names").grid(row=0, column=1, padx=5, pady=(0,5), sticky="nw")
        
        
        # Changed File List Label
        self.label2 = tk.Label(self.list_frame, text="Changed File Names").grid(row=0, column=2, sticky="nw")
        
        self.tree.bind('<<TreeviewSelect>>', self.update_file_lists)      
        self.list_frame.grid_rowconfigure(0, weight=1)
        self.list_frame.grid_columnconfigure(0, weight=2)
        self.list_frame.grid_columnconfigure(1, weight=1)
        # In create_widgets method, after initializing other components
        self.rename_rule_frame = tk.Frame(self.root)
        self.rename_rule_frame.grid(row=10, column=1, padx=10, pady=5, sticky="ew")
        self.prefix_entry = tk.Entry(self.rename_rule_frame)
        self.prefix_entry.grid(row=5, column=2, padx=5, pady=5, sticky="ew")
        self.prefix_label = tk.Label(self.rename_rule_frame, text="Prefix:")
        self.prefix_label.grid(row=4, column=2, padx=5, pady=5, sticky="ew")
        self.suffix_entry = tk.Entry(self.rename_rule_frame)
        self.suffix_entry.grid(row=5, column=1, padx=5, pady=5, sticky="ew")
        self.suffix_label = tk.Label(self.rename_rule_frame, text="Suffix:")
        self.suffix_label.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
        self.new_ext_entry = tk.Entry(self.list_frame)
        self.new_ext_entry.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        self.new_ext_label = tk.Label(self.list_frame, text="New extension (optional):")
        self.new_ext_label.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        self.prefix_entry.bind("<KeyRelease>", lambda event: self.update_file_lists())
        self.suffix_entry.bind("<KeyRelease>", lambda event: self.update_file_lists())
        self.prefix_var = tk.BooleanVar(value=False)  # Default to not using prefix
        self.prefix_checkbutton = tk.Checkbutton(self.rename_rule_frame, text="Use Number Prefix", variable=self.prefix_var, command=self.update_file_lists)
        self.prefix_checkbutton.grid(row=6, column=1, sticky="w")
    def create_menu(self):
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Select Output Folder", command=self.select_output_folder)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Get Directories", command=self.get_dir)
        self.file_menu.add_command(label="Update Preview", command=self.update_file_lists)
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Renaming Options menu
        self.renaming_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.renaming_menu.add_checkbutton(label="Use Hexadecimal", variable=self.use_hex_var, command = lambda : self.update_file_lists())
        self.renaming_menu.add_checkbutton(label="Prefix Number", variable=self.prefix_var, command = lambda : self.update_file_lists())
        self.renaming_menu.add_command(label="Apply Rename", command=self.apply_rename)
        self.menu_bar.add_cascade(label="Renaming Options", menu=self.renaming_menu)


    def on_scroll(self,*args):
        # Update the yview of both listboxes when the scrollbar is moved
        self.original_file_list.yview(*args)
        self.changed_file_list.yview(*args)

    def on_listbox_scroll(self,*args):
        # Update the scrollbar and sync listboxes when either listbox is scrolled
        self.scrollbar.set(*args)
        self.on_scroll('moveto', args[0])




    def select_output_folder(self):
        self.output_folder = filedialog.askdirectory()
        if self.output_folder:
            print(f"Output folder selected: {self.output_folder}")

    def add_file_type(self):
       
        file_type = self.add_file_type_entry.get()
        if file_type and file_type.startswith(".") and file_type not in self.file_type_vars:
            # Assuming self.file_type_vars is a dictionary to track the file types
            human_readable = f"{file_type.upper()} files ({file_type})"
            var = tk.IntVar()
            check = tk.Checkbutton(self.list_frame, text=human_readable, variable=var)
            check.grid(sticky='w')
            self.file_type_vars[file_type] = var
            self.add_file_type_entry.delete(0, tk.END)


    def get_dir(self):
        self.path = filedialog.askdirectory()
        self.populate_treeview_th(self.path)

    def populate_treeview_th(self, path):
        self.path = path
        def target():
            self.populate_treeview(self.path)  # Call the existing method
            self.root.after(0, self.loading_label.grid_remove)  # Schedule label hide on main thread
        
        self.loading_label.grid()  # Show loading label
        threading.Thread(target=target).start()


    def populate_treeview(self, root_path="."):
        self.loading_label.grid()  # Show the loading label
        self.tree.delete(*self.tree.get_children())  # Clear existing items

        try:
            # List all entries in the directory
            for entry in os.listdir(root_path):
                entry_path = os.path.join(root_path, entry)
            # Check if the entry is a directory
                if os.path.isdir(entry_path):
                    self.tree.insert('', 'end', text=entry, values=(entry_path,), open=False)
        except Exception as e:
            print(f"Error loading directory contents: {e}")


        self.loading_label.grid_remove()  # Hide the label after loading
    def insert_treeview_items(self, path):
        for entry in os.listdir(path):
            entry_path = os.path.join(path, entry)
            if os.path.isdir(entry_path):
                node = self.tree.insert('end', text=entry, open=False)
                self.insert_treeview_items(node, entry_path)
                self.insert_treeview_items(path)
                self.loading_label.grid_remove()  
        
            
    def show_feedback(self, message, title="Info", type="info"):
        if type == "error":
            messagebox.showerror(title, message)
        elif type == "warning":
            messagebox.showwarning(title, message)
        else:
            messagebox.showinfo(title, message)

    def select_output_folder(self):
        self.output_folder = filedialog.askdirectory()
        if not self.output_folder:
            return  # User cancelled the dialog
        print(f"Selected output folder: {self.output_folder}")

        # Check if the directory exists; if not, offer to create it
        if not os.path.exists(self.output_folder):
            if messagebox.askyesno("Create Directory", "Directory does not exist. Create it?"):
                os.makedirs(self.output_folder, exist_ok=True)
                messagebox.showinfo("Directory Created", f"Created the directory: {self.output_folder}")
            else:
                return
               
  
    def apply_rename(self, output_folder=None):
        
        selected_directory = self.tree.focus()  # Get selected directory for rename operation
        path = self.tree.item(selected_directory, 'text')
        if not self.validate_input():
            return  # Halt operation if validation fails
        # Allow user to select output folder if not specified
        if not output_folder:
            output_folder = filedialog.askdirectory()

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        self.start_number = 1  # Starting number for renaming
        for file in os.listdir(path):
            original_path = os.path.join(path, file)
            new_name = self.generate_newfilename(file, self.start_number, use_hex=False, prefix=False)
            new_path = os.path.join(output_folder, new_name)

            try:
                os.rename(original_path, new_path)
                self.show_success_message()
                print(f"Renamed '{original_path}' to '{new_path}'")
                self.start_number += 1  # Increment the number for the next file
            except OSError as e:
                 show_error_message(f"Error renaming file {file}: {e}")
                 print(f"Error renaming file {file}: {e}")

    def update_file_lists(self, event=None):
        selected_item = self.tree.focus()  # Get selected directory
        path = self.tree.item(selected_item, 'text')

        self.original_file_list.delete(0, tk.END)  # Clear ListBoxes
        self.changed_file_list.delete(0, tk.END)

        if not os.path.isdir(path):  # Ensure the path is a directory
            return

        for file in os.listdir(path):
            self.original_file_list.insert(tk.END, file)
            newfilename = self.generate_newfilename(file)
            self.changed_file_list.insert(tk.END, newfilename)

   


        self.start_number = 1  # Starting number for the prefix
        for index in range(self.original_file_list.size()):
            original_filename = self.original_file_list.get(index)
            new_filename = self.generate_newfilename(original_filename, self.start_number)
            self.changed_file_list.insert(tk.END, new_filename)
            self.start_number += 1  # Increment for the next file if prefix is used

    def generate_newfilename(self, original_filename, start_number = None):
        prefix = f"{self.start_number}_" if self.start_number is not None else "" 
        new_filename = f"{prefix}{original_filename}"
        prefix = self.prefix_entry.get()
        suffix = self.suffix_entry.get()
        new_ext = self.new_ext_entry.get() if self.new_ext_entry.get() else os.path.splitext(original_filename)[1]
        base_name = os.path.splitext(original_filename)[0]
        newfilename = f"{prefix}{base_name}{suffix}{new_ext}"
        return newfilename




    def show_success_message(self, message="Operation successful"):
            """Displays a success message to the user."""
            messagebox.showinfo("Success", message)

    def show_error_message(self, message="An error occurred"):
        """Displays an error message to the user."""
        messagebox.showerror("Error", message)


    
 
               
if __name__ == "__main__":
    root = tk.Tk()
    app = FileRenamerApp(root)
    root.mainloop()


