"""
 @author    : macab (macab@debian)
 @file      : magicmethod
 @created   : Monday Mar 18, 2019 23:28:43 IST
"""

'''
Magic methods in Python are the special methods which add "magic" to your
class. Magic methods are not meant to be invoked directly by you, but the
invocation happens internally from the class on a certain action. For example,
when you add two numbers using the + operator,internally, the __add__() method
will be called.
'''

num = 10
num.__add__(20)
print(num)

