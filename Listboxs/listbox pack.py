import tkinter as tk

app = tk.Tk()
app.title("My App")
app.geometry("200x75")

listbox = tk.Listbox()
listbox.insert(1, "Python")
listbox.insert(2, "PHP")
listbox.insert(3, "JavaScript")
listbox.insert(4, "HTML")
listbox.pack()

app.mainloop()
