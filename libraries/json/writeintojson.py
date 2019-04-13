"""
 @author    : macab (macab@debian)
 @file      : writeintojson
 @created   : Sunday Apr 07, 2019 03:21:47 IST
"""

import json

data = {'people':[{'name': 'Scott', 'website': 'stackabuse.com', 'from': 'Nebraska'}]}


with open('myjson.json', 'w') as fp:
    json.dump(data, fp)
