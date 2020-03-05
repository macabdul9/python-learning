"""
 @author    : macab (macab@debian)
 @file      : listcomprehension
 @created   : Monday Mar 18, 2019 22:21:49 IST
"""

# sperating char from a string
'''
char = []
for ch in "abdulwaheed":
    char.append(ch)

print(char)
'''

 # squares
'''
sqaures = [i*i for i in range(11)]
print(sqaures)
'''
# other list
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

mixed = [(x, y) for x in list1 for y in list2]
print(mixed)


