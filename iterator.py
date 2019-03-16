"""
 @author    : macab (macab@debian)
 @file      : iterator
 @created   : Saturday Mar 16, 2019 21:44:13 IST
"""

'''
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

'''

mylist = ["abdul", "waheed", "data", "scientist"]
myitr =  iter(mylist)

for item in myitr:
    print(item)


