"""
 @author    : macab (macab@debian)
 @file      : stringsubset
 @created   : Saturday Mar 23, 2019 18:29:59 IST
"""


def stringsubset(s, ans):
    
    if len(s) == 0:
        print(ans)
        return

    stringsubset(s[1:len(s)], ans)

    ans = ans + s[0]
    stringsubset(s[1:len(s)], ans)


if __name__ == "__main__":
    s = input()
    stringsubset(s, " ")

