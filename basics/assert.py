"""
 @author    : macab (macab@debian)
 @file      : assert
 @created   : Sunday Mar 17, 2019 00:28:58 IST
"""

'''
Python provides the assert statement to check if a given logical expression is true or false. Program execution proceeds
only if the expression is true and raises the AssertionError when it is false. The following code shows the usage of the
assert statement.It is much like an if-else
'''

x = int(input())
assert x >= 0
print(x)

