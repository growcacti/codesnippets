import tkinter as tk

app = tk.Tk()
app.title("My App")
app.geometry("200x75")

checkbutton = tk.Checkbutton(text="Checkbutton")
checkbutton.pack()

app.mainloop()
