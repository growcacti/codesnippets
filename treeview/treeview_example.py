from tkinter import *
from tkinter import ttk

root = Tk()
root.title("JH examples")
root.geometry("400x300")
root["bg"] = "#fb0"

tv = ttk.Treeview(root)
tv["columns"] = ("WTF", "Name", "Whatever")
tv.column("#0", width=0, stretch=NO)
tv.column("WTF", anchor=CENTER, width=80)
tv.column("Name", anchor=CENTER, width=80)
tv.column("Whatever", anchor=CENTER, width=80)

tv.heading("#0", text="", anchor=CENTER)
tv.heading("WTF", text="Id", anchor=CENTER)
tv.heading("Name", text="WTF", anchor=CENTER)
tv.heading("Whatever", text="Whatever", anchor=CENTER)

tv.insert(parent="", index=0, iid=0, text="", values=("1", "Vineet", "Alpha"))
tv.insert(parent="", index=1, iid=1, text="", values=("2", "Anil", "Bravo"))
tv.insert(parent="", index=2, iid=2, text="", values=("3", "Vinod", "Charlie"))
tv.insert(parent="", index=3, iid=3, text="", values=("4", "Vimal", "Delta"))
tv.insert(parent="", index=4, iid=4, text="", values=("5", "Manjeet", "Echo"))
tv.pack()


root.mainloop()
