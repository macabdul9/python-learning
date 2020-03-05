"""
 @author    : macab (macab@debian)
 @file      : countsetbits
 @created   : Saturday Mar 30, 2019 18:59:20 IST
"""

def countsetbits(n):
    count = 0
    while n > 0:
        count += 1
        n = n & (n - 1)
    return count

print(countsetbits(7))

