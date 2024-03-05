text4 = tk.Text(f4, height=250, width=200, bg="wheat")
text4.insert("1.0", tk.END)
text4.grid(row=0, column=4, rowspan=25, columnspan=3)


lb4 = tk.Listbox(f4, bg="light blue")
lb4.grid(row=0, column=0, sticky="nswe")
lb4.focus()
lb4.configure(selectmode="")
flist = os.listdir()
for item in flist:
    lb2.insert(tk.END, item)
lb4.bind("<Double-Button-1>", run)
lb4.bind("<<ListboxSelect>>", showcontent)

btn31 = tk.Button(f4, text="dir", command=dirsel)
btn31.grid(row=0, column=1)
