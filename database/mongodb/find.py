"""
 @author    : macab (macab@debian)
 @file      : find
 @created   : Friday Apr 19, 2019 23:13:19 IST
"""

import pymongo
import pprint

client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client .company
collection = db.tutors

x = collection.find_one({"Name" :"Abdul"})
print(x)

