"""
 @author    : macab (macab@debian)
 @file      : jsonload
 @created   : Sunday Apr 07, 2019 02:50:12 IST
"""

import json

# json data

person = '{"name" : "Abdul Waheed", "languages" : ["C++", "Python"]}'

person_dict = json.loads(person)
print(person_dict)

for entry in person_dict:
    print(entry.encode("ascii","replace"))

