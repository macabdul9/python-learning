"""
 @author    : macab (macab@debian)
 @file      : jsondump
 @created   : Sunday Apr 07, 2019 03:07:31 IST
"""

import json


person_dict = {'name': 'Abdul',
'age':200,
'children': None
}
person_json = json.dumps(person_dict)

# Output: {"name": "Bob", "age": 12, "children": null}
print(person_json)

my_dict = {
    "name":"abdul waheed",
    "rollno":"00196407218",
    "branch":"computer science and engineering",
    "group":"c7"
}

print(my_dict)

with open('my_dict.json', 'w') as fp:
    json.dump(my_dict,  fp)

