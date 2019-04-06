"""
 @author    : macab (macab@debian)
 @file      : jsonload
 @created   : Sunday Apr 07, 2019 02:50:12 IST
"""

import json

# json data

person = '{"name" : "Abdul Waheed", "languages" : ["Ci++", "Python"]}'

person_dict = json.loads(person)
print(person_dict['languages'])

