import tkinter as tk

app = tk.Tk()
app.title("My App")
app.geometry("200x75")

variable = tk.IntVar()
variable.set(1)

radiobutton1 = tk.Radiobutton(app, text="Radio 1", variable=variable, value=1)
radiobutton1.pack()

radiobutton2 = tk.Radiobutton(app, text="Radio 2", variable=variable, value=2)
radiobutton2.pack()

app.mainloop()
