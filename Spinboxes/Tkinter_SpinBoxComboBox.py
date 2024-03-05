from tkinter import *
from tkinter import ttk

root = Tk()
month = StringVar()
combobox = ttk.Combobox(root, textvariable=month)
combobox.grid(row=1, column=1)
combobox.config(
    values=(
        "jan",
        "feb",
        "mar",
        "apr",
        "may",
        "jun",
        "jul",
        "aug",
        "sep",
        "oct",
        "nov",
        "dec",
    )
)
year = StringVar()
spinbox = Spinbox(root, from_=1990, to=2020, textvariable=year)
spinbox.grid(row=2, column=1)
root.mainloop()
