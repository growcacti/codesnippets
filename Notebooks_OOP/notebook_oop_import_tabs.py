import tkinter as tk
from tkinter import ttk

from tab1 import *
from tab2 import *    

class MainApplication(tk.Frame):
  def __init__(self, parent, *args, **kwargs):
    tk.Frame.__init__(self, parent, *args, **kwargs)

    notebook = ttk.Notebook(parent)

    Tab1frame = Tab1(notebook)
    Tab2frame = Tab2(notebook)

    notebook.add(Typ1frame, text='TAB1')
    notebook.add(Typ2frame, text='TAB2')
    notebook.pack()

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
