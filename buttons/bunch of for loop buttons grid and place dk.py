import tkinter
from tkinter import *

win = Tk()
win.geometry("400x400")
frame = Frame(win)
frame.grid(row=5,column=10)

def numone(b):
    print("1")






b=0
for i in range(6):
    for j in range(6):
        b = b + 1
        Button(win, text = str(b), borderwidth=1).grid(row=i,column=j)
Button(text=str("1"), command=numone)
l1 = Label(win,text="Maths")
l1.place(x=10,y=200)
e1 = Entry(win,bd=5)
e1.place(x=60,y=200)
l2 = Label(win,text="English")
l2.place(x=10,y=250)
e2 = Entry(win,bd=5)
e2.place(x=60,y=250)
b = Button(win,text="Click Me")
b.place(x=100,y=300)

win.mainloop()
