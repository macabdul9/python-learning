"""
 @author    : macab (macab@debian)
 @file      : digit
 @created   : Sunday Apr 07, 2019 02:47:31 IST
"""

def ispresent(num, digit):
     while num > 0:
             if num%10 == digit:
                     break
             num /= 10
     return num > 0


