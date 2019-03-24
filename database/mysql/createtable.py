"""
 @author    : macab (macab@debian)
 @file      : insert
 @created   : Sunday Mar 24, 2019 19:55:53 IST
"""

import mysql.connector as mysql

pydb = mysql.connect(
    host = '127.0.0.1',
    user = 'macab',
    passwd = 'Sudo$0#1',
    database = 'pydb'
)

# get a cursor first !
cursor = pydb.cursor()

## create a table in pydb database !
# make it comment now since database has been created !
# cursor.execute('CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255))')

# show tables in database
cursor.execute('SHOW TABLES')

# fetch the tables from database
tables = cursor.fetchall()

for table in tables:
    print(table)

