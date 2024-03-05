import tkinter as tk

from tkinter import *

from tkinter import ttk

import os, sys, subprocess

from tkinter.filedialog import askopenfilename, asksaveasfilename

root = Tk()

root.geometry("500x500")

notebook = ttk.Notebook(root)


notebook.grid(row=0, column=0)

frame1 = ttk.Frame(notebook)


def open_file():

    """Open a file for editing."""

    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:

        return

    text1.delete(1.0, tk.END)

    with open(filepath, "r") as input_file:

        text = input_file.read()

        text1.insert(tk.END, text)


def save_file():

    filepath = (
        asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("Python", "py"), ("All Files", "*.*")],
        ),
    )

    if not filepath:

        return

    with open(filepath, "w") as output_file:

        text = text1.get(1.0, tk.END)

        output_file.write(text)


frame1.rowconfigure(0, minsize=800, weight=1)

frame1.columnconfigure(1, minsize=800, weight=1)


fr_buttons = tk.Frame(frame1, relief=tk.RAISED, bd=2)

btn_open = tk.Button(fr_buttons, text="Open", command=open_file)

btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)


btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

btn_save.grid(row=1, column=0, sticky="ew", padx=5)


fr_buttons.grid(row=0, column=0, sticky="ns")

text1 = tk.Text(frame1)

text1.grid(row=0, column=1, sticky="nsew")

frame2 = ttk.Frame(notebook)

notebook.add(frame1, text="1")

notebook.add(frame2, text="2")


##fr_buttons2 = tk.Frame(frame2, relief=tk.RAISED, bd=2)

##fr_buttons2.grid(row=0, column=0, sticky='ns')

##btn_save = tk.Button(fr_buttons2, text='Save As...', command=save_file)

##btn_open = tk.Button(fr_buttons2, text='Open others', command=op)

##btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)

##btn_save.grid(row=1, column=0, sticky='ew', padx=5)


frame2.rowconfigure(0, minsize=800, weight=1)

frame2.columnconfigure(1, minsize=800, weight=1)


text2 = tk.Text(frame2)

text2.grid(row=0, column=1, sticky="nsew")


f3 = ttk.Frame(notebook)

notebook.add(f3, text="3")


text3 = tk.Text(f3, height=250, width=100, bg="wheat")

text3.insert("1.0", tk.END)

text3.grid(row=0, column=4, rowspan=25, columnspan=10)

f4 = ttk.Frame(notebook)

notebook.add(f4, text="4")

f5 = ttk.Frame(notebook)


notebook.add(f5, text="5")

f6 = ttk.Frame(notebook)

notebook.add(f6, text="6")

f7 = ttk.Frame(notebook)

notebook.add(f7, text="7")

f8 = ttk.Frame(notebook)

notebook.add(f8, text="8")

f9 = ttk.Frame(notebook)

notebook.add(f9, text="9")

f10 = ttk.Frame(notebook)

notebook.add(f10, text="10")

f11 = ttk.Frame(notebook)

notebook.add(f11, text="11")

text10 = tk.Text(f10, height=250, width=100, bg="wheat")

text10.insert("1.0", tk.END)

text10.grid(row=0, column=4, rowspan=25, columnspan=10)


text4 = tk.Text(f4, height=250, width=300, bg="wheat")

text4.insert("1.0", tk.END)


text4.grid(row=0, column=4, rowspan=25, columnspan=10)

text5 = tk.Text(f5, height=250, width=300, bg="white")

text5.insert("1.0", tk.END)

text5.grid(row=0, column=4, rowspan=25, columnspan=10)

text6 = tk.Text(f6, height=250, width=100, bg="white")

text6.insert("1.0", tk.END)

text6.grid(row=0, column=4, rowspan=25, columnspan=10)

text7 = tk.Text(f7, height=250, width=100, bg="light blue")

text7.insert("1.0", tk.END)

text7.grid(row=0, column=4, rowspan=25, columnspan=10)

text8 = tk.Text(f8, height=250, width=100, bg="pink")

text8.insert("1.0", tk.END)

text8.grid(row=0, column=4, rowspan=25, columnspan=10)

text9 = tk.Text(f9, height=250, width=100, bg="light green")

text9.insert("1.0", tk.END)

text9.grid(row=0, column=4, rowspan=25, columnspan=10)


# disables the tab

# notebook.tab(0, state = 'disabled')

# entering and displaying multiple lines with the text widget


top = tk.Toplevel()

top.geometry("600x400")

fr1 = tk.Frame(top)

fr1.grid(row=1, column=0, rowspan=20, columnspan=7)


btn_open2 = tk.Button(fr1, text="Open2", command=lambda: op(text2))

btn_open2.grid(row=5, column=2, sticky="ew", padx=5, pady=5)


btn_open3 = tk.Button(fr1, text="Open3", command=lambda: op(text3))

btn_open3.grid(row=7, column=1, sticky="ew", padx=5, pady=5)

btn_open4 = tk.Button(fr1, text="Open4", command=lambda: op(text4))

btn_open4.grid(row=8, column=2, sticky="ew", padx=5, pady=5)

btn_open5 = tk.Button(fr1, text="Open5", command=lambda: op(text5))

btn_open5.grid(row=9, column=1, sticky="ew", padx=5, pady=5)

btn_open6 = tk.Button(fr1, text="Open6", command=lambda: op(text6))

btn_open6.grid(row=10, column=2, sticky="ew", padx=5, pady=5)

btn_open7 = tk.Button(fr1, text="Open7", command=lambda: op(text7))

btn_open7.grid(row=11, column=1, sticky="ew", padx=5, pady=5)

btn_open8 = tk.Button(fr1, text="Open8", command=lambda: op(text8))

btn_open8.grid(row=12, column=2, sticky="ew", padx=5, pady=5)

btn_open9 = tk.Button(fr1, text="Open9", command=lambda: op(text9))

btn_open9.grid(row=13, column=1, sticky="ew", padx=5, pady=5)

btn_open10 = tk.Button(fr1, text="Open10", command=lambda: op(text10))

btn_open10.grid(row=14, column=2, sticky="ew", padx=5, pady=5)


btn_sav3 = tk.Button(fr1, text="save3", command=lambda: sa(text3))

btn_sav3.grid(row=7, column=3, sticky="ew", padx=5, pady=5)

btn_sav4 = tk.Button(fr1, text="Save4", command=lambda: sa(text4))

btn_sav4.grid(row=8, column=3, sticky="ew", padx=5, pady=5)

btn_sav5 = tk.Button(fr1, text="Save5", command=lambda: sa(text5))

btn_sav5.grid(row=9, column=3, sticky="ew", padx=5, pady=5)

btn_sav6 = tk.Button(fr1, text="Save6", command=lambda: sa(text6))

btn_sav6.grid(row=10, column=3, sticky="ew", padx=5, pady=5)

btn_sav7 = tk.Button(fr1, text="Save7", command=lambda: sa(text7))

btn_sav7.grid(row=11, column=3, sticky="ew", padx=5, pady=5)

btn_sav8 = tk.Button(fr1, text="Save8", command=lambda: sa(text8))

btn_sav8.grid(row=12, column=3, sticky="ew", padx=5, pady=5)

btn_sav9 = tk.Button(fr1, text="Save9", command=lambda: sa(text9))

btn_sav9.grid(row=13, column=3, sticky="ew", padx=5, pady=5)

btn_sav10 = tk.Button(fr1, text="Save10", command=lambda: sa(text10))

btn_sav10.grid(row=14, column=3, sticky="ew", padx=5, pady=5)


def op(w=text10):

    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("Python", "py"), ("All Files", "*.*")]
    )

    if not filepath:

        return

    w.delete(1.0, tk.END)

    with open(filepath, "r") as input_file:

        text = input_file.read()

        w.insert(tk.END, text)


def sa(s=text10):

    ss = s.get(1.0, tk.END)

    filepath = asksaveasfilename(
        filetypes=[("Text Files", "*.txt"), ("Python", "py"), ("All Files", "*.*")]
    )

    if not filepath:

        return

    with open(filepath, "w") as ff:

        ff.write(ss)


root.mainloop()
