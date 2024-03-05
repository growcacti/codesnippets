

import tkinter as tk
import os

# WINDOW CREATION
win = tk.Tk()
geo = win.geometry
geo("400x400+400+400")
win['bg'] = 'blue'
# get the list of files
flist = os.listdir()

lbox = tk.Listbox(win)
lbox.pack()

# THE ITEMS INSERTED WITH A LOOP
for item in flist:
    lbox.insert(tk.END, item)

win.mainloop()