import tkinter
from tkinter import *
from tkinter import messagebox

root = Tk()

def open():
    messagebox.shorootfo('From My Computer','Your File has been Opened')
def close():
    messagebox.shorootfo('From My Computer','Your File has been Closed')
def nothing():
    messagebox.shorootfo('From My Computer','Are You Feeling Well')

menubar = Menu(root)

filemenu = Menu(menubar)
filemenu.add_command(label="Open File",command=open)
filemenu.add_command(label="New File",command=nothing)
filemenu.add_separator()
filemenu.add_command(label="Save",command=nothing)
filemenu.add_command(label="Save As",command=nothing)
filemenu.add_separator()
filemenu.add_command(label="Close",command=close)
filemenu.add_command(label="Close Tab",command=nothing)
filemenu.add_command(label="Close rootdow",command=nothing)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.quit)

menubar.add_cascade(label="File", menu = filemenu)

editmenu = Menu(menubar)
editmenu.add_command(label="Undo",command=nothing)
editmenu.add_command(label="Redo",command=nothing)
editmenu.add_separator()
editmenu.add_command(label="Copy",command=nothing)
editmenu.add_command(label="Paste",command=nothing)
editmenu.add_separator()
editmenu.add_command(label="Columns",command=nothing)
editmenu.add_command(label="Lines",command=nothing)
editmenu.add_command(label="Text",command=nothing)
editmenu.add_separator()
editmenu.add_command(label="Exit",command=root.quit)

menubar.add_cascade(label="Edit", menu = editmenu)

root.config(menu = menubar)

root.mainloop()
