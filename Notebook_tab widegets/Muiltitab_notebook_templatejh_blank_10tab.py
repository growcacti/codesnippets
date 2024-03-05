import tkinter as tk
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x500")
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0)
f1 = ttk.Frame(notebook)
f2 = ttk.Frame(notebook)
notebook.add(f1, text="1")
notebook.add(f2, text="2")
f3 = ttk.Frame(notebook)
notebook.add(f3, text="3")
f4 = ttk.Frame(notebook)

f5 = ttk.Frame(notebook)

# Combobox creation


notebook.add(f5, text="5")
f6 = ttk.Frame(notebook)
notebook.add(f6, text="6")
f7 = ttk.Frame(notebook)
notebook.add(f7, text="7")
f8 = ttk.Frame(notebook)
notebook.add(f8, text="8")
f8 = ttk.Frame(notebook)
notebook.add(f8, text="8")
f9 = ttk.Frame(notebook)
notebook.add(f9, text="9")
f10 = ttk.Frame(notebook)
notebook.add(f10, text="10")
# disables the tab
# notebook.tab(0, state = 'disabled')
# entering and displaying multiple lines with the text widget


root.mainloop()
