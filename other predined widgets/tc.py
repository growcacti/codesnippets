#building a converter

from tkinter import *
#create main window and style it. Add a title, sizing etc
window=Tk()
window.title("Tempreture Converter")
window.configure(background="pink", relief="solid")
window.geometry("1000x500")

#define the function to convert your input F to C
def conversion():
    fahrenheit = float(en1.get())
    celsius = (5/9) * (float(fahrenheit) - 32)
    mytexbox["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

#define function to convert input C to F
def celcius_to_fahrenheit():

    c_input = float(en2.get())
    fahrenheit_calc = (float(c_input - 9/5) + 32)
    mytexbox["text"]= fahrenheit_calc, 2


#define function to enable entry 1, and disable entry 2.
def Fah_active():
    en1.configure(state="normal")
    en2.configure(state="disable")
#define function to enable entry 2 and disable entry 1.
def Cel_active():
    en2.configure(state="normal")
    en1.configure(state="disable")

#define function to delete your entries in both boxes as well as the result in the textbox.
def clear_function():
    en1.delete(0,END)
    en2.delete(0,END) #use this for clearing. use 'destroy' to exit.
    mytexbox.configure(text="")

#define function to stop and exit the program.
def close_window():
    window.destroy()

#create a groups/ frames in order to store the entry widget
group1 =LabelFrame(window, text="Fahrenheit to Celcius", padx=50, pady=20, bg="powderblue")
group1.grid(row=1, column=0)

group2 =LabelFrame(window, text="Celcius to Fahrenheit", padx=50, pady=20, bg="powderblue")
group2.grid(row=1, column=2)



#create the entry boxes for your input. PLace it into group 1 frame by calling group 1. Disable the entry so that it will only be enabled when the activate button is pushed
en1=Entry(group1)
en1.configure(state="disable")
en1.grid(row=3,column=0)


#do the same as you did for entry 1.
en2=Entry(group2)
en2.configure(state="disable")
en2.grid(row=3,column=2)

#create a label that displays your results.
mytexbox= Label(window, width=20, height=2)#never make results a textbox
mytexbox.grid(rows=8,column=1)

#create buttons to activate the entry boxes.
f_button=Button(window, text="Activate Fahrenheit", command=Fah_active)
f_button.grid(row=10,column=0)

c_button=Button(window, text="Activate Celcius", command=Cel_active)
c_button.grid(row=10,column=2)


#create button and call the conversion command in order to convert to celcius.
my_button=Button(window, text="Convert to Celcius", command=conversion)
my_button.grid(row=13,column=0)

my_button=Button(window, text="Convert to Fahrenheight", command=celcius_to_fahrenheit)
my_button.grid(row=13,column=2)

#create a button that calls the clear function to delete entries.
my_clearbutton=Button(window,text="Clear", command=clear_function)
my_clearbutton.grid(row=15,column=1)

#create button that calls the close window command to exit the program.
button = Button (text = "Exit", command = close_window)
button.grid(row=17, column=1)


window.mainloop()
