"""
 @author    : macab (macab@debian)
 @file      : projection
 @created   : Sunday Apr 14, 2019 23:34:52 IST
"""

import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.company
collection = db.students

# projection !
cursor = collection.find({_id:1})

while True:
    try:
        print(cursor.next())
    except:
        break

