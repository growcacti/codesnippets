from tkinter import *
from tkinter import ttk
from Bone import *

skeleton = {
    1: Bone(-0.42, 0.1, 0.02, 0.002, 0.234),
    4: Bone(4, 0.042, 0.32, 0.23, -0.32),
    11: Bone(11, 1, -0.23, -0.42, 0.42),
    95: Bone(95, -0.93, 0.32, 0.346, 0.31),
}


root = Tk()
root.geometry("400x600")

boneID = Label(root, text="ID: 1")
boneID.grid(row=1, column=1, sticky=W, padx=(0, 15))

w = Label(root, text="-0.42")
w.grid(row=1, column=2, sticky=W)

x = Label(root, text="0.02")
x.grid(row=1, column=4, sticky=W)

y = Label(root, text="0.002")
y.grid(row=1, column=6, sticky=W)

z = Label(root, text="0.234")
z.grid(row=1, column=8, sticky=W)

wPlusBtn = Button(root, text="+")
wPlusBtn.grid(row=2, column=2)
wMinusBtn = Button(root, text="-")
wMinusBtn.grid(row=2, column=3, padx=(0, 15))

xPlusBtn = Button(root, text="+")
xPlusBtn.grid(row=2, column=4)
xMinusBtn = Button(root, text="-")
xMinusBtn.grid(row=2, column=5, padx=(0, 15))

yPlusBtn = Button(root, text="+")
yPlusBtn.grid(row=2, column=6)
yMinusBtn = Button(root, text="-")
yMinusBtn.grid(row=2, column=7, padx=(0, 15))

zPlusBtn = Button(root, text="+")
zPlusBtn.grid(row=2, column=8)
zMinusBtn = Button(root, text="-")
zMinusBtn.grid(row=2, column=9, padx=(0, 15))

root.mainloop()
