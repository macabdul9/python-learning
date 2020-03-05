"""
 @author    : macab (macab@debian)
 @file      : inheritance
 @created   : Saturday Mar 16, 2019 19:42:48 IST
"""
import os
clear = lambda:os.system('clear')
clear()


# parent class

class Vehicle:

    def category(self, category):
        self.category = category

    def color(self, color):
        self.color = color

class Car(Vehicle): # this is inheritance is achieved in python

    def name(self, name):
        self.name = name

    def printdata(self):
        print(self.category, self.color, self.name)


if __name__ ==  '__main__':
    c = Car()
    c.category("four wheelar")
    c.color('red')
    c.name('car')
    c.printdata()



