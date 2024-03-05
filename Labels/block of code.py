
Label(text="Position 1", width=10).grid(row=0, column=0)
Label(text="Position 2", width=10).grid(row=0, column=1)
Label(text="Position 3", width=10).grid(row=1, column=0)
Label(text="Position 4", width=10).grid(row=1, column=1)
root.mainloop()


def counter_label(label):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)

    count()
tk.Label(root, text="Red Text in Times Font", fg="red", font="Times").pack()
tk.Label(
    root,
    text="Green Text in Helvetica Font",
    fg="light green",
    bg="dark green",
    font="Helvetica 16 bold italic",
).pack()
tk.Label(
    root,
    text="Blue Text in Verdana bold",
    fg="blue",
    bg="yellow",
    font="Verdana 10 bold",
).pack()

root.mainloop()

rb1 = Radiobutton(frame, text="2", value=2).grid(row=1, column=1)
rb2 = Radiobutton(frame, text="3", value=3).grid(row=2, column=1)
rb3 = Radiobutton(frame, text="4", value=4).grid(row=3, column=1)
rb4 = Radiobutton(frame, text="5", value=5).grid(row=4, column=1)
rb5 = Radiobutton(frame, text="6", value=6).grid(row=5, column=1)
rb6 = Radiobutton(frame, text="7", value=7).grid(row=6, column=1)
rb7 = Radiobutton(frame, text="8", value=8).grid(row=7, column=1)
rb8 = Radiobutton(frame, text="9", value=9).grid(row=8, column=1)
rb9 = Radiobutton(frame, text="10", value=10).grid(row=9, column=1)
none_Rb = Radiobutton(frame, text="None", value=0).grid(row=10, column=1)


btn01 = Button(top, text="reset", command=reset, padx=20, pady=5).grid(row=19, column=1)
btn02 = Button(top, text="execute", command=lambda: execute, padx=20, pady=5).grid(
    row=20, column=1
)


class Checkbar(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var)
            chk.pack(side=side, anchor=anchor, expand=YES)
            self.vars.append(var)

    def state(self):
        return map((lambda var: var.get()), self.vars)


if __name__ == "__main__":
    root = Tk()
    lng = Checkbar(root, ["Python", "Ruby", "Perl", "C++"])
    tgl = Checkbar(root, ["English", "German"])
    lng.pack(side=TOP, fill=X)
    tgl.pack(side=LEFT)
    lng.config(relief=GROOVE, bd=2)

    def allstates():
        print(list(lng.state()), list(tgl.state()))

    Button(root, text="Quit", command=root.quit).pack(side=RIGHT)
    Button(root, text="Peek", command=allstates).pack(side=RIGHT)
    root.mainloop()
