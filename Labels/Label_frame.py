import tkinter as tk

app = tk.Tk()
app.title("My App")
app.geometry("200x75")

labelframe = tk.LabelFrame(app, text="Label Frame", bg="black", relief=tk.SUNKEN, bd=4)
labelframe.pack()

button = tk.Button(labelframe, text="Button")
button.pack()

entry = tk.Entry(labelframe)
entry.pack()

app.mainloop()
