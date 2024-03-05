import tkinter as tk
from tkinter import *
from tkinter import ttk


# r is root window, container
# f is frame example f1 is frame 1 sub container to r
# f is assicated wityh the tabs f1 is tab1
# nb is notebook to make tabs
# lbox is list box,
# cb isa combo box,
# e is entry,
# sp is spin box,
# txt is text widget
# label is Label if it need a variable

r
nb = ttk.Notebook(r)
nb.pack(expand=1, fill="both")

f1 = ttk.Frame(nb)


nb.add(f1, text="First")

##################################################
# Functions
##################################################


def ne(n, m, *args):

    n = e1.get()
    m = cb.get()
    lbox1.insert(1, n)
    lbox2.insert(1, m)


Label(f1, text="label1").grid(column=0, row=0)

Label(f1, text="label1").grid(column=0, row=2)

e1 = tk.Entry(f1, bg="yellow")
e1.grid(column=0, row=3)
Label(f1, text="label1").grid(column=0, row=4)

e2 = tk.Entry(f1, bg="yellow")
e2.grid(column=0, row=5)

cb = ttk.Combobox(
    f1,
    values=(
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "0",
        "=",
        "q",
        "w",
        "e",
        "r",
        "t",
        "y",
        "u",
        "i",
        "o",
        "p",
        "DEL",
        "a",
        "s",
        "d",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        ";",
        '"',
        "z",
        "x",
        "c",
        "v",
        "b",
        "n",
        "m",
        ",",
        ".",
        "!",
        "TAB",
        "SPACE",
    ),
)

cb.grid(column=1, row=3)
cb.set("-")

cb2 = ttk.Combobox(
    f1,
    values=(
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ),
)
cb2.grid(column=1, row=5)
cb2.set("A")
# cb.bind("<FocusIn>", defocus)


# combo_box.bind("<<ComboboxSelected>>"
btn1 = tk.Button(f1, text="send", command=ne)
btn1.grid(column=2, row=1)
btn2 = tk.Button(f1, text="button 2", command=command)
btn2.grid(column=2, row=2)
btn3 = tk.Button(f1, text="button 3", command=command).grid(column=2, row=3)
btn4 = tk.Button(f1, text="button 4", command=command).grid(column=2, row=4)
btn5 = tk.Button(f1, text="button 5", command=command).grid(column=2, row=5)
btn6 = tk.Button(f1, text="button 6", command=command).grid(column=3, row=1)
btn7 = tk.Button(f1, text="button 7", command=command).grid(column=3, row=2)
btn8u = tk.Button(f1, text="button 8", command=command).grid(column=3, row=3)
btn9 = tk.Button(f1, text="button 9", command=command).grid(column=3, row=4)
btn10 = tk.Button(f1, text="button 10", command=command).grid(column=3, row=5)
# The is the start of the 2nd tab which is also the 2nd frame f2 and the container
f2 = ttk.Frame(nb)
nb.add(f2, text="Second")
Label(f2, text="label2").grid(column=0, row=0)
Label(f2, text="label3").grid(column=2, row=0)
Label(f2, text="label4").grid(column=4, row=0)
Label(f2, text="label5").grid(column=6, row=0)
lbox1 = tk.Listbox(f2).grid(column=2, row=1)
lbox2 = tk.Listbox(f2).grid(column=4, row=1)
lbox3 = tk.Listbox(f2).grid(column=6, row=1)


f3 = ttk.Frame(nb)
nb.add(f3, text="Tab3")
Label(f3, text="label").grid(column=0, row=0)

Label(f3, text="label1").grid(column=0, row=0)

Label(f3, text="label1").grid(column=0, row=2)
ee1 = tk.StringVar()
Entry(f3, textvariable=ee1, bg="yellow").grid(column=0, row=3)
Label(f3, text="label1").grid(column=0, row=4)
ee2 = tk.StringVar()
Entry(f3, textvariable=ee2, bg="yellow").grid(column=0, row=5)
btn1 = tk.Button(f1, text="button 1", command=command).grid(column=2, row=1)
btn2 = tk.Button(f1, text="button 2", command=command).grid(column=2, row=2)
btn3 = tk.Button(f1, text="button 3", command=command).grid(column=2, row=3)
btn4 = tk.Button(f1, text="button 4", command=command).grid(column=2, row=4)
btn5 = tk.Button(f1, text="button 5", command=command).grid(column=2, row=5)

text = tk.Text(f3, bg="light green", height=50)
text.insert("1.0", tk.END)
text.grid(row=1, column=4, rowspan=5, columnspan=10)
# ----------------------------------------------------------
# tab4
# ----------------------------------------------------------


def termsCheck():
    if ckb.get() == 1:
        submit_btn["state"] = NORMAL
    else:
        submit_btn["state"] = DISABLED
        messagebox.showerror("Accept the terms & conditions")


f4 = ttk.Frame(nb)
nb.add(f4, text="Tab4")
Label(f4, text="label").grid(column=2, row=0)
Label(f4, text="label1").grid(column=4, row=0)
Label(f4, text="label1").grid(column=6, row=2)

Label(f4, text="label1").grid(column=0, row=0)

Label(f4, text="label1").grid(column=0, row=2)
ee1 = tk.StringVar()
Entry(f4, textvariable=ee1, bg="yellow").grid(column=0, row=3)
Label(f4, text="label1").grid(column=0, row=4)
ee2 = tk.StringVar()
Entry(f4, textvariable=ee2, bg="yellow").grid(column=0, row=5)


ckb = IntVar()
Checkbutton(
    f4,
    text="Accept the terms & conditions",
    variable=ckb,
    onvalue=1,
    offvalue=0,
    command=termsCheck,
).grid(row=8, columnspan=4, pady=5)


rb1 = tk.IntVar()
rb1.set(1)

radiobutton1 = tk.Radiobutton(f4, text="Radio 1", variable=rb1, value=1)
radiobutton1.grid(column=4, row=1)

radiobutton2 = tk.Radiobutton(f4, text="Radio 2", variable=rb1, value=2)
radiobutton2.grid(column=5, row=1)
r.mainloop()
