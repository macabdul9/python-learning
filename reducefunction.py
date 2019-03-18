"""
 @author    : macab (macab@debian)
 @file      : reducefunction
 @created   : Monday Mar 18, 2019 22:16:52 IST
"""

'''
Like the map and filter functions, the reduce() function receives
two arguments, a function and an iterable. However, it doesn't return
another iterable, instead it returns a single value.
'''
import functools
def mult(x,y):
    print("x=",x," y=",y)
    return x*y

fact=functools.reduce(mult, range(1, 4))
print ('Factorial of 3: ', fact)

