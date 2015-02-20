__author__ = 'JayantArora'

from time import *

y = 32

class TimeTracker:

    def __init__(self):
        self.totalHours = 0
        self.month = strftime("%m")
        self.day = strftime("%d")
        self.weekdayName = strftime("%a")
        self.year = strftime("%y")

    def timeSpent(self, hours, minutes):
        self.totalHours = self.totalHours + hours + (minutes/60)
        return self.totalHours

    def CurrentDate(self):
        print(strftime("%m") + '/' + strftime("%d") + '/' + strftime("%y") + ' ' + strftime("%A"))
        global y
        print(y)

    def add(self):
        openFile = open("tasks.txt", "a")
        toWrite = [str(self.totalHours), " ", str(self.month), " ", str(self.day), " ", str(self.year), "\n"]
        openFile.writelines(toWrite)
        openFile.close()



#def main():

x = TimeTracker()
x.CurrentDate()
#print(strftime("%m") + "/" + strftime("%d") + "/" + strftime("%y"))
#x.add()
#global y


#main()
