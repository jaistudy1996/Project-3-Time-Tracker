#Aks

from tkinter import *
   

def new_win():
    
    newwin = Tk()
    newwin.geometry("600x300")
    newwin.title("Add New")
    
    back = Button(newwin, text = "Back")
    types = Label(newwin, text = "Types")
    time = Label(newwin, text = "Time")
    date = Label(newwin, text = "Date")
    
    
    x = StringVar()
    combo = OptionMenu(newwin, x, 'Combo', 'list')
    
    combo.pack()
    date.pack()
    types.pack()
    back.pack()
    time.pack()

    date.place(x = 35, y = 95, height=50, width=70)
    back.place(x = 40, y = 210, height=50, width=70)
    time.place(x = 55, y = 55, height=50, width=30)
    types.place(x = 5, y = 8, height=50, width=140)
   
    
    
    return newwin

if __name__ == "__main__":
    new_win()


    

