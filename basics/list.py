"""
 @author    : macab (macab@debian)
 @file      : list
 @created   : Thursday Mar 14, 2019 20:11:40 IST
"""

'''
List is a collection which is ordered and changeable. Allows duplicate members

'''
list = ["abdul", "waheed"]
#print(list)
"""
for item in list:
    print(item)

"""
# check whether a particular item is present in the list or not
'''
if "apple" in list:
    print (True)
else:
    print(False)
'''
#print length of the list
# print(len(list))

# append an item in the last of the list
# list.append("abdul")
# print(list)


#insert an item in the list at specific index it will simply replace that item
# if index is not valid it will insert at the end of the list
list.insert(10, "no one !")
# print(list)


# remove - method removes the particular item, error if element is not found !
# pop - removes the particular index item (last item if the  index is not specified
'''
list.remove("abdul")
print(list)
list.pop(0)
print(list)
'''
# del keyword removes the element from specified index, gives error if index is invalid !
# del list[10]
# print(list)

# del keyword can also delete the list completely
# del list
# print(list) # now will simple print an empty list


# clear method clears the list
list.clear()
print(list)













