from tkinter import *

from tkinter import ttk


class Notebook:
    def __init__(self, title):

        self.root = Tk()

        self.root.title(title)

        self.notebook = ttk.Notebook(self.root)

    def add_tab(self, title, text):

        frame = ttk.Frame(self.notebook)

        self.notebook.add(frame, text=title)

        label = ttk.Label(frame, text=text)

        label.grid(column=1, row=1)

        self.notebook.pack()

    def run(self):

        self.root.mainloop()


nb = Notebook("Example")

nb.add_tab("Frame One", "This is on Frame One")

nb.add_tab("Frame Two", "This is on Frame Two")

nb.run()


from tkinter import *

from tkinter import ttk


class App(Frame):
    def __init__(self, *args, **kwargs):

        Frame.__init__(self, *args, **kwargs)

        self.notebook = ttk.Notebook()

        self.add_tab()

        self.notebook.grid(row=0)

    def add_tab(self):

        tab = Area(self.notebook)

        tab2 = Volume(self.notebook)

        self.notebook.add(tab, text="Tag")

        self.notebook.add(tab2, text="Tag2")


class Area(Frame):
    def __init__(self, name, *args, **kwargs):

        Frame.__init__(self, *args, **kwargs)

        self.label = Label(text="Hi This is Tab1")

        self.label.grid(row=1, column=0, padx=10, pady=10)

        self.name = name


class Volume(Frame):
    def __init__(self, name, *args, **kwargs):

        Frame.__init__(self, *args, **kwargs)

        self.label = Label(text="Hi This is Tab2")

        self.label.grid(row=1, column=0, padx=10, pady=10)

        self.name = name


my_app = App()
