"""
 @author    : macab (macab@debian)
 @file      : whereclause
 @created   : Monday Mar 25, 2019 00:33:42 IST
"""


import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "macab",
    passwd = "Sudo$0#1",
    database = "pydb"
)

cursor = db.cursor()

query = "select name from users where user_name = 'macab'"

cursor.execute(query)

records = cursor.fetchall()

for record in records:
    for entry in record:
        print(entry)


