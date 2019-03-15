"""
 @author    : macab (macab@debian)
 @file      : num
 @created   : Friday Mar 15, 2019 20:45:41 IST
"""


n = int(input())
sum = 0
for i in range(n):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print(sum)
