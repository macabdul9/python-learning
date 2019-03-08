# is given string pallindrom means on reversing string remains same

# iterative
# def ispallindrome(s):
#     a = s.__len__()
#     if a < 2:
#         return True
#
#     for i in range(int(a/2)):
#         if s[i] != s[a - 1 - i]:
#             return False
#     return True

def ispallindrome(s, itr, len):
    if len < 2 or itr >= int(len/2):
        return True
    if s[itr] != s[len - 1 - itr]:
        return False
    return  ispallindrome(s, itr + 1, len)


t = int(input())
while t > 0 :
    s = input('')
    print(ispallindrome(s, 0, s.__len__()))
    t -= 1

