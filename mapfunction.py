"""
 @author    : macab (macab@debian)
 @file      : mapfunction
 @created   : Monday Mar 18, 2019 22:05:50 IST
"""


'''
The map() function calls the specified function for each item of an iterable
(such as string, list, tuple or dictionary) and returns a list of results.
'''

def square(x):
    return x*x

numbers = [1, 2, 3, 4, 5]

sqrList = map(square, numbers)
print(sqrList)

# map with lambda

sqrList2 = map(lambda x:x*x, numbers)

print(sqrList2)
