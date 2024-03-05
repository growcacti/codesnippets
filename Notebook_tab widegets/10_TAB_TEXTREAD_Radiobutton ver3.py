import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import scrolledtext, Toplevel, Menu, LabelFrame
from tkinter import *
import os
import sys

# import subprocess
# import shutil
import string
from PIL import Image, ImageTk
import string
from string import *
import itertools
import collections
from collections import *
from collections import Counter
from string import ascii_lowercase


root = tk.Tk()

root.geometry("500x500")

notebook = ttk.Notebook(root)

top = Toplevel()
top.geometry("300x300+300+700")


notebook.grid(row=0, column=0)

frame1 = ttk.Frame(notebook)


menubar = Menu(root)
root.config(menu=menubar)


def openfile():

    filepath = askopenfilename(
        filetypes=[("All Files", "*.*"), ("Text Files", "*.txt"), ("Python", "*.py")]
    )

    if not filepath:

        return
    with open(filepath, "r") as f:
        text = f.read()

        def selection():
            nonlocal text
            choice = var.get()
            with open(filepath, "r") as f:
                text = f.read()
                if choice == 1:
                    text1.insert("1.0", text)
                elif choice == 2:
                    text2.insert("1.0", text)

                elif choice == 3:
                    text3.insert("1.0", text)

                elif choice == 4:
                    text4.insert("1.0", text)

                elif choice == 5:
                    text5.insert("1.0", text)

                elif choice == 6:
                    text6.insert("1.0", text)

                elif choice == 7:
                    text7.insert("1.0", text)

                elif choice == 8:
                    text8.insert("1.0", text)

                elif choice == 9:
                    text9.insert("1.0", text)

                elif choice == 10:
                    text10.insert("1.0", text)

                elif choice == 11:
                    text11.insert("1.0", text)

                elif choice == 12:
                    text22.insert("1.0", text)

                elif choice == 13:
                    text23.insert("1.0", text)

                elif choice == 14:
                    text210.insert("1.0", text)

                elif choice == 15:
                    text211.insert("1.0", text)
                    text = text211

    top = Toplevel()

    frm1 = LabelFrame(top)
    frm1.grid(row=0, column=0, rowspan=2)
    frm2 = LabelFrame(frm1, text=" ", padx=30, pady=10)

    var = IntVar()
    rb1 = Radiobutton(
        frm2, text="From 1", variable=var, value=1, command=selection
    ).grid(row=2, column=2)
    rb2 = Radiobutton(
        frm2, text="From 2", variable=var, value=2, command=selection
    ).grid(row=3, column=2)
    rb3 = Radiobutton(
        frm2, text="From 3", variable=var, value=3, command=selection
    ).grid(row=4, column=2)

    rb4 = Radiobutton(
        frm2, text="From 4", variable=var, value=4, command=selection
    ).grid(row=5, column=2)
    rb5 = Radiobutton(
        frm2, text="From 5", variable=var, value=5, command=selection
    ).grid(row=6, column=2)
    rb6 = Radiobutton(
        frm2, text="From 6", variable=var, value=6, command=selection
    ).grid(row=7, column=2)

    rb7 = Radiobutton(
        frm2, text="From 7", variable=var, value=7, command=selection
    ).grid(row=8, column=2)
    rb8 = Radiobutton(
        frm2, text="From 8", variable=var, value=8, command=selection
    ).grid(row=9, column=2)
    rb9 = Radiobutton(
        frm2, text="From 9", variable=var, value=9, command=selection
    ).grid(row=10, column=2)
    rb10 = Radiobutton(
        frm2, text="From 10", variable=var, value=10, command=selection
    ).grid(row=11, column=2)
    rb11 = Radiobutton(
        frm2, text="From 11", variable=var, value=11, command=selection
    ).grid(row=12, column=2)
    rb12 = Radiobutton(
        frm2, text="From 12", variable=var, value=12, command=selection
    ).grid(row=13, column=2)
    rb13 = Radiobutton(
        frm2, text="From 13", variable=var, value=13, command=selection
    ).grid(row=14, column=2)
    rb14 = Radiobutton(
        frm2, text="From 14", variable=var, value=14, command=selection
    ).grid(row=15, column=2)
    rb15 = Radiobutton(
        frm2, text="From 15", variable=var, value=15, command=selection
    ).grid(row=16, column=2)
    frm2.grid(row=3, columnspan=3, padx=30)

    text = selection()


##
##
##            text10.insert('1.0', text)
##        btn1=tk.Button(top, text='Tab1', command=lambda: tabin(x=1))
##        btn1.grid(column=0, row=1)
##        btn2=tk.Button(top, text='Tab2', command=lambda: tabin(x=2))
##        btn2.grid(column=0, row=2)
##        btn3=tk.Button(top, text='Tab3', command=lambda: tabin(x=3))
##        btn3.grid(column=0, row=3)
##        btn4=tk.Button(top, text='Tab4', command=lambda: tabin(x=4))
##        btn4.grid(column=0, row=4)
##        btn5=tk.Button(top, text='Tab5', command=lambda: tabin(x=5))
##        btn5.grid(column=0, row=5)
##        btn6=tk.Button(top, text='Tab 6', command=lambda: tabin(x=6))
##        btn6.grid(column=0, row=6)
##        btn7=tk.Button(top, text='Tab 7', command=lambda: tabin(x=7))
##        btn7.grid(column=0, row=7)
##        btn8=tk.Button(top, text='Tab 8', command=lambda: tabin(x=8))
##        btn8.grid(column=0, row=8)
##        btn9=tk.Button(top, text='Tab 9', command=lambda: tabin(x=9))
##        btn9.grid(column=0, row=9)
##        btn10=tk.Button(top, text='Tab 10', command=lambda: tabin(x10))
##        btn10.grid(column=0, row=10)


def savefile(x):

    if x == 1:

        text = text1.get("1.0", tk.END)

    elif x == 2:

        text = text2.get("1.0", tk.END)

    elif x == 3:

        text = text3.get("1.0", tk.END)

    elif x == 4:

        text = text4.get("1.0", tk.END)

    elif x == 5:

        text = text5.get("1.0", tk.END)

    elif x == 6:

        text = text6.get("1.0", tk.END)

    elif x == 7:

        text = text7.get("1.0", tk.END)

    elif x == 8:

        text = text8.get("1.0", tk.END)

    elif x == 9:

        text = text9.get("1.0", tk.END)

    elif x == 10:

        text = text10.get("1.0", tk.END)

        text11.insert("1.0", text)

    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("Python", "py"), ("All Files", "*.*")],
    )

    if not filepath:

        return

    with open(filepath, "w") as f:

        text = text11.get(1.0, tk.END)

        f.write(text)


def quit():
    if tk.messagebox.askokcancel("Quit?", "Really quit?"):
        root.quit()
        root.destory()


def new_file(event=None):

    global file_name

    file_name = None

    text.delete(1.0, END)


def open_file(event=None):

    input_file_name = tk.filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
    )

    if input_file_name:

        global file_name

        file_name = input_file_name

        text.delete("1.0", tk.END)

        with open(file_name) as f:

            text.insert("1.0", f.read())


def save_file(event=None):

    global file_name

    if not file_name:

        save_as_file()

    else:

        write_to_file(file_name)

    return "break"


def save_as_file(event=None):

    input_file_name = tk.filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
    )

    if input_file_name:

        global file_name

        file_name = input_file_name

        write_to_file(file_name)

    return "break"


def write_to_file(file_name):

    try:

        content = text.get("1.0", tk.END)

        with open(file_name, "w") as the_file:

            the_file.write(content)

    except IOError:

        pass


def cut():

    text.event_generate("<<Cut>>")


def copy():

    text.event_generate("<<Copy>>")


def paste():

    text.event_generate("<<Paste>>")


def undo():

    text.event_generate("<<Undo>>")


def redo(event=None):

    text.event_generate("<<Redo>>")

    return "break"


def find_func(event=None):
    def find():
        word = find_input.get()
        text.tag_remove("match", "1.0", tk.END)
        matches = 0
        if word:
            start_pos = "1.0"
            while True:
                start_pos = text.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                text.tag_add("match", start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text.tag_config("match", foreground="red", background="yellow")

    def replace():
        word = find_input.get()
        replace_content = replace_input.get()
        content = text.get(1.0, tk.END)
        new_content = content.replace(word, replace_content)
        text.delete(1.0, tk.END)
        text.insert(1.0, new_content)

    find_dialog = tk.Toplevel()
    find_dialog.geometry("450x250+500+200")
    find_dialog.title("Find")
    find_dialog.resizable(0, 0)

    find_frame = ttk.Labelframe(find_dialog, text="Find/Replace")
    find_frame.grid(row=1, column=1)

    # labels
    text_find_label = ttk.Label(find_frame, text="Find: ")
    text_replace_label = ttk.Label(find_frame, text="Replace")
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)
    # entry boxes
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)
    # buttons
    find_button = ttk.Button(find_frame, text="Find", command=find)
    replace_button = ttk.Button(find_frame, text="Replace", command=replace)
    find_button.grid(row=2, column=0, padx=4, pady=4)
    replace_button.grid(row=2, column=1, padx=4, pady=4)


def find(event=None):

    search_top_level = Toplevel(root)

    search_top_level.title("Find Text")

    search_top_level.transient(root)

    Label(search_top_level, text="Find All:").grid(row=0, column=0, sticky="e")

    search_entry_widget = Entry(search_top_level, width=25)

    search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky="we")

    search_entry_widget.focus_set()

    ignore_case_value = IntVar()

    Checkbutton(search_top_level, text="Ignore Case", variable=ignore_case_value).grid(
        row=1, column=1, sticky="e", padx=2, pady=2
    )

    Button(
        search_top_level,
        text="Find All",
        underline=0,
        command=lambda: search_output(
            search_entry_widget.get(),
            ignore_case_value.get(),
            text,
            search_top_level,
            search_entry_widget,
        ),
    ).grid(row=2, column=2, sticky="e" + "w", padx=2, pady=2)

    def close_search_r():

        text.tag_remove("match", "1.0", END)

        search_top_level.destroy()

        search_top_level.protocol("WM_DELETE_WINDOW", close_search_root)

        return "break"


def search_output(needle, if_ignore_case, text, search_top_level, search_box):

    text.tag_remove("match", "1.0", tk.END)

    matches_found = 0

    if needle:

        start_pos = "1.0"

        while True:

            start_pos = text.search(
                needle, start_pos, nocase=if_ignore_case, stopindex=END
            )

            if not start_pos:

                break

            text.tag_add("match", start_pos, end_pos)

            matches_found += 1

            start_pos = end_pos

            text.tag_config("match", foreground="red", background="yellow")

            search_box.focus_set()

            search_top_level.title("{} matches found".format(matches_found))


def select_all(event=None):

    text.tag_add("sel", "1.0", tk.END)

    return "break"


btn11 = tk.Button(top, text="Tab1 save", command=lambda: savefile(1))
btn11.grid(column=2, row=1)
btn12 = tk.Button(top, text="Tab2 Save", command=lambda: savefile(2))
btn12.grid(column=2, row=2)
btn13 = tk.Button(top, text="Tab3 Save", command=lambda: savefile(3))
btn13.grid(column=2, row=3)
btn14 = tk.Button(top, text="Tab4 Save", command=lambda: savefile(4))
btn14.grid(column=2, row=4)
btn15 = tk.Button(top, text="Tab5 Save", command=lambda: savefile(5))
btn15.grid(column=2, row=5)
btn16 = tk.Button(top, text="Tab 6 Save", command=lambda: savefile(6))
btn16.grid(column=2, row=6)
btn17 = tk.Button(top, text="Tab 7 Save", command=lambda: savefile(7))
btn17.grid(column=2, row=7)
btn18 = tk.Button(top, text="Tab 8 Save", command=lambda: savefile(8))
btn18.grid(column=2, row=8)
btn19 = tk.Button(top, text="Tab 9 Save", command=lambda: savefile(9))
btn19.grid(column=2, row=9)
btn20 = tk.Button(top, text="Tab 10 Save", command=lambda: savefile(10))
btn20.grid(column=2, row=10)


frame1.rowconfigure(0, minsize=800, weight=1)

frame1.columnconfigure(1, minsize=800, weight=1)


text1 = scrolledtext.ScrolledText(frame1)

text1.grid(row=0, column=1, sticky="nsew")

frame2 = ttk.Frame(notebook)

notebook.add(frame1, text="1")

notebook.add(frame2, text="2")


frame2.rowconfigure(0, minsize=800, weight=1)

frame2.columnconfigure(1, minsize=800, weight=1)


text2 = scrolledtext.ScrolledText(frame2)

text2.grid(row=0, column=1, sticky="nsew")


f3 = ttk.Frame(notebook)

notebook.add(f3, text="3")


text3 = scrolledtext.ScrolledText(f3, height=250, width=100, bg="wheat")

text3.insert("1.0", tk.END)

text3.grid(row=0, column=4, rowspan=25, columnspan=10)

f4 = ttk.Frame(notebook)

notebook.add(f4, text="4")

f5 = ttk.Frame(notebook)


notebook.add(f5, text="5")

f6 = ttk.Frame(notebook)

notebook.add(f6, text="6")

f7 = ttk.Frame(notebook)

notebook.add(f7, text="7")

f8 = ttk.Frame(notebook)

notebook.add(f8, text="8")

f9 = ttk.Frame(notebook)

notebook.add(f9, text="9")

f10 = ttk.Frame(notebook)

notebook.add(f10, text="10")

f11 = ttk.Frame(notebook)

notebook.add(f11, text="11")

text10 = scrolledtext.ScrolledText(f10, height=250, width=100, bg="wheat")

text10.insert("1.0", tk.END)

text10.grid(row=0, column=4, rowspan=25, columnspan=10)

text11 = scrolledtext.ScrolledText(f11, height=250, width=100, bg="wheat")

text11.insert("1.0", tk.END)

text11.grid(row=0, column=4, rowspan=25, columnspan=10)

text4 = scrolledtext.ScrolledText(f4, height=250, width=300, bg="orange")

text4.insert("1.0", tk.END)


text4.grid(row=0, column=4, rowspan=25, columnspan=10)

text5 = scrolledtext.ScrolledText(f5, height=250, width=300, bg="white")

text5.insert("1.0", tk.END)

text5.grid(row=0, column=4, rowspan=25, columnspan=10)

text6 = scrolledtext.ScrolledText(f6, height=250, width=100, bg="white")

text6.insert("1.0", tk.END)

text6.grid(row=0, column=4, rowspan=25, columnspan=10)

text7 = scrolledtext.ScrolledText(f7, height=250, width=100, bg="light blue")

text7.insert("1.0", tk.END)

text7.grid(row=0, column=4, rowspan=25, columnspan=10)

text8 = scrolledtext.ScrolledText(f8, height=250, width=100, bg="pink")

text8.insert("1.0", tk.END)

text8.grid(row=0, column=4, rowspan=25, columnspan=10)

text9 = scrolledtext.ScrolledText(f9, height=250, width=100, bg="light green")

text9.insert("1.0", tk.END)

text9.grid(row=0, column=4, rowspan=25, columnspan=10)


file_menu = Menu(menubar, tearoff=0)

file_menu.add_command(
    label="New", accelerator="Ctrl+N", compound="left", underline=0, command=new_file
)

file_menu.add_command(
    label="Open", accelerator="Ctrl+O", compound="left", underline=0, command=open_file
)

file_menu.add_command(
    label="Save", accelerator="Ctrl+S", compound="left", underline=0, command=save_file
)

file_menu.add_command(
    label="Save As",
    accelerator="Shift+Ctrl+S",
    compound="left",
    underline=0,
    command=save_as_file,
)

file_menu.add_command(
    label="Exit", accelerator="Alt+F4", compound="left", underline=0, command=quit
)

menubar.add_cascade(label="File", menu=file_menu)


edit_menu = Menu(menubar, tearoff=0)

edit_menu.add_command(
    label="Cut", accelerator="Ctrl+X", compound="left", underline=0, command=cut
)

edit_menu.add_command(
    label="Copy", accelerator="Ctrl+C", compound="left", underline=0, command=copy
)

edit_menu.add_command(
    label="Paste", accelerator="Ctrl+V", compound="left", underline=0, command=paste
)

edit_menu.add_command(
    label="Undo", accelerator="Ctrl+Z", compound="left", underline=0, command=undo
)

edit_menu.add_command(
    label="Redo", accelerator="Ctrl+Y", compound="left", underline=0, command=redo
)

edit_menu.add_command(
    label="Find", accelerator="Ctrl+F", compound="left", underline=0, command=find
)

edit_menu.add_command(
    label="Find/Replace",
    accelerator="Ctrl+R",
    compound="left",
    underline=0,
    command=find_func,
)

edit_menu.add_command(
    label="Select All",
    accelerator="Ctrl+A",
    compound="left",
    underline=7,
    command=select_all,
)

menubar.add_cascade(label="Edit", menu=edit_menu)


root.protocol("WM_DELETE_r", quit)

root.config(menu=menubar)


##

btn111 = tk.Button(top, text="Open File", command=openfile)
btn111.grid(column=3, row=1)
if __name__ == "__main__":
    root.mainloop()
