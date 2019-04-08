"""
 @author    : macab (macab@debian)
 @file      : arrays
 @created   : Monday Apr 08, 2019 22:40:08 IST
"""

import os
import numpy as np

clear = lambda:os.system('clear')
clear()

# creating array from a list
arr = np.array([1, 2, 3])
# prints array
print(arr)
# in numpy everything is ndarray
print(type(arr))
# print shape of the array
print(arr.shape)

