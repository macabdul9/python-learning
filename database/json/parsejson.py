"""
 @author    : macab (macab@debian)
 @file      : parsejson
 @created   : Sunday Apr 07, 2019 02:59:53 IST
"""

import json
with open('myjson.json') as f:
    data = json.load(f)

print(type(data))

print(data['quiz']['sport']['q1'].values())

