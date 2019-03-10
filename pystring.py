"""
 @author    : macab (macab@debian)
 @file      : string
 @created   : Saturday Mar 09, 2019 18:33:23 IST
"""

a = "hello"
#for i in a:
#    print(i)

#for i in range(a.__len__()):
#    print(a[i])

# substring of a string
# print(a[0:a.__len__()])

# The strip() method removes any whitespace from the beginning or the end:

#b = "  hello "
#print(b, b.__len__())
#b = b.strip()
#print(b, b.__len__())

#print(a.__len__())

# upper lower
print(a.lower(), a.upper())
a = a.replace('h', 'm')
print(a)
print(a.split(" "))

# entering input
name = input("")
print('Hello ! ', name)