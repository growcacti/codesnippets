import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.filedialog import askopenfilename
from tkinter import colorchooser
from tkinter import messagebox as mb
import os
import sys
import subprocess
import shutil
import runpy
class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Example")
        self.geometry('1800x900')

        self.notebook = ttk.Notebook(self)

        self.Frame1 = Frame1(self.notebook)
        self.Frame2 = Frame2(self.notebook)
        self.Frame3 = Frame3(self.notebook)
        self.Frame4 = Frame4(self.notebook)
        self.Frame5 = Frame5(self.notebook)
        self.Frame6 = Frame6(self.notebook)
        self.Frame7 = Frame7(self.notebook)
        self.Frame8 = Frame8(self.notebook)
        self.Frame9 = Frame9(self.notebook)
        self.Frame10 = Frame10(self.notebook)
        self.Frame11 = Frame11(self.notebook)
        self.Frame12 = Frame12(self.notebook)


        self.notebook.add(self.Frame1, text='View')
        self.notebook.add(self.Frame2, text='Edit')
        self.notebook.add(self.Frame3, text='Map')
        self.notebook.add(self.Frame4, text='Values')
        self.notebook.add(self.Frame5, text='Colors Fonts')
        self.notebook.add(self.Frame6, text='Info')
        self.notebook.add(self.Frame7, text='Generator')
        self.notebook.add(self.Frame8, text='Test')
        self.notebook.add(self.Frame9, text='Design')
        self.notebook.add(self.Frame10, text='GUI')
        self.notebook.add(self.Frame11, text='Lists')
        self.notebook.add(self.Frame12, text='Functions')
        self.notebook.grid(row=0,column=0)
        
    
        

class Frame1(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        self.labelA = ttk.Label(self, text = "Quick List Text Viewer")
        self.labelA.grid(column=2, row=0)
            
    try:
        self.showlistitems()

    

        local_path = Path(cwd)
        err_file = 'error_log.txt'
        self.text = tk.Text(self, height=60, width=200, bg='white')
        self.text.insert('1.0', tk.END)
        self.text.grid(row=0, column=5)
        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)
            

        self.scrollbar = tk.Scrollbar(f1)
        self.scrollbar.grid(row=0, column=6, sticky="nswe")
        self.scrollbar.config(command = text.yview)
        self.lb = tk.Listbox(f1, bg="light blue", exportselection=False, selectmode=tk.MULTIPLE)
        self.lb.grid(row=0, column=3, sticky="nswe")
        self.lb.focus()
        self.lb.configure(selectmode="")
        flist = os.listdir()
        for item in flist:
            self.lb.insert(tk.END, item)

        self.lb.bind("<<ListboxSelect>>", self.showcontent)
        self.lb.bind("<Double-Button-1>", self.opensystem)
        self.showlistitems()
    except Exception as ex:
        with open(local_path, 'w') as err_file:
            err_file.write(ex)







        def scrollbars():
            self.scrollbar = tk.Scrollbar(self._frame2)
            self.scrolbar.grid(column=2, row=0, sticky="nswe")

        def quit(self, evt=""):
            "Quit the window when press escape"
            self.save()
            self.root.destroy()



        def save(self):
            # "Saves the file selected in the listbox"
            if self.filename != "":
                try:
                    with open(f"{self.folder}/{self.filename}", "w") as file:
                        file.write(self._text.get("0.0", tk.END))
                except:

                    self.popup("Message", "Nothing selected")

        def delete(self):
            try:
                self.filename = self._lbx.get(self._lbx.curselection())
                os.remove(f"{self.folder}/{self.filename}")
                print(f"Deleted {self.folder}/{self.filename}")
                self.showlistitems()
            except OSError as e:
                        print("Failed with:" , e.sterror)
                        print("Error code:" , e.code)
            self._text.delete("0.0", tk.END)

        def input_filename(self,
            title="Enter a new name",
            sentence="Do not put the extension"):

            #tk.Tk().withdraw()
            name = simpledialog.askstring(title, sentence)
            try:
                if name != "":
                    return name + self.extension
            except TypeError:
                return ""
        


            
        def open_folder(self):
            "Open the folder of the selected file"
            # print(self.filename)
            os.startfile(self.folder)

        def quit(self, evt=""):
            "Quit the window when press escape"
            self.save()
            self.root.destroy()

        def newfile(self, evt):
            "Create a new file"
            self.save()
            self.newfilename = self.input_filename()
            if self.newfilename != "":
                with open(f"snippets/{self.newfilename}", "w", encoding="utf-8") as file:
                    pass
                self._lbx.insert(0, self.newfilename)

        def newfile2(self):
            "Create a new file"
            self.save()
            self.newfilename = self.input_filename()
            if self.newfilename != "":
                with open(f"{self.folder}/{self.newfilename}", "w", encoding="utf-8") as file:
                    pass
                self._lbx.insert(0, self.newfilename)
            return self.newfilename

        def showlistitems(self):
            self.lb.delete(0, tk.END)
            list_of_items = os.listdir(path)
            list_of_items.sort(reverse=True)
            # print(list_of_items)
            for file in list_of_items:
                if file.endswith(self.extension.lower()) or file.endswith(self.extension.upper()):
                    self.lb.insert(0, file)
                    self.lb.focus()

        def showcontent(self, evt):
            if self.extension != ".png":
                try:
                    filenum = self.lb.curselection()
                    self.filename = self.lb.get(filenum)
                    with open(f"{self.folder}/{self.filename}", "r", encoding="utf-8") as file:
                        content = file.read()
                        self.text.delete("0.0", tk.END)
                        self.text.insert(tk.END, content)
                except Exception as fx:
                    print("fx")
            else:
                pass
            
                     





























class Frame2(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        self.labelB = ttk.Label(self, text = "This is on Frame Two")
        self.labelB.grid(column=1, row=1)

class Frame3(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text = "This is on Frame3")
        self.labelc.grid(column=1, row=1)




class Frame4(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text = "This is on Frame3")
        self.labelc.grid(column=1, row=1)
        
class Frame5(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text = "This is on Frame3")
        self.labelc.grid(column=1, row=1)
class Frame6(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text = "This is on Frame3")
        self.labelc.grid(column=1, row=1)
class Frame7(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text = "This is on Frame3")
        self.labelc.grid(column=1, row=1)


class Frame8(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text = "This is on Frame3")
        self.labelc.grid(column=1, row=1)


class Frame9(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text = "This is on Frame3")
        self.labelc.grid(column=1, row=1)

class Frame10(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text = "This is on Frame3")
        self.labelc.grid(column=1, row=1)


class Frame11(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text = "This is on Frame3")
        self.labelc.grid(column=1, row=1)


class Frame12(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text = "This is on Frame3")
        self.labelc.grid(column=1, row=1)





















        
if __name__ == '__main__':
    app = MainApplication()
    app.mainloop()




    """


import tkinter as tk
from code.buttons import buttons
import glob

def window(self):
    "Contains all the widgets"
    
    def frame0():
        "Contains the text"
        self._frame0 = tk.Frame(self.root, bg="coral")
        self._frame0.grid(
            column=0,
            row=0,
            columnspan=2,
            sticky="nswe"
            )
        self._frame0.grid_rowconfigure(0, weight=0)
        self._frame0.grid_columnconfigure(0, weight=0)
        self._frame0.grid_columnconfigure(1, weight=0)
    
    def label_banner():
        "This is at 0,0 and occupies 2 column"
        # img = tk.PhotoImage(file=f"{self.folder}/banner.PNG")
        self.lb_banner = tk.Label(
            self._frame0,
            text=glob.glob("*book*.py")[-1],
            bg="coral")

        self.lb_banner.grid(
            column=0,
            row=0,
            columnspan=2,
            sticky="nswe"
            )

    def label_under_banner():
        "Contains the name of the file selected in the listbox on the left"
        # v. 2903 19.01.2021
        self.lb_under_banner = tk.Label(self._frame0, text=self.filename, bg="yellow")
        self.lb_under_banner.grid(
            column=0,
            row=1,
            columnspan=2,
            sticky="nswe"
            )

    def frame():
        "Contains the list of chapter names in listbox"
        self._frame = tk.Frame(self.root, bg="gray")
        self._frame.grid(column=0, row=1, sticky="nswe")
        for n in range(9):
            self._frame.grid_rowconfigure(n, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)
        # self._frame.grid_columnconfigure(1, weight=1)
    
    def frame2():
        "Contains the text"
        self._frame2 = tk.Frame(self.root, bg="coral")
        self._frame2.grid(column=1, row=1, sticky="nswe" )
        self._frame2.grid_rowconfigure(0, weight=1)
        # self._frame2.grid_rowconfigure(1, weight=1)
        self._frame2.grid_columnconfigure(0, weight=1, minsize=1)
    

    def listbox():
        "The book chapter name list goes here"
        self._lbx = tk.Listbox(
            self._frame,
            bg="yellow",
            exportselection=False # To mantain the selection in the listbox when you select in the text box
            # selectmode=tk.MULTIPLE
            )
        self._lbx.grid(
            column=0,
            row=0,
            sticky="nswe"
            ) # adapt the listbox to the frame
        # self._lbx.configure(selectmode="")
        self.showlistitems()

    def scrollbars():
        self.scrollbar = tk.Scrollbar(self._frame2)
        self.scrolbar.grid(column=2, row=0,
            sticky="nswe")

    def text():
        "Contains the text of selected chapter in listbox"
        self._text = tk.Text(self._frame2, wrap=tk.WORD)
        self._text.grid(column=0, row=0, sticky="nswe")
        self._text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self._text.yview)
        
    def widgets_order():
        "The widgets on the screen"
        frame0()
        frame()
        frame2()
        label_banner()
        label_under_banner()
        listbox()
        buttons(self) # code/buttons.py
        scrollbars()
        text()
        
    widgets_order()"""
