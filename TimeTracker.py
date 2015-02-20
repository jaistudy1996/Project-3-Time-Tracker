__author__ = 'JayantArora'

from tkinter import *
#from tkinter import ttk


def printName(event):
    print("This is your name!")
    try:
        comboValue = str(comboVar.get())
        print(comboValue)
    except:
        print("Sorry")

def main():
    root = Tk()
    root.title("Time Tracker Tool")

    # mainframe = Frame(root, width=500, height=500)
    # mainframe.columnconfigure(0, weight=1)
    # mainframe.rowconfigure(0, weight=1)
    # mainframe.pack()

    heading = Label(root, text="Time Tracker Tool")
    # heading.grid(row=0, columnspan=5, sticky=N)
    heading.pack()

    eventsButton = Button(root, text="Events")
    # eventsButton.place(x = 50, y = 50)
    # eventsButton.grid(row=2, column=0, padx=20, pady=20)
    eventsButton.pack()

    okayButton = Button(root, text="OK")
    # okayButton.grid(row=2, column=5, padx=20, pady=20)
    okayButton.bind("<Button-1>", printName)
    okayButton.pack()

    global comboVar
    comboVar = StringVar()
    combo = OptionMenu(root, comboVar, 'lions', 'tigers', 'bear')
    combo.pack()

    root.mainloop()


main()


