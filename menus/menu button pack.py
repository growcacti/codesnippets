import tkinter as tk

app = tk.Tk()
app.title("My App")
app.geometry("200x75")

menubutton = tk.Menubutton(text="Menubutton")
menubutton.pack()

menu = tk.Menu(menubutton, tearoff=False)
menu.add_radiobutton(label="Menu 1")
menu.add_radiobutton(label="Menu 2")

menubutton["menu"] = menu

app.mainloop()
