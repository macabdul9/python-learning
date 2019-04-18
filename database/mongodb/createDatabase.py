"""
 @author    : macab (macab@debian)
 @file      : createDatabase
 @created   : Thursday Apr 18, 2019 23:17:42 IST
"""

import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

# list database names !

print(client.list_database_names())

db = client['college']

dblist = client.list_database_names()

if db in dblist:
    print("database 'college' is present in the database !")
else:
    print('college is not present in the database  ! ')
