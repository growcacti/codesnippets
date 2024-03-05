import tkinter as tk
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x500")
notebook = ttk.Notebook(root)
notebook.pack()

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
notebook.add(frame1, text="1")
notebook.add(frame2, text="2")
ttk.Button(frame2, text="Click me").pack()
frame3 = ttk.Frame(notebook)
notebook.add(frame3, text="3")
frame4 = ttk.Frame(notebook)
spinbox1 = ttk.Spinbox(frame4, from_=1, to=1000).pack(side=TOP)
spinbox2 = ttk.Spinbox(frame4, from_=1, to=1000).pack(side=LEFT)
spinbox3 = ttk.Spinbox(frame4, from_=1, to=1000).pack(side=RIGHT)
notebook.add(frame4, text="4")
frame5 = ttk.Frame(notebook)

# label text for title
label_combo = ttk.Label(frame5, text="GFG Combobox Widge").pack()

# label
ttk.Label(frame5, text="Select the Month :", font=("Times New Roman", 10)).pack(
    padx=10, pady=25
)

# Combobox creation
n = tk.StringVar()
monthchoosen = ttk.Combobox(frame5, width=27, textvariable=n)

# Adding combobox drop down list
monthchoosen["values"] = (
    " January",
    " February",
    " March",
    " April",
    " May",
    " June",
    " July",
    " August",
    " September",
    " October",
    " November",
    " December",
)

monthchoosen.pack(side=LEFT)
monthchoosen.current()
notebook.add(frame5, text="5")
frame6 = ttk.Frame(notebook)
notebook.add(frame6, text="6")
frame7 = ttk.Frame(notebook)
notebook.add(frame7, text="7")
frame8 = ttk.Frame(notebook)
notebook.add(frame8, text="8")
frame8 = ttk.Frame(notebook)
notebook.add(frame9, text="9")
frame9 = ttk.Frame(notebook)
notebook.add(frame10, text="10")
frame10 = ttk.Frame(notebook)
notebook.add(frame11, text="11")
# disables the tab
# notebook.tab(0, state = 'disabled')
# entering and displaying multiple lines with the text widget
text = Text(frame1, width=100, height=100)
text.pack()
text2 = Text(frame2, width=100, height=100)
text2.pack()
text3 = Text(frame3, width=100, height=100)
text3.pack()
text4 = Text(frame4, width=10, height=10)
text4.pack()
text5 = Text(frame5, width=100, height=100)
text5.pack()
text6 = Text(frame6, width=100, height=100)
text6.pack()
text7 = Text(frame7, width=100, height=100)
text7.pack()
text8 = Text(frame8, width=100, height=100)
text8.pack()
text9 = Text(frame9, width=100, height=100)
text9.pack()
text10 = Text(frame10, width=100, height=100)
text10.pack()


def combo():
    window = tk.Tk()
    window.title("Combobox")
    window.geometry("250x150")

    # label text for title
    ttk.Label(
        window,
        text="GFG Combobox Widget",
        background="green",
        foreground="white",
        font=("Times New Roman", 15),
    ).grid(row=0, column=1)

    # label
    ttk.Label(window, text="Select the Month :", font=("Times New Roman", 10)).grid(
        column=0, row=5, padx=10, pady=25
    )

    # Combobox creation
    n = tk.StringVar()
    monthchoosen = ttk.Combobox(window, width=27, textvariable=n)

    # Adding combobox drop down list
    monthchoosen["values"] = (
        " January",
        " February",
        " March",
        " April",
        " May",
        " June",
        " July",
        " August",
        " September",
        " October",
        " November",
        " December",
    )

    monthchoosen.grid(column=1, row=5)
    monthchoosen.current()


# window = Tk()
# window.geometry('250x150')
def para_res():

    # --- functions ---
    # ---GUI for adding two resistors in parallel and in series
    # Future project with be with 3 or more resistors
    # Would also like to make a reverse calculation which give parallel resistor for ohm value desired
    def generate():
        try:
            con1 = 1 / float(num1.get())  # seems to work better if done in steps
            con2 = 1 / float(num2.get())  # con is for conductance
            consum = con1 + con2
            result = 1 / consum
            result2 = float(num1.get()) + float(
                num2.get()
            )  # using float is obvious way
        except Exception as ex:
            print(ex)
            result = "error"

        num3.set(result)
        num4.set(result2)

    root = tk.Tk()

    num1 = tk.StringVar()
    num2 = tk.StringVar()
    num3 = tk.StringVar()
    num4 = tk.StringVar()
    tk.Label(root, text=" Input R1:").grid(row=0, column=0)
    tk.Label(root, text="Input R2:").grid(row=1, column=0)
    tk.Label(root, text=" Output Parallel:").grid(row=2, column=0)
    tk.Label(root, text="Output Series:").grid(row=3, column=0)

    tk.Entry(root, textvariable=num1).grid(row=0, column=1)
    tk.Entry(root, textvariable=num2).grid(row=1, column=1)
    tk.Entry(root, textvariable=num3).grid(row=2, column=1)
    tk.Entry(root, textvariable=num4).grid(row=3, column=1)
    button = tk.Button(root, text="Calculate", command=generate)
    button.grid(row=4, column=1)

    root.mainloop()


if __name__ == "__main__":
    mainloop()
