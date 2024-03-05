import tkinter as tk
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x500")
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0)
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
notebook.add(frame1, text="1")
notebook.add(frame2, text="2")
frame3 = ttk.Frame(notebook)
notebook.add(frame3, text="3")
frame4 = ttk.Frame(notebook)

frame5 = ttk.Frame(notebook)

# Combobox creation


notebook.add(frame5, text="5")
frame6 = ttk.Frame(notebook)
notebook.add(frame6, text="6")
frame7 = ttk.Frame(notebook)
notebook.add(frame7, text="7")
frame8 = ttk.Frame(notebook)
notebook.add(frame8, text="8")
frame8 = ttk.Frame(notebook)
notebook.add(frame8, text="8")
frame9 = ttk.Frame(notebook)
notebook.add(frame9, text="9")
frame10 = ttk.Frame(notebook)
notebook.add(frame10, text="10")
# disables the tab
# notebook.tab(0, state = 'disabled')
# entering and displaying multiple lines with the text widget


root.mainloop()
