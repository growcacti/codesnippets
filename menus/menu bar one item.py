import tkinter as tk


def quitCommand():
    quit()


app = tk.Tk()
app.title("My App")
app.geometry("200x75")

menubar = tk.Menu(app)
app.config(menu=menubar)

submenu = tk.Menu(menubar)
submenu.add_command(label="Quit", command=quitCommand)

menubar.add_cascade(label="Menu", menu=submenu)

app.mainloop()
