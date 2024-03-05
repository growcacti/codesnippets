from tkinter import *
root = Tk()
courses = ['C','C++','Python','Java','Unix','DevOps'] r = ['course'] for c in courses:
tk.Label(text=c, width=15).grid(column=0)
tk.Label(text=r, relief=tk.RIDGE, width=15).grid(column=1)


Label(text="Position 1", width=10).grid(row=0, column=0)
Label(text="Position 2", width=10).grid(row=0, column=1)
Label(text="Position 3", width=10).grid(row=1, column=0)
Label(text="Position 4", width=10).grid(row=1, column=1)
root.mainloop()
