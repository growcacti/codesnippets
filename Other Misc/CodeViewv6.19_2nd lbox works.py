#!/usr/bin/env python3
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import filedialog
from tkinter import Tk, Frame, Button, BOTH, SUNKEN
from tkinter import colorchooser
import os
import sys
import subprocess
import shutil
from PIL import Image, ImageTk
import runpy


# --------------------------------------------------------------------
# Functions and call backs
# --------------------------------------------------------------------


def run(event):
    x = lb.curselection()[0]
    file = lb.get(x)
    runpy.run_path(path_name=file)


def opensystem(event):

    x = lb.curselection()[0]

    file = lb.get(x)
    with open(file, "r") as file:
        file = file.read()
        text.delete("1.0", tk.END)
        text.insert(tk.END, file)

        return


def showcontent(x):

    lb.focus()
    x = lb.curselection()[0]
    file = lb.get(x)
    with open(file, "r") as file:
        file = file.read()
        text.delete("1.0", tk.END)
        text.insert(tk.END, file)

        return


#
# -----------------------------------------------------------------------------
# GUI Magic Starts Here
# ----------------------------------------------------------------------------

r = tk.Tk()
r.geometry("1850x1080")
r.title("GUI TEMPLATE")
notebook = ttk.Notebook(r)
notebook.grid(row=0, column=1)
f1 = ttk.Frame(r, width=1800, height=1000)
f1.grid(row=0, column=0)

# f1.columnconfigure(4, weight=3)
# f1.rowconfigure(10, weight=1)
notebook.add(f1, text="TAB1")


text = tk.Text(f1, height=60, width=150, bg="white")
text.insert("1.0", tk.END)
text.grid(row=0, column=3)


def runpyprg(event):

    file = lb.get(ANCHOR)
    runpy.run_path(path_name=file)

    return


scrollbar = tk.Scrollbar(f1)
scrollbar.grid(row=0, column=4, sticky="nswe")
scrollbar.config(command=text.yview)
lb = tk.Listbox(f1, bg="light blue", exportselection=False, selectmode=tk.MULTIPLE)
lb.grid(row=0, column=0, sticky="nswe")
lb.focus()
lb.configure(selectmode="")
flist = os.listdir()
for item in flist:
    lb.insert(tk.END, item)
lb.bind("<Double-Button-1>", run)
lb.bind("<<ListboxSelect>>", showcontent)
# lb.bind("<Double-Button-1>", opensystem)

# ---------------------------------------------------------------------
# Next Tab  TAB2 f2
# ---------------------------------------------------------------------
def cmdbtn():
    runpy.run_path(path_name="cmd_btn_console.py")


def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)


def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)


def clear():
    txt_edit.delete("1.0", tk.END)


def ggtxt():
    a = text.get("1.0", tk.END)
    txt_edit.insert(tk.END, a)


def newdirlist():

    path = filedialog.askdirectory()
    os.chdir(path)
    flist = os.listdir(path)
    lbox.delete(0, tk.END)
    for item in flist:

        lbox.insert(tk.END, item)
    return flist


f2 = ttk.Frame(r)
notebook.add(f2, text="TAB2")

txt_edit = tk.Text(f2, height=500, width=500)
fr_buttons = tk.Frame(f2, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_open.grid(row=1, column=0)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
btn_save.grid(row=2, column=0)
btn_clear = tk.Button(fr_buttons, text="Clear", command=clear)
btn_clear.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_grab = tk.Button(fr_buttons, text="Grab", command=ggtxt)
btn_grab.grid(row=4, column=0)
# btn_s.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")


f3 = ttk.Frame(r)
notebook.add(f3, text="TAB3")
canvas_width = 1800
canvas_height = 900
w = Canvas(f3, width=canvas_width, height=canvas_height)
w.grid(row=0, column=0)
# img = ImageTk.PhotoImage(Image.open("screen_locations.png"))
# w.create_image(10, 10, anchor=NW, image=img)

f4 = ttk.Frame(r)
notebook.add(f4, text="TAB4")


btn_open = tk.Button(fr_buttons, text="CMD BTN CONSOLE", command=cmdbtn)
btn_open.grid(row=1, column=0)


# btn1f3=tk.Button(f3, text='Button', command=command)
# btn1f3.grid(column=1, row=1)


f5 = ttk.Frame(r)
notebook.add(f5, text="TAB5")


def checkered(canvas, line_distance):

    canvas.create_line(10, 400, 1900, 400, fill="blue", width=4)

    canvas.create_line(750, 10, 750, 900, fill="green", width=4)
    canvas.create_line(50, 390, 50, 410, fill="blue", width=4)
    canvas.create_line(100, 390, 100, 410, fill="blue", width=4)
    canvas.create_line(150, 390, 150, 410, fill="blue", width=4)
    canvas.create_line(200, 390, 200, 410, fill="blue", width=4)
    canvas.create_line(250, 390, 250, 410, fill="blue", width=4)
    canvas.create_line(300, 390, 300, 410, fill="blue", width=4)
    canvas.create_line(350, 390, 350, 410, fill="blue", width=4)
    canvas.create_line(400, 390, 400, 410, fill="blue", width=4)
    canvas.create_line(450, 390, 450, 410, fill="blue", width=4)
    canvas.create_line(500, 390, 500, 410, fill="blue", width=4)
    canvas.create_line(550, 390, 550, 410, fill="blue", width=4)
    canvas.create_line(600, 390, 600, 410, fill="blue", width=4)
    canvas.create_line(650, 390, 650, 410, fill="blue", width=4)
    canvas.create_line(700, 390, 700, 410, fill="blue", width=4)
    canvas.create_line(750, 390, 750, 410, fill="blue", width=4)
    canvas.create_line(800, 390, 800, 410, fill="blue", width=4)
    canvas.create_line(850, 390, 850, 410, fill="blue", width=4)
    canvas.create_line(900, 390, 900, 410, fill="blue", width=4)
    canvas.create_line(950, 390, 950, 410, fill="blue", width=4)
    canvas.create_line(1000, 390, 1000, 410, fill="blue", width=4)
    canvas.create_line(1050, 390, 1050, 410, fill="blue", width=4)
    canvas.create_line(1100, 390, 1100, 410, fill="blue", width=4)
    canvas.create_line(1150, 390, 1150, 410, fill="blue", width=4)
    canvas.create_line(1200, 390, 1200, 410, fill="blue", width=4)
    canvas.create_line(1250, 390, 1250, 410, fill="blue", width=4)
    canvas.create_line(1300, 390, 1300, 410, fill="blue", width=4)
    canvas.create_line(1350, 390, 1350, 410, fill="blue", width=4)
    canvas.create_line(1400, 390, 1400, 410, fill="blue", width=4)
    canvas.create_line(1450, 390, 1450, 410, fill="blue", width=4)
    canvas.create_line(1500, 390, 1500, 410, fill="blue", width=4)
    canvas.create_line(1550, 390, 1550, 410, fill="blue", width=4)
    canvas.create_line(1600, 390, 1600, 410, fill="blue", width=4)
    canvas.create_line(1650, 390, 1650, 410, fill="blue", width=4)
    canvas.create_line(1700, 390, 1700, 410, fill="blue", width=4)
    canvas.create_line(1750, 390, 1750, 410, fill="blue", width=4)
    canvas.create_line(1800, 390, 1800, 410, fill="blue", width=4)

    canvas.create_line(740, 20, 760, 20, fill="blue", width=4)
    canvas.create_line(740, 30, 760, 30, fill="blue", width=4)
    canvas.create_line(740, 50, 760, 50, fill="blue", width=4)
    canvas.create_line(740, 100, 760, 100, fill="blue", width=4)
    canvas.create_line(740, 150, 760, 150, fill="blue", width=4)
    canvas.create_line(740, 200, 760, 200, fill="blue", width=4)
    canvas.create_line(740, 250, 760, 250, fill="blue", width=4)
    canvas.create_line(740, 300, 760, 300, fill="blue", width=4)
    canvas.create_line(740, 350, 760, 350, fill="blue", width=4)
    canvas.create_line(740, 400, 760, 400, fill="blue", width=4)
    canvas.create_line(740, 450, 760, 450, fill="blue", width=4)
    canvas.create_line(740, 500, 760, 500, fill="blue", width=4)
    canvas.create_line(740, 550, 760, 550, fill="blue", width=4)
    canvas.create_line(740, 600, 760, 600, fill="blue", width=4)
    canvas.create_line(740, 650, 760, 650, fill="blue", width=4)
    canvas.create_line(740, 700, 760, 700, fill="blue", width=4)
    canvas.create_line(740, 750, 760, 750, fill="blue", width=4)
    canvas.create_line(740, 800, 760, 800, fill="blue", width=4)
    canvas.create_line(740, 850, 760, 850, fill="blue", width=4)
    canvas.create_line(740, 900, 760, 900, fill="blue", width=4)
    canvas.create_line(740, 950, 760, 950, fill="blue", width=4)
    canvas.create_line(740, 1000, 760, 1000, fill="blue", width=4)

    # vertical lines at an interval of "line_distance" pixel
    for x in range(line_distance, canvas_width, line_distance):
        canvas.create_line(x, 0, x, canvas_height, fill="#476042")
    # horizontal lines at an interval of "line_distance" pixel
    for y in range(line_distance, canvas_height, line_distance):
        canvas.create_line(0, y, canvas_width, y, fill="#476042")


canvas_width = 1900
canvas_height = 900
canvas = Canvas(f5, width=canvas_width, height=canvas_height)
w.grid(row=0, column=0)


checkered(w, 10)


f6 = ttk.Frame(r)
notebook.add(f6, text="TAB6")
##
##
##
##text2 = tk.Text(f6, height=60, width=150, bg='white')
##text2.insert('1.0', tk.END)
##text2.grid(row=0, column=0)
text2 = tk.Text(f6, height=55, width=100, bg="white")
text2.insert("1.0", tk.END)
text2.grid(row=1, column=3)
lbox = tk.Listbox(f6, bg="light blue", exportselection=False, selectmode=tk.MULTIPLE)
lbox.grid(row=1, column=1, sticky="nswe")
lbox.focus()
lbox.configure(selectmode="")
btnf6 = tk.Button(f6, text="get dir", command=newdirlist)
btnf6.grid(row=0, column=0)
scrollbar2 = tk.Scrollbar(f6)
scrollbar2.grid(row=0, column=2, sticky="nswe")
scrollbar2.config(command=text.yview)
##lb2 = tk.Listbox(f6, bg="light blue", exportselection=False, selectmode=tk.MULTIPLE)
##lb2.grid(row=0, column=3, sticky="nswe")
##lb2.focus()
##lb2.configure(selectmode="")

# path = "home/jh/Desktop/Codeview_Project/ref/*.*"
# filepath = os.listdir(path)


def lboxfun(event):

    lbox.focus()
    lbox.configure(selectmode="")
    x1 = lbox.get(ANCHOR)


def showcontent2(x):

    lb.focus()
    x = lbox.curselection()[0]
    file = lbox.get(x)
    with open(file, "r") as file:
        file = file.read()
        text2.delete("1.0", tk.END)
        text2.insert(tk.END, file)
        lboxfun()
        return


def opensystem2(event):

    x = lbox.curselection()[0]

    file = lbox.get(x)
    with open(file, "r") as file:
        file = file.read()
        text2.delete("1.0", tk.END)
        text2.insert(tk.END, file)

        return


def op():
    path = "/home/jh/Desktop/Codeview_Project/ref/"
    dirs = os.listdir(path)

    # This would print all the files and directories
    for file in dirs:
        lbox.insert(tk.END, file)


##flist = os.listdir()
##for item in flist:
##    lbox.insert(tk.END, item)

##def refreshlist():
##
##    lbox.delete(0, END)
##    mylist = os.listdir("/home/jh/Desktop/Codeview_Project/")
##    for file in mylist:
##        lbox.insert(END, file)
##        return
##refreshlist()
# lb2.insert(tk.END, filepath)
lbox.bind("<<ListboxSelect>>", showcontent2)
lbox.bind("<Double-Button-1>", opensystem2)
# lb2.bind("<<ListboxSelect>>", showcontent2)
# lb2.bind("<Double-Button-1>", opensystem2)

###################################################################


if __name__ == "__main__":
    r.mainloop()
