from fractions import Fraction
import tkinter as tk


def fc(d=0.25):

    frc = Fraction(str(d))
    lb.insert(1, frc)


# Define a window name
r = tk.Tk()
var = tk.DoubleVar()
# declare the spinbox widget by assigning values to from_, to and increment
sp = tk.Spinbox(r, from_=0.01, to=50.0, increment=0.01, textvariable=var)
# To show the content in the window
sp.grid(row=0, column=0)

##
##var2 = tk.DoubleVar()
###declare the spinbox widget by assigning values to from_, to and increment
##sp = tk.Spinbox(
##r,
##from_=1.0,
##to=1000.0,
##increment=0.1,
##textvariable=var2
##)
###To show the content in the window
##sp.grid(row=1, column=0)
##
##
##
##
##var3 = tk.DoubleVar()
###declare the spinbox widget by assigning values to from_, to and increment
##sp2 = tk.Spinbox(
##r,
##from_=1,
##to=31,
##increment=1,
##textvariable=var3
##)
###To show the content in the window
##sp2.grid(row=2, column=0)
tk.Label(r, text="   ").grid(row=2, column=1)
tk.Label(r, text="     ").grid(row=1, column=1)
tk.Label(r, text="  ").grid(row=0, column=1)
btn = tk.Button(r, text="show", command=lambda: fc(sp.get))
btn.grid(row=6, column=2)
lb = tk.Listbox(r)
lb.grid(row=6, column=1)


r.mainloop()
