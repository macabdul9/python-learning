"""
 @author    : macab (macab@debian)
 @file      : droptable
 @created   : Sunday Mar 24, 2019 20:12:13 IST
"""

import mysql.connector as mysql

database = mysql.connect(
    host = '127.0.0.1',
    user = 'macab',
    passwd = 'Sudo$0#1',
    database = 'pydb'
)
# get a cursor

cursor = database.cursor()

cursor.execute('DROP TABLE users')


