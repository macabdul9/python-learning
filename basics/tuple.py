"""
 @author    : macab (macab@debian)
 @file      : tuples
 @created   : Thursday Mar 14, 2019 23:06:47 IST
"""

# tuples are in ()
mytuple = ("abdul", "waheed", "new")
#print(mytuple)

# difference between tuple and list list items are changable while tuple items unchangable
'''
mylist = ["abdul", "waheed", "new"]
mylist[0] = "eabdul"
mytuple[0] = "eabdul"  # this will give an error saying tuples , tuple item does not supports object assignment
print (mylist)
print(mytuple)
'''

'''
# loop through tuple
for item in mytuple:
    print(item)
'''

# adding items into the tuple
# adding items into the tuple is not possible becuase tuple is unchangable, hence there's no method to add an item

# short cut to see whether item is in tuple or not
print("ab" in mytuple)


