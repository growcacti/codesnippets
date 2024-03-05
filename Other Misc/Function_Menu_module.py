import tkinter as tk


# Crude menu function module
# Might be able to use as a templete menu for other developing programs
# Most option I seen yet


def change_font(win):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))


def change_size(win):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))


font_combo.bind("<<ComboboxSelected>>", change_font)
size_combo.bind("<<ComboboxSelected>>", change_size)


# ****************buttons functionality
def change_bold():
    text_property = tk.font.Font(font=text_editor["font"])
    if text_property.actual()["weight"] == "normal":
        text_editor.configure(font=(current_font_family, current_font_size, "bold"))
    if text_property.actual()["weight"] == "bold":
        text_editor.configure(font=(current_font_family, current_font_size, "normal"))


bold_button.configure(command=change_bold)


# italic functionality
def change_italic():
    italic = tk.font.Font(font=text_editor["font"])
    if italic.actual()["slant"] == "roman":
        text_editor.configure(font=(current_font_family, current_font_size, "italic"))
    if italic.actual()["slant"] == "italic":
        text_editor.configure(font=(current_font_family, current_font_size, "roman"))


italic_button.configure(command=change_italic)


# underline functionality
def change_underline():
    underline = tk.font.Font(font=text_editor["font"])
    if underline.actual()["underline"] == 0:
        text_editor.configure(
            font=(current_font_family, current_font_size, "underline")
        )
    if underline.actual()["underline"] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, "normal"))


underline_button.configure(command=change_underline)


# color functionality
def color_change():
    color = tk.colorchooser.askcolor()
    text_editor.configure(fg=color[1])


font_color_button.configure(command=color_change)


# now we will do allignment
def left():
    text_content = text_editor.get(1.0, "end")
    text_editor.tag_config("left", justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "left")


align_left_button.configure(command=left)


def center():
    text_content = text_editor.get(1.0, "end")
    text_editor.tag_config("center", justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "center")


align_center_button.configure(command=center)


def right():
    text_content = text_editor.get(1.0, "end")
    text_editor.tag_config("right", justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "right")


align_right_button.configure(command=right)

text_editor.configure(font=("Arial", 12))
# # ***********************************************End of Text editor******************************************

# ************************************************Status bar***************************************************
status_bar = ttk.Label(win, text="Status Bar")
status_bar.pack(side=tk.BOTTOM)

text_changed = False


def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, "end-1c").split())
        characters = len(text_editor.get(1.0, "end-1c"))
        status_bar.config(text=f"Characters:{characters}  Words : {words} ")
    text_editor.edit_modified(False)


text_editor.bind("<<Modified>>", changed)
# ************************************************End of status bar********************************************

# ************************************************Main menu functionality***********************************
url = ""  # variable


# new functionality
def new_file(event=None):
    global url
    url = ""
    text_editor.delete(1.0, tk.END)


# file new command
file.add_command(
    label="New",
    image=new_icon,
    compound=tk.LEFT,
    accelerator="Ctrl+N",
    command=new_file,
)


# open functionality
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select File",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*")),
    )
    try:
        with open(url, "r") as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    win.title(os.path.basename(url))


# open command
file.add_command(
    label="Open",
    image=open_icon,
    compound=tk.LEFT,
    accelerator="Ctrl+O",
    command=open_file,
)
file.add_separator()


# functionality to save a file
def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, "w", encoding="utf-8") as wf:
                wf.write(content)
        else:
            url = filedialog.asksaveasfile(
                mode="w",
                defaultextension=".txt",
                filetypes=(("Text files", "*.txt"), ("All files", "*.*")),
            )
            content = text_editor.get(1.0, tk.END)
            url.write(content)
            url.close()
    except:
        return


# save command
file.add_command(
    label="Save",
    image=save_as_icon,
    compound=tk.LEFT,
    accelerator="Ctrl+S",
    command=save_file,
)


# save as functionality
def save_as(event=None):
    global url
    try:
        url = filedialog.asksaveasfile(
            mode="w",
            defaultextension=".txt",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*")),
        )
        content = text_editor.get(1.0, tk.END)
        url.write(content)
        url.close()
    except:
        return


# save as command
file.add_command(
    label="Save As",
    image=save_as_icon,
    compound=tk.LEFT,
    accelerator="Ctrl+S",
    command=save_as,
)
file.add_separator()


# Exit command functionality
def exit_fun(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel(
                "Warning!", "Do you want to save your file?"
            )
            if mbox:
                if url:
                    content = str(text_editor.get(1.0, tk.END))
                    with open(url, "w", encoding="utf-8") as wf:
                        wf.write(content)
                        win.destroy()
                else:
                    url = filedialog.asksaveasfile(
                        mode="w",
                        defaultextension=".txt",
                        filetypes=(("Text files", "*.txt"), ("All files", "*.*")),
                    )
                    content2 = text_editor.get(1.0, tk.END)
                    url.write(content2)
                    url.close()
                    win.destroy()
            elif mbox is False:
                win.destroy()
        else:
            win.destroy()
    except:
        return


# exit command
file.add_command(
    label="Exit",
    image=exit_icon,
    compound=tk.LEFT,
    accelerator="Ctrl+Z",
    command=exit_fun,
)


# edit commands adding functionality
# find functionality
def find_func(event=None):
    def find():
        word = find_input.get()
        text_editor.tag_remove("match", "1.0", tk.END)
        matches = 0
        if word:
            start_pos = "1.0"
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                text_editor.tag_add("match", start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config("match", foreground="red", background="yellow")

    def replace():
        word = find_input.get()
        replace_content = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_content)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)
