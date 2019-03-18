"""
 @author    : macab (macab@debian)
 @file      : RegExp
 @created   : Monday Mar 18, 2019 23:52:37 IST
"""

'''
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern
'''

import re

txt = "My name is Khan"
#x = re.split("a", txt)

x  =re.sub("\s", "a", txt)
print(x)
