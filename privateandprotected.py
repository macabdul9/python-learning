"""
 @author    : macab (macab@debian)
 @file      : privateandprotected
 @created   : Monday Mar 18, 2019 22:43:49 IST
"""

'''
implementation of private and protected fields(var or method)
'''
''' Python's convention to make an instance variable protected is to add a prefix _
(single underscore) to it. This effectively prevents it to be accessed, unless it
is from within a sub-class.
'''
# protected
class Student:
    def __init__(self, name, rollNo):
        self._name = name
        self._rollNo = rollNo


s = Student('Waheed', 001)
print(s._name, s._rollNo)
s._name = 'Abdul'
s._rollNo = 2
print(s._name, s._rollNo)

class Info:
    s = Student('a', 1)
    print(s._rollNo)

i = Info()

# double underscore is used to get the private fields
