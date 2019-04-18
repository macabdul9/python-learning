"""
 @author    : macab (macab@debian)
 @file      : insert
 @created   : Sunday Apr 14, 2019 19:41:31 IST
"""


import pymongo
import pprint

client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client.company

collection = db.tutors

data = { "Name" :"Abdul", "Age":19 }


x = collection.insert_one(data)

print(type(x))
print(x.inserted_id)
