"""
 @author    : macab (macab@debian)
 @file      : delete
 @created   : Monday Mar 25, 2019 00:42:27 IST
"""


import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "macab",
    passwd = "Sudo$0#1",
    database = "pydb"
)

cursor = db.cursor()

# before delete
checkquery = 'select * from users'
cursor.execute(checkquery)
records = cursor.fetchall()
for record in records:
    for entry in record:
        print(entry, end = " ")
    print()

query = 'delete from users where name = "abdul" OR name = "Peter"'

cursor.execute(query)

cursor.execute(checkquery)
records = cursor.fetchall()
for record in records:
    for entry in record:
        print(entry, end = " ")
    print()


