"""
 @author    : macab (macab@debian)
 @file      : set
 @created   : Thursday Mar 14, 2019 23:17:03 IST
"""

# set - A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets
# A set is exactly like a set in cpp , no duplicate , no ordering, use hashing.

#myset = {"apple", "orange", "banana", "nothing else !"}
#print(myset)

# index based element access is not possible in set
# print(myset[0]) # this is throw an error saying set object does not support indexing

# check whether item is present in my set
# print("apple" in myset) same apply for tuple and list


# remove and discard are the two methods to remove and item
# the only differene bw them is remove throw an error when item is present
# in the set while discard doesnt

# another method to remove an item is pop() but bcoz its an unordered list
# hence you we dont know which item will be remove pop removes the last item
set_1 = {1, 3, 5, 23}
set_2 = {34, 3, 5, 10}
#print(set_1.intersection(set_2)) # this will give intersection of set_1 and set_2





