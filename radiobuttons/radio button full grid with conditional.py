from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("JH app sample")
root.geometry("250x300")


def selection():
    choice = var.get()
    if choice == 1:

        m = "ooooo"
    elif choice == 2:
        m = "--------."
    elif choice == 3:
        m = "11"
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass
    elif choice == 7:
        pass

    elif choice == 8:
        pass
    elif choice == 9:
        pass
    elif choice == 10:
        pass
    elif choice == 11:
        pass
    elif choice == 12:
        pass
    elif choice == 13:
        pass
    elif choice == 14:
        pass
    elif choice == 15:
        pass

    return m


def submit():

    m = selection()
    return messagebox.showinfo("app sample", f"{m} {name}, privacy protected.")


frm1 = Label(root)
frm1.grid(row=0, column=0, rowspan=2)
frm2 = LabelFrame(frm1, text=" ", padx=30, pady=10)

var = IntVar()
rb1 = Radiobutton(frm2, text="From 1", variable=var, value=1, command=selection).grid(
    row=2, column=2
)
rb2 = Radiobutton(frm2, text="From 2", variable=var, value=2, command=selection).grid(
    row=3, column=2
)
rb3 = Radiobutton(frm2, text="From 3", variable=var, value=3, command=selection).grid(
    row=4, column=2
)
rb4 = Radiobutton(frm2, text="From 4", variable=var, value=4, command=selection).grid(
    row=5, column=2
)
rb5 = Radiobutton(frm2, text="From 5", variable=var, value=5, command=selection).grid(
    row=6, column=2
)
rb6 = Radiobutton(frm2, text="From 6", variable=var, value=6, command=selection).grid(
    row=7, column=2
)
rb7 = Radiobutton(frm2, text="From 7", variable=var, value=7, command=selection).grid(
    row=8, column=2
)
rb8 = Radiobutton(frm2, text="From 8", variable=var, value=8, command=selection).grid(
    row=9, column=2
)
rb9 = Radiobutton(frm2, text="From 9", variable=var, value=9, command=selection).grid(
    row=10, column=2
)
rb10 = Radiobutton(
    frm2, text="From 10", variable=var, value=10, command=selection
).grid(row=11, column=2)
rb11 = Radiobutton(
    frm2, text="From 11", variable=var, value=11, command=selection
).grid(row=12, column=2)
rb12 = Radiobutton(
    frm2, text="From 12", variable=var, value=12, command=selection
).grid(row=13, column=2)
rb13 = Radiobutton(
    frm2, text="From 13", variable=var, value=13, command=selection
).grid(row=14, column=2)
rb14 = Radiobutton(
    frm2, text="From 14", variable=var, value=14, command=selection
).grid(row=15, column=2)
rb15 = Radiobutton(
    frm2, text="From 15", variable=var, value=15, command=selection
).grid(row=16, column=2)
frm2.grid(row=3, columnspan=3, padx=30)
Button(frm1, text="Submit", command=submit, padx=50, pady=5).grid(
    row=4, columnspan=4, pady=5
)

root.mainloop()
