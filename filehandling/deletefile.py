"""
 @author    : macab (macab@debian)
 @file      : deletefile
 @created   : Thursday Mar 21, 2019 12:54:15 IST
"""

import os

if __name__ == "__main__":
    if os.path.exists("demofile.txt"):
        os.remove("demofile.txt")
    else:
        print("The file does not exist")

