"""
 @author    : macab (macab@debian)
 @file      : mymodule
 @created   : Saturday Mar 16, 2019 21:58:58 IST
"""

'''
Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your applicatio

'''

def reverse(mylist):
    back = len(mylist) - 1
    front = 0
    while front <= back:
        a = mylist[front]
        mylist[front] = mylist[back]
        mylist[back] = a
        front = front + 1
        back = back - 1



