"""
 @author    : macab (macab@debian)
 @file      : showdatabase
 @created   : Sunday Mar 24, 2019 18:37:14 IST
"""


import mysql.connector as mysql

mydb = mysql.connect(
    host = '127.0.0.1',
    user = 'macab',
    passwd = 'Sudo$0#1'
)


cursor = mydb.cursor()
cursor.execute('show databases')
# 'fetchall()' method fetches all the rows from the last executed statement # it returns a list of all databases present
database_list = cursor.fetchall()
for x in database_list:
    print(x)

# show tables
