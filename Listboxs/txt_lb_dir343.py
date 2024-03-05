text3 = tk.Text(f5, height=250, width=200, bg="wheat")
text3.insert("1.0", tk.END)
text3.grid(row=0, column=4, rowspan=25, columnspan=3)


lb = tk.Listbox(f5, bg="light blue")
lb.grid(row=0, column=0, sticky="nswe")
lb.focus()
lb.configure(selectmode="")
flist = os.listdir()
for item in flist:
    lb.insert(tk.END, item)
lb.bind("<Double-Button-1>", run)
lb.bind("<<ListboxSelect>>", showcontent)

btn30 = tk.Button(f5, text="dir", command=newdirlist)
btn30.grid(row=0, column=1)
