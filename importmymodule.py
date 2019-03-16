"""
 @author    : macab (macab@debian)
 @file      : importmymodule
 @created   : Saturday Mar 16, 2019 22:05:09 IST
"""

import mymodule

if __name__ == '__main__':
    mylist = [1, 2, 3, 4, 5]
    print(mylist)
    mymodule.reverse(mylist)
    print(mylist)