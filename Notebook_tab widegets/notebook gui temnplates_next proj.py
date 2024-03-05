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

r = Tk()
r.geometry("800x800")
r.title("Notebook Template")


def movetolist():
    lbox1.insert(1, e1.get())
    llbox.insert(2, e2.get())


nb = ttk.Notebook(r)
nb.pack(expand=1, fill="both")

f1 = ttk.Frame(nb)


nb.add(f1, text="First")


e1 = tk.Entry(f1)
e1.grid(column=0, row=0)

e2 = tk.Entry(f1)
e2.grid(column=0, row=2)


lbox1 = tk.Listbox(f1)
lbox1.grid(column=0, row=6)


# combo_box.bind("<<ComboboxSelected>>"
btn1 = tk.Button(f1, text="button 1", command=movetolist).grid(column=3, row=1)
btn2 = tk.Button(f1, text="button 2", command=com).grid(column=3, row=2)
btn3 = tk.Button(f1, text="button 3", command=com).grid(column=3, row=3)
btn4 = tk.Button(f1, text="button 4", command=com).grid(column=3, row=4)
btn5 = tk.Button(f1, text="button 5", command=com).grid(column=3, row=5)
btn6 = tk.Button(f1, text="button 6", command=com).grid(column=4, row=1)
btn7 = tk.Button(f1, text="button 7", command=com).grid(column=4, row=2)
btn8u = tk.Button(f1, text="button 8", command=com).grid(column=4, row=3)
btn9 = tk.Button(f1, text="button 9", command=com).grid(column=4, row=4)
btn10 = tk.Button(f1, text="button 10", command=command).grid(column=3, row=5)
# The is the start of the 2nd tab which is also the 2nd frame f2 and the container
f2 = ttk.Frame(nb)
nb.add(f2, text="Second")

lbox2 = tk.Listbox(f2)
lbox2.grid(column=0, row=1, rowspan=4)


f3 = ttk.Frame(nb)
nb.add(f3, text="Tab3")


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


rb1 = tk.IntVar()
rb1.set(1)

radiobutton1 = tk.Radiobutton(f4, text="Radio 1", variable=rb1, value=1)
radiobutton1.grid(column=4, row=1)

radiobutton2 = tk.Radiobutton(f4, text="Radio 2", variable=rb1, value=2)
radiobutton2.grid(column=5, row=1)
r.mainloop()
