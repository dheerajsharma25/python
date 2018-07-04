# Write a python program
# using tkinter interface to take an input in the GUI program and print it.

import tkinter
from tkinter import *

root=Tk()

def show():
    print(entry.get())
def terminate():
    exit(0)

root.geometry('250x250')

entry=Entry(root,width=30)
entry.pack()

b1=Button(root,width=20,text='click',command=show)
b1.pack()

b2=Button(root,width=20,text='exit',command=terminate)
b2.pack()

root.mainloop()