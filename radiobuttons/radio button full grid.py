from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("JH app sample")
root.geometry("250x300")


def selection():
    choice = var.get()
    if choice == 1:
        m = "Ms."
    elif choice == 2:
        m = "Mr."
    elif choice == 3:
        pass
    return m


def submit():
    name = entry1.get()
    m = selection()
    return messagebox.showinfo("app sample", f"{m} {name}, privacy protected.")


frm1 = Label(root)
frm1.grid(row=0, column=0, rowspan=2)
frm2 = LabelFrame(frm1, text="sexual orientation", padx=30, pady=10)

var = IntVar()

Label(frm1, text="Full Name").grid(row=0, column=0, padx=5, pady=5)
Label(frm1, text="Email").grid(row=1, column=0, padx=5, pady=5)
Label(frm1, text="Password").grid(row=2, column=0, padx=5, pady=5)
Radiobutton(frm2, text="Female", variable=var, value=1, command=selection).grid(
    row=5, column=2
)
Radiobutton(frm2, text="Male", variable=var, value=2, command=selection).grid(
    row=6, column=2
)
Radiobutton(frm2, text="groups", variable=var, value=3, command=selection).grid(
    row=7, column=2
)
entry1 = Entry(frm1)
entry1.grid(row=0, column=2)
entry2 = Entry(frm1)
entry2.grid(row=1, column=2)
entry3 = Entry(frm1, show="*")
entry3.grid(row=2, column=2)
frm2.grid(row=3, columnspan=3, padx=30)
Button(frm1, text="Submit", command=submit, padx=50, pady=5).grid(
    row=4, columnspan=4, pady=5
)

root.mainloop()
