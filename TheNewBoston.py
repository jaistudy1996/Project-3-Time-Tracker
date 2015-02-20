__author__ = 'JayantArora'

from tkinter import *

root = Tk()

myLabel = Label(root, text="This is a label")
myLabel.grid(columnspan=4, sticky=N)

label2 = Label(root, text="This is what I call using a rowspan")
label2.grid(row=1, columnspan=4, sticky=N)


root.mainloop()