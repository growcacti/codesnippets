import tkinter as tk

app = tk.Tk()
app.title("My App")
app.geometry("200x75")

spinbox = tk.Spinbox(from_=0,to=50)
spinbox.pack()

app.mainloop()
