import tkinter as tk
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x500")
notebook = ttk.Notebook(root)
notebook.pack()

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
notebook.add(frame1, text="1")
notebook.add(frame2, text="2")
ttk.Button(frame2, text="Click me").pack()
frame3 = ttk.Frame(notebook)
notebook.add(frame3, text="3")
frame4 = ttk.Frame(notebook)
spinbox1 = ttk.Spinbox(frame4, from_=1, to=1000).pack(side=TOP)
spinbox2 = ttk.Spinbox(frame4, from_=1, to=1000).pack(side=LEFT)
spinbox3 = ttk.Spinbox(frame4, from_=1, to=1000).pack(side=RIGHT)
notebook.add(frame4, text="4")
frame5 = ttk.Frame(notebook)

# label text for title
label_combo = ttk.Label(frame5, text="GFG Combobox Widge").pack()

# label
ttk.Label(frame5, text="Select the Month :", font=("Times New Roman", 10)).pack(
    padx=10, pady=25
)

# Combobox creation
n = tk.StringVar()
monthchoosen = ttk.Combobox(frame5, width=27, textvariable=n)

# Adding combobox drop down list
monthchoosen["values"] = (
    " January",
    " February",
    " March",
    " April",
    " May",
    " June",
    " July",
    " August",
    " September",
    " October",
    " November",
    " December",
)

monthchoosen.pack(side=LEFT)
monthchoosen.current()
notebook.add(frame5, text="5")
frame6 = ttk.Frame(notebook)
notebook.add(frame6, text="6")
import glob
from time import sleep
import os

# from commit import commit
folder = "4ce"


class Ebook:
    def __init__(self, frame6, folder, js_link_to_html):
        """Define window for the app"""
        self.frame6 = frame6
        self.folder = folder
        self.js_link_to_html = js_link_to_html
        self.frame6.geometry("850x400")
        self.frame6["bg"] = "coral"
        self.menu()
        self.filelist()
        self.editor()
        self.frame6.bind("<Control-b>", lambda x: self.save_ebook())
        self.lstb.select_set(0)
        self.filename = self.lstb.get("active")
        self.index = self.lstb.curselection()
        self.show_text_in_editor()
        self.hidden = 0
        self.frame6bind()
        self.letter_size = 16

    def frame6bind(self):
        self.frame6.bind("<Control-l>", lambda x: self.hide())
        self.frame6.bind("<Control-minus>", lambda x: self.small_letters())
        self.frame6.bind("<Control-MouseWheel>", lambda x: self.wheel(x))

    # Widgets on the left ===============|
    def menu(self):
        """Listbox on the left with file names"""

        self.menubar = tk.Menu(self.frame6)
        # List of themes
        self.themes = tk.Menu(self.frame6)
        self.themes.add_command(label="Dark mode", command=self.dark)
        self.themes.add_command(label="Light mode", command=self.light)

        self.menubar.add_command(label="+", command=lambda: self.new_window(Win1))
        self.menubar.add_command(label="DELETE", command=lambda: self.delete_file())
        self.menubar.add_command(
            label="RENAME", command=lambda: self.new_window(Rename)
        )

        # ========= SUB RENDER ============
        self.menubar.add_command(label="Render Page", command=self.render_page)
        self.menubar.add_command(label="Render Ebook", command=self.save_ebook)

        self.menubar.add_command(label="SAVE", command=self.save)
        self.menubar.add_command(label="HELP", command=lambda: self.new_window(Help))
        self.menubar.add_cascade(label="THEME", menu=self.themes)
        # self.frame6.config(menu=self.menu_theme)
        self.frame6.config(menu=self.menubar)

    def filelist(self):
        self.frame1 = tk.Frame(self.frame6)
        self.frame1["bg"] = "coral"
        self.frame1.pack(side="left", fill=tk.BOTH)
        # self.frame1.pack()
        self.lstb = tk.Listbox(
            self.frame1, width=30
        )  # selectmode='multiple', exportselection=0)
        self.lstb["bg"] = "black"
        self.lstb["fg"] = "gold"
        self.lstb.pack(fill=tk.BOTH, expand=1)
        self.lstb.bind("<<ListboxSelect>>", lambda x: self.show_text_in_editor())
        self.lstb.bind("<F2>", lambda x: self.new_window(Rename))
        self.files = glob.glob(f"{self.folder}\\*.txt")
        # print("self.files", self.files)
        for file in self.files:
            self.lstb.insert(tk.END, file)
        self.lstb.bind("<Control-p>", lambda x: self.render_page())

    def hide(self):
        if self.hidden == 0:

            self.frame1.destroy()
            self.hidden = 1
        else:
            self.frame2.destroy()
            self.filelist()
            self.editor()
            self.lstb.select_set(self.index)
            self.show_text_in_editor()
            self.hidden = 0

    # Themes
    def dark(self):
        self.text["bg"] = "black"
        self.text["fg"] = "white"

    def light(self):
        self.text["bg"] = "darkgreen"
        self.text["fg"] = "white"
        self.text["font"] = "Arial 24"

    def big_letters(self):
        if self.letter_size < 72:
            self.letter_size += 2
        self.text["font"] = "Arial " + str(self.letter_size)

    def wheel(self, event):
        print(event.delta)
        if event.delta == 120:
            self.big_letters()
        else:
            self.small_letters()

    def small_letters(self):
        if self.letter_size > 8:
            self.letter_size -= 2
        self.text["font"] = "Arial " + str(self.letter_size)

    def delete_file(self):
        for num in self.lstb.curselection():
            filehtml = "{}.html".format(self.files[num][:-4])
            if os.path.exists(filehtml):  # because not all files are renered
                os.remove("{}.html".format(self.files[num][:-4]))
            os.remove(self.files[num])
        self.reload_list_files_delete()

    def editor(self):
        """The text where you can write"""
        self.frame2 = tk.Frame(self.frame6)
        self.frame2["bg"] = "coral"
        self.frame2.pack(side="left", fill=tk.Y)
        self.scrollbar = tk.Scrollbar(self.frame2)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.label_file_name = tk.Label(
            self.frame2, text="Editor - choose a file on the left"
        )
        self.label_file_name.pack(fill=tk.BOTH, expand=1)
        self.text = tk.Text(self.frame2, wrap=tk.WORD)
        self.text["bg"] = "darkgreen"
        self.text["fg"] = "white"
        self.text["font"] = "Arial 24"
        self.text.pack(fill=tk.Y, expand=1)
        self.text.bind("<Control-s>", lambda x: self.save())
        self.text.bind("<Control-p>", lambda x: self.render_page())
        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)

    def html_convert(self, text_to_render):
        """Convert to my Markup language"""
        html = "<style>body{margin:5%;font-size:2em;}</style>"
        text_to_render = text_to_render.split("\n")
        print(text_to_render)
        for line in text_to_render:
            if line != "":
                if line[0] == "*":
                    line = line.replace("*", "")
                    html += f"<h2>{line}</h2>"
                elif line[0] == "^":
                    line = line.replace("^", "")
                    html += f"<h3>{line}</h3>"
                elif line[0] == "#":
                    line = line.replace("#", "")
                    if line.startswith("http"):
                        html += f"<img src='{line}' /><br>"
                    else:
                        html += f"<img src='img\\{line}' /><br>"
                elif line[0] == "=" and line[1] == ">":
                    line = line.replace("=>", "")
                    html += f"<span style='color:red'>{line}</span>"
                else:
                    html += f"<p>{line}</p>"
        return html

    def new_window(self, _class):
        self.new = tk.Toplevel(self.frame6)
        _class(self.new)

    def new_chapter(self, filename):
        self.new.destroy()
        if not filename.endswith(".txt"):
            filename += ".txt"
        # os.chdir(f"{self.folder}")
        with open(f"{self.folder}\\" + filename, "w", encoding="utf-8") as file:
            file.write("")
        self.reload_list_files(filename)

    def reload_list_files(self, filename=""):
        # os.chdir("..")
        self.lstb.delete(0, tk.END)
        self.files = [f for f in glob.glob(f"{self.folder}\\*txt")]
        for file in self.files:
            self.lstb.insert(tk.END, file)
        self.lstb.select_set(self.files.index(f"{self.folder}\\" + filename))

    def reload_list_files_delete(self, filename=""):
        # os.chdir("..")
        self.lstb.delete(0, tk.END)
        self.files = [f for f in glob.glob(f"{self.folder}\\*txt")]
        for file in self.files:
            self.lstb.insert(tk.END, file)

    def rename(self, filename):
        # renames also the html rendered file if it exists
        self.current = self.lstb.get(tk.ACTIVE)[:-4]
        print(self.current)
        filehtml = "{}.html".format(self.current)
        print("=>", filename)
        print("==>", filehtml)
        if os.path.exists(filehtml):
            os.rename(filehtml, f"{self.folder}\\" + filename[:-4] + ".html")
        self.lstb.delete("active")
        os.rename(self.filename, f"{self.folder}\\" + filename)
        self.files = glob.glob(f"{self.folder}\\*.txt")
        self.reload_list_files(filename)

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            file.write(self.text.get("1.0", tk.END))
        self.label_file_name["text"] += "...saved"

    def save_ebook(self):
        html = ""
        with open("ebook.html", "w", encoding="utf-8") as htmlfile:
            for file in self.files:  # this is the name of each file
                with open(file, "r", encoding="utf-8") as singlefile:
                    # ================= SYMBOL => HTML ==============
                    html += self.html_convert(singlefile.read())
            htmlfile.write(html)
        self.label_file_name["text"] += "...Opening Ebook"
        os.startfile("ebook.html")

    def convert_if(self, read):
        if "#html_convert" in read:
            read = read.replace("#html_convert", "<!-- page converted -->")
            read = self.html_convert(read)
        else:
            pass  # convert this text in html with *^=>
        return read

    def render_page(self):
        """Save a single page v. 1.4 23/09/2019 at 05:40"""
        self.save()
        html = ""
        self.current = self.lstb.get(tk.ACTIVE)[:-4]  # The file selected without .txt
        with open(f"{self.current}.html", "w", encoding="utf-8") as htmlfile:
            # opend the active (selected) item in the listbox
            with open(f"{self.current}.txt", "r", encoding="utf-8") as readfile:
                read = readfile.read()  # get the text of the active file
                read = self.convert_if(read)  # searches for #html_convert tag
                htmlfile.write(read)  # create the new file with the rendered text
        self.create_newlinks()

    def create_newlinks(self):
        """This creates a list of links to the web pages created with render page"""
        with open("..\\{}.js".format(self.js_link_to_html), "w") as filejs:
            linka = str(self.lstb.get(tk.ACTIVE))
            linka = linka.split("\\")[1]
            self.current = self.current.split("\\")[1]

            # WE CAN HAVE MORE PYEMP FOR DIFFERENT CLASSES THAT SAVES INTO DIFFERENT self.FOLDERS
            # THEY WILL SHOW UP INTO DIFFERENT DIVS???
            # CREATE THE LINKS TO THE HTML PAGES SAVED AS SINGLE FILES
            listofhtml = []
            for file in os.listdir(f"{self.folder}"):
                if file.endswith(".html"):
                    listofhtml.append(file)
            html1 = ""

            for file in listofhtml:
                # I write the new link from the above list into the js file... then git commit to
                # have it on the web site
                # We will have a DIV THAT GETS THE LINKS FOR THIS PYEM AND RELATIVE self.FOLDER
                # WE NEED A DIV {} and a js file {}.js and a <script src="newlinks4ce"
                # just copy everything in index.html, put in place and copy th js fil
                html1 += """{}.innerHTML += "<a href='Programmi20192020/{}/{}'>{}</a><br>"
                """.format(
                    self.js_link_to_html, self.folder, file, file[:-5]
                )
            filejs.write(html1)

        self.label_file_name["text"] += "...page rendered +"
        os.startfile("{}\\{}.html".format(self.folder, self.current))
        os.system("start ../index.html")

    def show_text_in_editor(self):
        """Shows text of selected file in the editor"""
        self.index = self.lstb.curselection()
        if self.lstb.curselection() != ():
            # self.index = self.lstb.curselection()
            # index = self.lstb.curselection()[0]
            # self.filename = self.files[index] # instead of self.lstb.get(index)
            self.filename = self.lstb.get(self.index)
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read()
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, content)
            self.label_file_name["text"] = self.filename


class Rename:
    def __init__(self, frame6):
        self.frame6 = frame6
        self.frame6.geometry("300x100+200+200")
        self.frame6.title("Insert new file name")
        self.label_file_name = tk.Label(self.frame6, text="Enter a name")
        self.label_file_name.pack()
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self.frame6, textvariable=self.entry_var)
        self.entry.pack()
        self.entry.focus()
        self.entry_var.set(app.filename.split("\\")[1])
        self.entry.bind("<Return>", lambda x: app.rename(self.entry.get()))


class Win1:
    def __init__(self, frame6):
        self.frame6 = frame6
        self.frame6.geometry("300x100")
        self.frame6.title("Insert new file name")
        self.label_file_name = tk.Label(self.frame6, text="Enter a name")
        self.label_file_name.pack()
        self.entry = tk.Entry(self.frame6)
        self.entry.pack()
        self.entry.focus()
        self.entry.bind("<Return>", lambda x: app.new_chapter(self.entry.get()))


global js_link_to_html
# this file is in the frame6 folder of github.io where index.html is
"""
formazione.github.io
    |
    newlinks_4ce.js            # contains newlinks_4ce.innerHTML += "<a href='Programmi20192020/text_4ce/
                                    Compiti.html'>Compiti.html</a><br>" (made by create_newlinks called by
                                    render_page that renders the page in html in the folder called text)
    index.html                 # This calles the script above and has a div id=newlinks_4ce that loads the links
    programmi20192020
        |
        PyEbook_4CE_3b.py
        imgs
        text
            |
            file.txt
            file.htm

To create a new indipendent PyEbook that creates contents in html that will 
automatically go into index.html
1. Create the PyEbook
2. Change the js_link_to_html with the name of a js file in the frame6 of github.io
3. give a name to the folder (this creates a new folder for the html file)
4. Open index.html, call the js script with the name you choose in js_link_to_html
5. Create a div with the same name of the js file above without the .js
"""

# This folder is in the folder of this script;
# This script is into a folder (programmi20192020) of the frame6 folder of github.io

if __name__ == "__main__":
    #  checks if folders exists & creates them if not
    if f"{folder}" in os.listdir():
        print(f"{folder} folder exists")
    else:
        os.mkdir(f"{folder}")
        print(f"{folder} folder created")
    if "img" in os.listdir():
        print("img folder exists")
    else:
        os.mkdir("img")
        print(f"{folder} folder created")
    frame6 = tk.Tk()
    app = Ebook(frame6, "4ce", "newlinks_4ce_2020")
    app.frame6.title("4ce 2020 2021")
    frame6.mainloop()

frame7 = ttk.Frame(notebook)
notebook.add(frame7, text="7")
frame8 = ttk.Frame(notebook)
notebook.add(frame8, text="8")
frame9 = ttk.Frame(notebook)
notebook.add(frame9, text="9")
frame10 = ttk.Frame(notebook)
notebook.add(frame10, text="10")
frame11 = ttk.Frame(notebook)
notebook.add(frame11, text="11")
# disables the tab
# notebook.tab(0, state = 'disabled')
# entering and displaying multiple lines with the text widget
text = Text(frame1, width=100, height=100)
text.pack()
text2 = Text(frame2, width=100, height=100)
text2.pack()
text3 = Text(frame3, width=100, height=100)
text3.pack()
text4 = Text(frame4, width=10, height=10)
text4.pack()
text5 = Text(frame5, width=100, height=100)
text5.pack()
text6 = Text(frame6, width=100, height=100)
text6.pack()
text7 = Text(frame7, width=100, height=100)
text7.pack()
text8 = Text(frame8, width=100, height=100)
text8.pack()
text9 = Text(frame9, width=100, height=100)
text9.pack()
text10 = Text(frame10, width=100, height=100)
text10.pack()


def combo():
    window = tk.Tk()
    window.title("Combobox")
    window.geometry("250x150")

    # label text for title
    ttk.Label(
        window,
        text="GFG Combobox Widget",
        background="green",
        foreground="white",
        font=("Times New Roman", 15),
    ).grid(row=0, column=1)

    # label
    ttk.Label(window, text="Select the Month :", font=("Times New Roman", 10)).grid(
        column=0, row=5, padx=10, pady=25
    )

    # Combobox creation
    n = tk.StringVar()
    monthchoosen = ttk.Combobox(window, width=27, textvariable=n)

    # Adding combobox drop down list
    monthchoosen["values"] = (
        " January",
        " February",
        " March",
        " April",
        " May",
        " June",
        " July",
        " August",
        " September",
        " October",
        " November",
        " December",
    )

    monthchoosen.grid(column=1, row=5)
    monthchoosen.current()


# window = Tk()
# window.geometry('250x150')
def para_res():

    # --- functions ---
    # ---GUI for adding two resistors in parallel and in series
    # Future project with be with 3 or more resistors
    # Would also like to make a reverse calculation which give parallel resistor for ohm value desired
    def generate():
        try:
            con1 = 1 / float(num1.get())  # seems to work better if done in steps
            con2 = 1 / float(num2.get())  # con is for conductance
            consum = con1 + con2
            result = 1 / consum
            result2 = float(num1.get()) + float(
                num2.get()
            )  # using float is obvious way
        except Exception as ex:
            print(ex)
            result = "error"

        num3.set(result)
        num4.set(result2)

    root = tk.Tk()

    num1 = tk.StringVar()
    num2 = tk.StringVar()
    num3 = tk.StringVar()
    num4 = tk.StringVar()
    tk.Label(root, text=" Input R1:").grid(row=0, column=0)
    tk.Label(root, text="Input R2:").grid(row=1, column=0)
    tk.Label(root, text=" Output Parallel:").grid(row=2, column=0)
    tk.Label(root, text="Output Series:").grid(row=3, column=0)

    tk.Entry(root, textvariable=num1).grid(row=0, column=1)
    tk.Entry(root, textvariable=num2).grid(row=1, column=1)
    tk.Entry(root, textvariable=num3).grid(row=2, column=1)
    tk.Entry(root, textvariable=num4).grid(row=3, column=1)
    button = tk.Button(root, text="Calculate", command=generate)
    button.grid(row=4, column=1)

    root.mainloop()


if __name__ == "__main__":
    mainloop()
