"""
 @author    : macab (macab@debian)
 @file      : generator2
 @created   : Saturday Mar 23, 2019 22:46:49 IST
"""

def generator(low, high):
    while low <= high:
        yield low
        low += 1

if __name__ == "__main__":
    for i in generator(5, 10):
        print(i)

