import re

# Example text
text = "This is a sample text with 'a specific phrase' to find, and some more text."

# Pattern to find text within single quotes
pattern_quotes = r"'(.*?)'"

# Pattern to find a specific word, e.g., "specific"
pattern_word = r"\bspecific\b"

# Pattern for a step search, finding two words in sequence with any characters in between
pattern_step_search = r"sample.*?phrase"

# Finding text within quotes
matches_quotes = re.findall(pattern_quotes, text)
print("Text within quotes:", matches_quotes)

# Finding a specific word
matches_word = re.findall(pattern_word, text)
print("Occurrences of the word 'specific':", matches_word)

# Performing a step search
matches_step = re.findall(pattern_step_search, text)
print("Step search result:", matches_step)
import tkinter as tk
from tkinter import ttk
import re

# Initialize main window
root = tk.Tk()
root.title("Regex Search Tool")

# Layout configuration
root.geometry("600x400")

# Entry widgets, Text widget, and Buttons
text_entry_label = tk.Label(root, text="Enter Text:")
text_entry_label.pack()
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack()

pattern_entry_label = tk.Label(root, text="Enter Regex Pattern:")
pattern_entry_label.pack()
pattern_entry = tk.Entry(root)
pattern_entry.pack()

search_button = tk.Button(root, text="Search", command=lambda: perform_search())
search_button.pack()

result_text = tk.Text(root, height=10, width=50)
result_text.pack()

# Function to perform search
def perform_search():
    # Clear previous results
    result_text.delete('1.0', tk.END)
    input_text = text_entry.get("1.0", tk.END)
    pattern = pattern_entry.get()
    try:
        matches = re.finditer(pattern, input_text)
        match_positions = []
        for match in matches:
            start, end = match.span()
            match_positions.append((start, end))
            result_text.insert(tk.END, f"Match found: {match.group()} at position {start}-{end}\n")
        # Highlight matches in the text
        for start, end in match_positions:
            result_text.tag_add("highlight", f"1.0+{start}c", f"1.0+{end}c")
            result_text.tag_config("highlight", background="yellow")
    except re.error as e:
        result_text.insert(tk.END, f"Regex Error: {str(e)}")

root.mainloop()



import tkinter as tk
from tkinter import ttk
import re

# Function to handle the search logic
def perform_search():
    pattern = pattern_entry.get()
    text = text_input.get("1.0", tk.END)
    search_type = search_type_combobox.get()
    result_display.delete("1.0", tk.END)  # Clear previous results

    try:
        if search_type == "Find All":
            matches = re.findall(pattern, text)
            result_display.insert(tk.END, "\n".join(matches))
        elif search_type == "Match":
            match = re.match(pattern, text)
            if match:
                result_display.insert(tk.END, match.group(0))
        # Additional search types can be implemented here
    except re.error as e:
        result_display.insert(tk.END, f"Regex Error: {str(e)}")

# Function to clear all inputs and results
def clear_all():
    pattern_entry.delete(0, tk.END)
    text_input.delete("1.0", tk.END)
    result_display.delete("1.0", tk.END)

# Initialize Tkinter window
root = tk.Tk()
root.title("Regex Search Tool")
root.geometry("600x400")

# GUI elements
pattern_entry = tk.Entry(root, width=50)
pattern_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Label(root, text="Regex Pattern:").grid(row=0, column=0)

text_input = tk.Text(root, height=10, width=50)
text_input.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

search_types = ["Find All", "Match", "Search Between"]
search_type_combobox = ttk.Combobox(root, values=search_types, state="readonly")
search_type_combobox.current(0)
search_type_combobox.grid(row=2, column=1)

tk.Button(root, text="Search", command=perform_search).grid(row=3, column=0, pady=5)
tk.Button(root, text="Clear", command=clear_all).grid(row=3, column=1, pady=5)

result_display = tk.Text(root, height=10, width=50)
result_display.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
# Additional Functionality within the perform_search function

    elif search_type == "Search Between":
        # Example pattern for searching text between quotes: '"(.*?)"'
        matches = re.findall(f'{pattern}', text)
        result_display.insert(tk.END, "\n".join(matches))
    # Step search functionality can be implemented as an extension
import tkinter as tk
from tkinter import ttk
import re

# Function to handle the search logic
def perform_search():
    pattern = pattern_entry.get()
    text = text_input.get("1.0", tk.END)
    search_type = search_type_combobox.get()
    result_display.delete("1.0", tk.END)  # Clear previous results

    try:
        if search_type == "Find All":
            matches = re.findall(pattern, text)
            result_display.insert(tk.END, "\n".join(matches))
        elif search_type == "Match":
            match = re.match(pattern, text)
            if match:
                result_display.insert(tk.END, match.group(0))
        # Additional search types can be implemented here
    except re.error as e:
        result_display.insert(tk.END, f"Regex Error: {str(e)}")

# Function to clear all inputs and results
def clear_all():
    pattern_entry.delete(0, tk.END)
    text_input.delete("1.0", tk.END)
    result_display.delete("1.0", tk.END)

# Initialize Tkinter window
root = tk.Tk()
root.title("Regex Search Tool")
root.geometry("600x400")

# GUI elements
pattern_entry = tk.Entry(root, width=50)
pattern_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Label(root, text="Regex Pattern:").grid(row=0, column=0)

text_input = tk.Text(root, height=10, width=50)
text_input.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

search_types = ["Find All", "Match", "Search Between"]
search_type_combobox = ttk.Combobox(root, values=search_types, state="readonly")
search_type_combobox.current(0)
search_type_combobox.grid(row=2, column=1)

tk.Button(root, text="Search", command=perform_search).grid(row=3, column=0, pady=5)
tk.Button(root, text="Clear", command=clear_all).grid(row=3, column=1, pady=5)

result_display = tk.Text(root, height=10, width=50)
result_display.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

roimport tkinter as tk
from tkinter import messagebox

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Processing App")
        self.root.geometry("400x200")  # Example size, adjust as needed
        self.create_widgets()

    def create_widgets(self):
        # Input Field Label
        self.input_label = tk.Label(self.root, text="Enter Data:")
        self.input_label.pack()

        # Input Field
        self.input_entry = tk.Entry(self.root)
        self.input_entry.pack()

        # Submit Button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.process_input)
        self.submit_button.pack()

        # Output Display Area
        self.output_label = tk.Label(self.root, text="")
        self.output_label.pack()

    def process_input(self):
        # Placeholder for processing function integration
        input_data = self.input_entry.get()
        # For now, just display input data back to user
        self.output_label.config(text=f"Input Received: {input_data}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
ot.mainloop()
