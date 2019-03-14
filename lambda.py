"""
 @author    : macab (macab@debian)
 @file      : lambda
 @created   : Friday Mar 15, 2019 00:05:12 IST
"""

'''
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.isinstance
'''

#x = lambda a : a/2
#print(x(10))  # 10/2 = 5 it will return 5

#x = lambda a, b, c: a + b + c
#print(x(10, 20, 30))

'''
Why Use Lambda Functions?

The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

'''
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(13))



