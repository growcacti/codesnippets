import tkinter
from tkinter import *

pw = PanedWindow()
pw.grid(row=1, column=1)

entry = Entry(pw, bd=5)
pw.add(entry)

pw1 = PanedWindow(pw, orient=VERTICAL)
pw.add(pw1)

sl = Scale(pw1, orient=HORIZONTAL)
pw1.add(sl)
sl1 = Scale(pw1, orient=HORIZONTAL)
pw1.add(sl1)
s2 = Scale(pw1, orient=HORIZONTAL)
pw1.add(s2)
s3 = Scale(pw1, orient=HORIZONTAL)
pw1.add(s3)
s4 = Scale(pw1, orient=HORIZONTAL)
pw1.add(s4)
pw1.add(b=Button(pw1, text="Click Me"))
pw1.add(b)

mainloop()
