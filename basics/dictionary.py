"""
 @author    : macab (macab@debian)
 @file      : dictionary
 @created   : Thursday Mar 14, 2019 23:43:17 IST
"""

'''
A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly
brackets, and they have keys and values.

'''
mydict ={
    1 : "abdul",
    2 : "waheed",
    1 : "no one !"
}
# print(mydict)

# accessing item : we can access item by
#print(mydict[0]) # if key is not present in the dict it will throw an error
# or get()

# x = mydict.get(30) # it wont throw error like that if key is not there in mydict

'''
# iteration throw loop
for key in mydict:
    print(key)# this will give key
for value in mydict.values():
    print(value)
for item in mydict.items():
    print(item)

'''
# check if key is present
# print(1 in mydict)

# adding item into the dictionary
# mydict[3] = "no one!"
print(mydict)

# removing item
mydict.pop(1)
print(mydict)

# popitem removes the random item while del mydict[] works same as pop


# duplicate keys are not allowed in dictionary , later value gets added !


