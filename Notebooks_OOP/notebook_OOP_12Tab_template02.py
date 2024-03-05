import tkinter as tk
from tkinter import ttk

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Code Inspection project")
        self.geometry('1800x900')

        self.notebook = ttk.Notebook(self)

        self.Frame1 = Frame1(self.notebook)
        self.Frame2 = Frame2(self.notebook)
        self.Frame3 = Frame3(self.notebook)
        self.Frame4 = Frame4(self.notebook)
        self.Frame5 = Frame5(self.notebook)
        self.Frame6 = Frame6(self.notebook)
        self.Frame7 = Frame7(self.notebook)
        self.Frame8 = Frame8(self.notebook)
        self.Frame9 = Frame9(self.notebook)
        self.Frame10 = Frame10(self.notebook)
        self.Frame11 = Frame11(self.notebook)
        self.Frame12 = Frame12(self.notebook)


        self.notebook.add(self.Frame1, text='View')
        self.notebook.add(self.Frame2, text='Edit')
        self.notebook.add(self.Frame3, text='Map')
        self.notebook.add(self.Frame4, text='Values')
        self.notebook.add(self.Frame5, text='Colors Fonts')
        self.notebook.add(self.Frame6, text='Info')
        self.notebook.add(self.Frame7, text='Generator')
        self.notebook.add(self.Frame8, text='Test')
        self.notebook.add(self.Frame9, text='Snips')
        self.notebook.add(self.Frame10, text='GUI')
        self.notebook.add(self.Frame11, text='Lists')
        self.notebook.add(self.Frame12, text='Functions')
        self.notebook.grid(row=0,column=0)












        
class Frame1(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        self.labelA = ttk.Label(self, text = "This is on Frame One")
        self.labelA.grid(column=1, row=1)

class Frame2(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        self.labelB = ttk.Label(self, text = "This is on Frame Two")
        self.labelB.grid(column=1, row=1)

class Frame3(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text = "This is on Frame3")
        self.labelc.grid(column=1, row=1)




class Frame4(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text = "This is on Frame4")
        self.labelc.grid(column=1, row=1)
        
class Frame5(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text = "This is on Frame5")
        self.labelc.grid(column=1, row=1)
class Frame6(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text = "This is on Frame6")
        self.labelc.grid(column=1, row=1)
class Frame7(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text = "This is on Frame7")
        self.labelc.grid(column=1, row=1)


class Frame8(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text = "This is on Frame8")
        self.labelc.grid(column=1, row=1)


class Frame9(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text = "This is on Frame9")
        self.labelc.grid(column=1, row=1)

class Frame10(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text = "This is on Frame10")
        self.labelc.grid(column=1, row=1)


class Frame11(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text = "This is on Frame11")
        self.labelc.grid(column=1, row=1)


class Frame12(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text = "This is on Frame12")
        self.labelc.grid(column=1, row=1)





















        
if __name__ == '__main__':
    app = MainApplication()
    app.mainloop()
