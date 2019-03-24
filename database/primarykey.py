"""
 @author    : macab (macab@debian)
 @file      : primarykey
 @created   : Sunday Mar 24, 2019 20:23:27 IST
"""

import mysql.connector as mysql

mydb = mysql.connect(host = '127.0.0.1', user = 'macab', passwd = 'Sudo$0#1', database = 'pydb')

# get a cursor
cursor = mydb.cursor()

# create a table having primary !

## creating the 'users' table again with the 'PRIMARY KEY'
cursor.execute("CREATE TABLE users (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), user_name VARCHAR(255))")

## 'DESC table_name' is used to get all columns information
cursor.execute("DESC users")

## it will print all the columns as 'tuples' in a list
print(cursor.fetchall())
