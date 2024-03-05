import tkinter as tk


root = tk.Tk()
# create the widget.  Make sure to save a reference.
text = tk.Text(root)

# insert a string at the beginning
text.insert("1.0", "I love  text widget!")

# insert a string into the current text
text.insert("1.2", "REALLY ")

# get the whole string
text.get("1.0", tk.END)

# delete the last character.
# Note that there is always a newline character
# at the end of the input, so we backup 2 chars.
text.delete("end - 2 chars")


text.grid(row=0, column=1)
root.mainloop()
