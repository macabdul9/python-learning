"""
 @author    : macab (macab@debian)
 @file      : filterfunction
 @created   : Monday Mar 18, 2019 22:09:22 IST
"""

import math as m
import os
clear =  lambda:os.system('clear')
clear()
'''
The filter() function calls the specified function which
returns boolen for each item of the specified iterable (list)
'''

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(m.sqrt(x))):
        if x%i == 0:
            return False
    return True


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
prime = filter(isPrime, numbers)

print(prime)
