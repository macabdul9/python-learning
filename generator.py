"""
 @author    : macab (macab@debian)
 @file      : generator
 @created   : Saturday Mar 23, 2019 18:16:20 IST
"""

def generatorfun():
    yield 1
    yield 2


if __name__ == "__main__":
    x = generatorfun()
    # x is the generator object

    print(x.next())
    print(x.next())

