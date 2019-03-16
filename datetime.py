"""
 @author    : macab (macab@debian)
 @file      : datattime
 @created   : Sunday Mar 17, 2019 00:09:46 IST
"""

import datetime

x = datetime.datetime.now()
'''
print(x)
print(x.year)
print(x.strftime("%A"))
'''

# creating date object
date = datetime.datetime(2019, 03, 17)

print(date.strftime('%D'))

