# Create a frame using tkinter
# with any label text and two buttons.One to exit and other to change the label to some other text.

import tkinter
from tkinter import *

root=Tk()

def show():
    var.set("hello python")

def terminate():
    exit(0)

var=StringVar()

root.geometry('250x250')
b1=Button(root,width=20,text='click',command=show)
b1.pack()

b2=Button(root,width=20,text='exit',command=terminate)
b2.pack()

var.set("hello world")
label=Label(root,textvariable=var,width=30)
label.pack()

root.mainloop()
