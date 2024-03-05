#building a calculator

from tkinter import *

window=Tk()
window.title("GUILESSON")
window.configure(background="pink", relief="solid")
window.geometry("700x200")

def add_function():
    a = int(en1.get())
    b = int(en2.get())
    result= a+b
    mytexbox.configure(text=result)

def clear_function():
    en1.delete(0,END)
    en2.delete(0,END) #use this for clearing. use 'destroy' to exit.
    mytexbox.configure(text="")

lb1=Label(window,text="First number:", font="arial 18 bold")
lb1.grid(row=0,column=0)

en1=Entry(window)
en1.grid(row=0,column=1)

lb2=Label(window,text="Second number:", font="arial 18 bold")
lb2.grid(row=1,column=0)

en2=Entry(window)
en2.grid(row=1,column=1)

lb3=Label(window,text="Result:", font="arial 18 bold")
lb3.grid(row=2,column=0)

mytexbox= Label(window, width=30)#never make results a textbox
mytexbox.grid(row=2,column=1)

my_button=Button(window, text="Add", command=add_function)
my_button.grid(row=3,column=1)

my_clearbutton=Button(window,text="Clear", command=clear_function)
my_clearbutton.grid(row=4,column=1)


#first establish your window

window.mainloop()
