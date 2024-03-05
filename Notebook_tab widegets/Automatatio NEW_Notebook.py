import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import pyautogui as pg
import pyperclip as pc
import sys

root = tk.Tk()
root.geometry("1800x900")
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0)
fr1 = ttk.Frame(notebook, height=200, width=200)

fr2 = ttk.Frame(notebook)
fr2.rowconfigure(0, minsize=800, weight=1)
fr2.columnconfigure(1, minsize=800, weight=1)


notebook.add(fr1, text="Control")
notebook.add(fr2, text="txtpad")
fr3 = ttk.Frame(notebook)
notebook.add(fr3, text="3")
fr4 = ttk.Frame(notebook)
notebook.add(fr4, text="4")
fr5 = ttk.Frame(notebook)
notebook.add(fr5, text="5")
fr6 = ttk.Frame(notebook)
notebook.add(fr6, text="6")
fr7 = ttk.Frame(notebook)
notebook.add(fr7, text="7")
fr8 = ttk.Frame(notebook)
notebook.add(fr8, text="8")
fr9 = ttk.Frame(notebook)
notebook.add(fr9, text="9")
fr10 = ttk.Frame(notebook)
notebook.add(fr10, text="10")
fr11 = ttk.Frame(notebook)
notebook.add(fr11, text="11")
# disables the tab
# notebook.tab(0, state = 'disabled')
# entering and displaying multiple lines with the text widget
################################################################
# Tab1
################################################################
ffr1 = ttk.Frame(fr1)
ffr1.grid(row=0, column=0, rowspan=10)
ffr2 = ttk.Frame(fr1)
ffr2.grid(row=4, column=1, rowspan=10)
ffr3 = ttk.Frame(fr1)
ffr3.grid(row=3, column=2, rowspan=10)
ffr4 = ttk.Frame(fr1)
ffr4.grid(row=3, column=3, rowspan=10)
ffr5 = ttk.Frame(fr1)
ffr5.grid(row=3, column=4, rowspan=10)
ffr6 = ttk.Frame(fr1)
ffr6.grid(row=3, column=5, rowspan=10)
e1 = tk.Entry(fr1, bg="light green")
e1.grid(row=12, column=4)

e2 = tk.Entry(fr1, bg="light blue")
e2.grid(row=13, column=4)

e3 = tk.Entry(fr1, bg="plum")
e3.grid(row=15, column=4)

e4 = tk.Entry(fr1, bg="orange")
e4.grid(row=6, column=4)

e5 = tk.Entry(fr1, bg="pink")
e5.grid(row=8, column=4)

e6 = tk.Entry(fr1, bg="blue")
e6.grid(row=10, column=4)

e7 = tk.Entry(fr1, bg="light green")
e7.grid(row=12, column=4)

e8 = tk.Entry(fr1, bg="lime green")
e8.grid(row=10, column=4)

e9 = tk.Entry(fr1, bg="light yellow")
e9.grid(row=11, column=4)

e10 = tk.Entry(fr1, bg="cyan")
e10.grid(row=12, column=4)

e11 = tk.Entry(fr1, bg="lawn green")
e11.grid(row=14, column=4)

e1 = tk.StringVar()
e2 = tk.StringVar()
e3 = tk.StringVar()
e4 = tk.StringVar()
e5 = tk.StringVar()
e6 = tk.StringVar()
e7 = tk.StringVar()
e8 = tk.StringVar()
e9 = tk.StringVar()
e10 = tk.StringVar()
e11 = tk.StringVar()


def get_filename(_type=""):
    "Returns the path and name of file selected"
    # _type=".txt" to get txt file name

    filename = filedialog.askopenfilename(
        initialdir=".",  # same dir of this script
        title="Select file",
        filetypes=(("", _type), ("all files", "*.*")),
    )
    text2.insert(tk.END, filename)
    text2.insert(tk.END, "\n")
    return filename


###########################################################
def insert1():
    lb1.insert(1, cb1.get())


def insert2():
    lb1.insert(1, cb2.get())


def insert3():
    lb1.insert(1, cb1.get())


def insert3():
    lb1.insert(1, cb1.get())


def insert4():
    lb1.insert(1, cb1.get())


def insert5():
    lb1.insert(1, cb1.get())


def clear():
    lb1.delete(0, END)


def txte1(txt):

    text2.insert(tk.END, txt)
    text2.insert(tk.END, "\n")


def txte2(txt):

    text2.insert(tk.END, txt)
    text2.insert(tk.END, "\n")


def txte3(txt):

    text2.insert(tk.END, txt)
    text2.insert(tk.END, "\n")


def cl():
    fr1.withdraw()
    fr1.clipboard_clear()
    fr1.clipboard_append(entry.get())
    fr1.update()
    fr1.deiconify()
    return


def paste():
    # pg.hotkey('alt', 'tab')  # change window
    pg.hotkey("ctrl", "v")  # ctrl-v to paste
    return


def copy():
    pg.hotkey("ctrl", "c")  # ctrl-c to copy
    return


def manager():
    pass


text1 = "www.distrowatch.com"


def auto1():
    text1 = "www.distrowatch.com"
    pg.hotkey("alt", "F3", interval=0.25)  # change window
    pg.write("firefox")
    pg.press("enter")
    pg.moveTo(522, 120)
    pg.click(x=522, y=120)
    pg.click(x=522, y=120)
    pg.press("enter")
    pg.hoykey("ctrl", "a")
    pg.press("backspace")
    pc.copy(text1)
    pg.hotkey("ctrl", "v")


##         pc.paste()
##         pg.press('enter')
##         pg.hotkey('ctrl', 'a')
##         pg.press('backspace')
##pg.click(x=100, y=200)
## pg.hotkey('F3')   # select  all
## pg.write("waterfox")
## #pg.hotkey('alt', 'tab')
## pg.hotkey('alt', 'tab')


def auto2():
    pg.hotkey("F4")
    pg.press("enter")
    pg.typewrite("sudo apt install update")
    pg.press("enter", interval=1)

    pc.paste
    pg.press("enter")


def auto3():
    pg.hotkey("F4")
    pg.press("enter")
    pg.write("cd /media/jh/Python_Backup")
    pg.press("enter")
    pg.write("pwd")
    pg.press("enter")
    pg.write("find . -name '*.py' | xargs cp -t /home/jh/Desktop/PYDUMP")
    pg.press("enter")


def auto4():
    var_one = e1.get()
    var_two = e2.get()
    print(var_one)
    print(var_two)
    pg.hotkey("F4")
    pg.press("enter")
    pg.write(var_one)
    pg.press("enter")
    pg.write(var_two)
    pg.press("enter")


############################################################

##menubar = tk.Menu(top)
##menubar.add_command(label="load web", command=auto1)
##menubar.add_command(label="File", command=get_filename)
##menubar.add_command(label="Call", command=None)
##menubar.add_command(label="Insert", command=None)
##menubar.add_command(label="Run", command=None)
##menubar.add_command(label="1", command=None)
##menubar.add_command(label="2", command=None)
##menubar.add_command(label="3", command=None)
##menubar.add_command(label="4", command=None)
##menubar.add_command(label="5", command=None)
###################################################################
btn1 = tk.Button(fr1, text="auto2", command=auto2)
btn1.grid(column=0, row=1)
btn2 = tk.Button(fr1, text="auto3 find and dump", command=auto3)
btn2.grid(column=0, row=2)
btn3 = tk.Button(fr1, text="auto4", command=auto4)
btn3.grid(column=0, row=3)
btn4 = tk.Button(fr1, text="clear", command=clear)
btn4.grid(column=0, row=4)
btn5 = tk.Button(fr1, text="web broswer", command=auto1)
btn5.grid(column=0, row=5)
btn6 = tk.Button(fr1, text="Get Filename", command=get_filename)
btn6.grid(column=0, row=6)
btn7 = tk.Button(fr1, text="e1 to txtpad", command=lambda: txte1(e1.get()))
btn7.grid(column=0, row=7)
btn8 = tk.Button(fr1, text="e2 to txtpad", command=lambda: txte2(e2.get()))
btn8.grid(column=0, row=8)
btn9 = tk.Button(fr1, text="e3 to txtpad", command=lambda: txte3(e3.get()))
btn9.grid(column=0, row=9)
btn10 = tk.Button(fr1, text="button 10", command=None)
btn10.grid(column=0, row=10)
########################################################################
list1 = [
    "2323",
    "john.hewitt@cox.net",
    "Whobade55!",
    "john.hewitt1970@gmail.com",
    "ajolily@cox.net",
]
cb1 = ttk.Combobox(fr1, values=list1)
cb1.grid(row=3, column=1)
cb2 = ttk.Combobox(fr1, values=list1)
cb2.grid(row=4, column=1)
###########################################################################
lb1 = tk.Listbox(fr1)
lb1.grid(row=3, column=4, columnspan=3)


##btn11=tk.Button(fr1, text='copy', command=copy)
##btn11.grid(column=1, row=1)
##btn12=tk.Button(fr1, text='auto1', command=auto1)
##btn12.grid(column=1, row=2)
##btn13=tk.Button(fr1, text='auto2', command=command)
##btn13.grid(column=1, row=3)
##btn14=tk.Button(fr1, text='button 4', command=command)
##btn14.grid(column=1, row=4)
##btn15=tk.Button(fr1, text='button 5', command=command)
##btn15.grid(column=1, row=5)
##btn16=tk.Button(fr1, text='button 6', command=command)
##btn16.grid(column=1, row=6)
##btn17=tk.Button(fr1, text='button 7', command=command)
##btn17.grid(column=1, row=7)
##btn18=tk.Button(fr1, text='button 8', command=command)
##btn18.grid(column=1, row=8)
##btn19=tk.Button(fr1, text='button 9', command=command)
##btn19.grid(column=1, row=9)
##btn20=tk.Button(fr1, text='button 10', command=command)
##btn20.grid(column=1, row=10)


##btn21=tk.Button(fr1, text='copy', command=copy)
##btn21.grid(column=2, row=1)
##btn22=tk.Button(fr1, text='auto1', command=auto1)
##btn22.grid(column=2, row=2)
##btn23=tk.Button(fr1, text='auto2', command=command)
##btn23.grid(column=2, row=3)
##btn24=tk.Button(fr1, text='button 4', command=command)
##btn24.grid(column=2, row=4)
##btn25=tk.Button(fr1, text='button 5', command=command)
##btn25.grid(column=2, row=5)
##btn26=tk.Button(fr1, text='button 6', command=command)
##btn26.grid(column=2, row=6)
##btn27=tk.Button(fr1, text='button 7', command=command)
##btn27.grid(column=2, row=7)
##btn28=tk.Button(fr1, text='button 8', command=command)
##btn28.grid(column=2, row=8)
##btn29=tk.Button(fr1, text='button 9', command=command)
##btn29.grid(column=2, row=9)
##btn30=tk.Button(fr1, text='button 10', command=command)
##btn30.grid(column=2, row=10)
##
##


text2 = tk.Text(fr2)
text2.grid(row=0, column=1, sticky="nsew")


if __name__ == "__main__":
    root.mainloop()
