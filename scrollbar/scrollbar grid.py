import tkinter as tk

app = tk.Tk()
app.title("My App")

text = tk.Text(height=5,width=50)
text.grid(row=0, column=0, sticky='ew')

scrollbar = tk.Scrollbar(command=text.yview)
scrollbar.grid(row=0, column=1, sticky='ns')

text['yscrollcommand'] = scrollbar.set

app.mainloop()
