"""
 @author    : macab (macab@debian)
 @file      : trycatch
 @created   : Tuesday Mar 19, 2019 00:08:09 IST
"""

# exception handling
'''
try:
    a = 1/0
except:
    print("error !")
'''

try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
  print("operation done !")
except:
  print("Something went wrong when writing to the file")
