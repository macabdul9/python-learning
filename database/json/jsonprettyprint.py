"""
 @author    : macab (macab@debian)
 @file      : jsonprettyprint
 @created   : Sunday Apr 07, 2019 03:15:31 IST
"""


import json

person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'

# Getting dictionary
person_dict = json.loads(person_string, encoding='utf-8')

# Pretty Printing JSON string back
print(json.dumps(person_dict, indent = 4, sort_keys=True))

# Printing dictionary
print(person_dict)

