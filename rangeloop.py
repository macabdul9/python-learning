"""
 @author    : macab (macab@debian)
 @file      : rangeloop
 @created   : Thursday Mar 14, 2019 21:26:15 IST
"""

if __name__ == '__main__':
    n = int(input())

result = 0

for i in range(1, n + 1):
    result = result*10 + i;
    print(result)
    #print(i, result)
    print (i)

print(result)

