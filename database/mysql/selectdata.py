"""
 @author    : macab (macab@debian)
 @file      : selectdata
 @created   : Monday Mar 25, 2019 00:22:06 IST
"""


import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "macab",
    passwd = "Sudo$0#1",
    database = "pydb"
)

cursor = db.cursor()

# query = 'select * from users'

# cursor.execute(query)

# records = cursor.fetchall()

# for record in records:
#    print(record)

'''
# getting coloumn!

query = 'select user_name from users'
cursor.execute(query)
usernames = cursor.fetchall()
for username in usernames:
    for entries in username:
        print(entries)

'''

# getting more than one col.
query = 'select user_name, name from users'
cursor.execute(query)
pair = cursor.fetchall()
for tup in pair:
    for entry in tup:
        print(entry, end = " ")
    print()


