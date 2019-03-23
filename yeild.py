"""
 @author    : macab (macab@debian)
 @file      : yeild
 @created   : Saturday Mar 23, 2019 15:39:28 IST
"""

def test():
    yield 1
    yield 2
    yield 3

if __name__ == "__main__":
    for i in test():
        print(i)

