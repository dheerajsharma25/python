# Write a python program using tkinter interface to write Hello World and
# a exit button that closes the interface.

import tkinter
from tkinter import *

root=Tk()

def show():
    print("hello world")
def terminate():
    exit(0)
root.geometry('250x250')
b1=Button(root,width=20,text='click',command=show)
b1.pack()

b2=Button(root,width=20,text='exit',command=terminate)
b2.pack()

root.mainloop()

