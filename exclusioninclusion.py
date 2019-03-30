"""
 @author    : macab (macab@debian)
 @file      : exclusioninclusion
 @created   : Saturday Mar 30, 2019 14:20:22 IST
"""
import os
clear = lambda:os.system('clear')
clear()

def countsetbit(n):
    count = 0
    while n > 0:
        if n & 1:
            count += 1
        n >>= 1
    return count

#print(countsetbit(1))
# inclusion exclusion

# how many numbers upto 100 are divisible by an array elements ie: [2, 3, 5]

def inclexcl(arr, k):
    total = 0;
    for i in range(1, 1 << len(arr)):
        mask = i
        mul = 1;
        itr = 0
        setbits = countsetbit(i)
        while mask > 0:
            if mask & 1 :
                mul *= arr[itr]
            mask >>= 1
            itr += 1

        # if number of set bits are odd !
        if setbits & 1:
            total += k/mul
        # if number of set bits are even !
        else:
            total -= k/mul

    return total


if __name__ == "__main__":
    arr = [2, 11, 5, 7]
    print(inclexcl(arr, 100))

