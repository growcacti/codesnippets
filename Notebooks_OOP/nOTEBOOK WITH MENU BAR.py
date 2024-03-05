import tkinter as tk
from tkinter import ttk


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GUI")
        self.geometry("900x600")
        self.resizable(width=False, height=False)

        names = ["Tab_1", "Tab_2"]
        self.nb = self.create_notebook(names)
        self.menu = self.create_menus()

        mess_tab = self.nb.tabs["Tab_1"]

        mess_lbl_frm = ttk.LabelFrame(mess_tab, text="Label Frame")
        mess_lbl_frm.grid(row=0, column=0, sticky=tk.NSEW)

        mess_lbl = ttk.Label(mess_lbl_frm, text="This is a label")
        mess_lbl.grid(row=0, column=0)

        self.mainloop()

    def create_notebook(self, names):
        nb = MyNotebook(self, names)
        nb.grid(sticky=tk.NSEW)

        help_tab = nb.tabs["Tab_2"]
        help_lblfrm = ttk.Labelframe(help_tab, text="Tab_2")
        help_lblfrm.grid(row=0, column=0)
        help_lbl = ttk.Label(help_lblfrm, text="nothing here yet")
        help_lbl.grid(row=0, column=0, padx=106, pady=64)
        return nb

    def create_menus(self):
        menu = tk.Menu(self, tearoff=False)
        self.config(menu=menu)
        sub_menu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="File", menu=sub_menu)
        sub_menu.add_separator()
        sub_menu.add_command(label="Exit", command=self.destroy)
        return menu


class MyNotebook(ttk.Notebook):
    def __init__(self, master, names):
        super().__init__(master, width=897, height=595)
        self.tabs = {}
        for name in names:
            self.tabs[name] = tab = ttk.Frame(self)
            self.add(tab, text=name)


GUI()
