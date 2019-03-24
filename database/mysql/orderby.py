"""
 @author    : macab (macab@debian)
 @file      : orderby
 @created   : Monday Mar 25, 2019 00:39:36 IST
"""


import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "macab",
    passwd = "Sudo$0#1",
    database = "pydb"
)

cursor = db.cursor()

query = 'select name from users ORDER BY name DESC'

cursor.execute(query)
records = cursor.fetchall()

for record in records:
    for entry  in record:
        print(entry)
