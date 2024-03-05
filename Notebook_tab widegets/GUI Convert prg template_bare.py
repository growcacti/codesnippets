import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import math

r = tk.Tk()
r.geometry("1200x800")
r.title("APPS")
notebook = ttk.Notebook(r)
notebook.grid(row=0, column=0)
f0 = ttk.Frame(notebook)
notebook.add(f0, text="MAIN")
f1 = ttk.Frame(notebook)
f2 = ttk.Frame(notebook)
notebook.add(f1, text="1")
notebook.add(f2, text="2")

f3 = ttk.Frame(notebook)
notebook.add(f3, text="3")
f4 = ttk.Frame(notebook, height=100, width=100)
notebook.add(f4, text="4")
f5 = ttk.Frame(notebook)
notebook.add(f5, text=" 5 ")
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


def c():

    pass


btn1 = tk.Button(f1, text="", command=c)
btn1.grid(row=4, column=1)


btn2 = tk.Button(f1, text="Send txt", command=c)
btn2.grid(row=5, column=1)


btn4 = tk.Button(f2, text="Calculate", command=c)
btn4.grid(row=4, column=1)


btn6 = tk.Button(f2, text="Send txt", command=c)
btn6.grid(row=5, column=1)

text = tk.Text(f3, width=300, height=200)
text.grid(row=6, column=1)


btn22 = tk.Button(f3, text="Calculate", command=c)
btn22.grid(row=4, column=1)


if __name__ == "__main__":
    r.mainloop()
