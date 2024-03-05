f4 = ttk.Frame(nb)
nb.add(f4, text='Tab4')
Label(f4, text= 'label').grid(column=2, row=0)
Label(f4, text= 'label1').grid(column=4, row=0)
Label(f4, text= 'label1').grid(column=6, row=2)

Label(f4, text= 'label1').grid(column=0, row=0)

Label(f4, text= 'label1').grid(column=0, row=2)
ee1 = tk.StringVar()
Entry(f4, textvariable=ee1, bg="yellow").grid(column=0, row=3)
Label(f4, text= 'label1').grid(column=0, row=4)
ee2 = tk.StringVar()
Entry(f4, textvariable=ee2, bg="yellow").grid(column=0, row=5)
ckb = tk.Checkbutton(text="Checkbutton1").grid(column=3, row=1)
ckb2 = tk.Checkbutton(text="Checkbutton2").grid(column=3, row=1)
ckb3 = tk.Checkbutton(text="Checkbutton3").grid(column=3, row=1)
ckb4 = tk.Checkbutton(text="Checkbutton4").grid(column=3, row=1)
ckb5 = tk.Checkbutton(text="Checkbutton5").grid(column=3, row=1)

menu = Menu(f4)

new_item = Menu(menu)

new_item.add_command(label='New')

menu.add_cascade(label='File', menu=new_item)

f4.config(menu=menu)

rb1 = tk.IntVar()
rb1.set(1)

radiobutton1 = tk.Radiobutton(f4, text="Radio 1", variable=rb1, value=1)
radiobutton1.grid(column=4, row1)

radiobutton2 = tk.Radiobutton(f4, text="Radio 2", variable=rb1, value=2)
radiobutton2.grid(column=5, row=1)
