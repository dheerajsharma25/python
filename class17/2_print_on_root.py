# Write a python program to in the same interface as above and create an
# action when the button is click it will display some text.

import tkinter
from tkinter import *

root=Tk()

def show():
    var.set("hello world")

def terminate():
    exit(0)

var=StringVar()

root.geometry('250x250')
b1=Button(root,width=20,text='click',command=show)
b1.pack()

b2=Button(root,width=20,text='exit',command=terminate)
b2.pack()

label=Label(root,textvariable=var,width=30)
label.pack()

root.mainloop()