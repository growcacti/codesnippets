
import tkinter as tk
from tkinter import 
top = Tk()
top.title("App")
top.geometry('450x400')
top.configure(bg='light green')



Label(top, text='to calculate 2 - 10').pack()
rb1 = Radiobutton(frame, text="2", value=2).pack(anchor=W)
rb2 = Radiobutton(frame, text="3", value=3).pack(anchor=W)
rb3 = Radiobutton(frame, text="4", value=4).pack(anchor=W)
rb4 = Radiobutton(frame, text="5", value=5).pack(anchor=W)
rb5 = Radiobutton(frame, text="6", value=6).pack(anchor=W)
rb6 = Radiobutton(frame, text="7", value=7).pack(anchor=W)
rb7 = Radiobutton(frame, text="8", value=8).pack(anchor=W)
rb8 = Radiobutton(frame, text="9", value=9).pack(anchor=W)
rb9 = Radiobutton(frame, text="10", value=10).pack(anchor=W)
none_Rb = Radiobutton(frame, text="None", value=0).pack(anchor=W)
`

btn01 = Button(top, text='reset', command=reset, padx=20, pady=5).pack(pady=10)
btn02 = Button(top, text='execute', command=lambda: parares, padx=20, pady=5).pack(pady=10)







