# Akshay Singh

from tkinter import *
from page2 import new_win

# def window():
#     frame = Tk()
#     frame.geometry("600x300")
#     frame.title("Main")
#     return frame

def main():
    #frame = window()

    root = Tk()
    root.geometry("600x300")
    root.title("Main")


    activity = Button(root, text="Add New Activity", command=new_win)
    events = Button(root, text="Events")
    report = Button(root, text="Reports")


    activity.place(x=20, y=210, height=100, width=140)
    events.place(x=230, y=210, height=100, width=140)
    report.place(x=440, y=210, height=100, width=140)

    root.mainloop()

main()
    



   


    
