"""
 @author    : macab (macab@debian)
 @file      : propertyfunction
 @created   : Monday Mar 18, 2019 23:23:24 IST
"""

class person:
    def __init__(self, name="Guest"):
        self.__name=name
    def setname(self, name):
        self.__name=name
    def getname(self):
        return self.__name


p1 = person()
print(p1.getname())
p1.setname('waheed')
print(p1.getname))

