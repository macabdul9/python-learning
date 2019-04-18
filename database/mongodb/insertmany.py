"""
 @author    : macab (macab@debian)
 @file      : insertmany
 @created   : Friday Apr 19, 2019 02:17:52 IST
"""

import pymongo
import pprint

client = pymongo.MongoClient('mongodb://localhost:27017')

db  = client['company']

collection = db['tutors']


mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

x = collection.insert_many(mylist)

pprint.pprint(x.inserted_ids)


