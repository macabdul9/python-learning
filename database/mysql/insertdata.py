"""
 @author    : macab (macab@debian)
 @file      : insertdata
 @created   : Sunday Mar 24, 2019 20:41:18 IST
"""

import mysql.connector as mysql

mydb = mysql.connect(host = '127.0.0.1', user = 'macab', passwd = 'Sudo$0#1', database = 'pydb')

# get a cursor
cursor = mydb.cursor()

# first let's drop the primary for convenience !
# cursor.execute('ALTER TABLE users DROP id') deleted already !

query = 'INSERT INTO users(name,user_name) values(%s, %s)'
values = ('abdul', 'macab')

cursor.execute(query, values)

# inserting multiple values




## to make final output we have to run the 'commit()' method of the database object
mydb.commit()

print(cursor.rowcount, "record inserted")
