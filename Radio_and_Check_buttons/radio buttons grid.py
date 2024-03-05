import tkinter as tk
from tkinter import *

top = Tk()
top.title("App")
top.geometry("450x400")
top.configure(bg="light green")
frame = tk.Frame(top)
frame.grid(row=0, column=1, rowspan=4, columnspan=4)


def reset():
    pass


def execute():
    pass


Label(top, text="to calculate 2 - 10").grid(row=0, column=0)
rb1 = Radiobutton(frame, text="2", value=2).grid(row=1, column=1)
rb2 = Radiobutton(frame, text="3", value=3).grid(row=2, column=1)
rb3 = Radiobutton(frame, text="4", value=4).grid(row=3, column=1)
rb4 = Radiobutton(frame, text="5", value=5).grid(row=4, column=1)
rb5 = Radiobutton(frame, text="6", value=6).grid(row=5, column=1)
rb6 = Radiobutton(frame, text="7", value=7).grid(row=6, column=1)
rb7 = Radiobutton(frame, text="8", value=8).grid(row=7, column=1)
rb8 = Radiobutton(frame, text="9", value=9).grid(row=8, column=1)
rb9 = Radiobutton(frame, text="10", value=10).grid(row=9, column=1)
none_Rb = Radiobutton(frame, text="None", value=0).grid(row=10, column=1)


btn01 = Button(top, text="reset", command=reset, padx=20, pady=5).grid(row=19, column=1)
btn02 = Button(top, text="execute", command=lambda: execute, padx=20, pady=5).grid(
    row=20, column=1
)
