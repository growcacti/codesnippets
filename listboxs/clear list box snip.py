def clearlbox1():
    lbox1.delete(0, END)
    lbox2.delete(0, END)
def clearlbox2():
    lbox5.delete(0, END)
    lbox6.delete(0, END)
btn3 = tk.Button(f6, text="Clear", command=clearlbox1)
btn3.grid(row=7, column=0)
