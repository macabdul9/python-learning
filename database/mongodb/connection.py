"""
 @author    : macab (macab@debian)
 @file      : connection
 @created   : Sunday Apr 14, 2019 03:51:43 IST
"""

import pymongo
import pprint
# connect to the local server of the database !
client = pymongo.MongoClient('mongodb://localhost:27017/')

#  get a database !
db = client.department

# get a collection !
collection = db.student

# pprint.pprint(collection.find_one())

#l = iter(docs)
'''
while True:
    val = next(l, 'end')
    if val != 'end':
        print(val)
    else:
        break
'''

cursor = collection.find()

while True:
    try:
        print(cursor.next())
    except:
        break
