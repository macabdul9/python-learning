"""
 @author    : macab (macab@debian)
 @file      : test
 @created   : Friday Mar 22, 2019 23:05:33 IST
"""
import mysql.connector

mydb = mysql.connector.connect(user='macab', password='Sudo$0#1',
                              host='127.0.0.1',
                              #database='dbmslab'
        )

#print(cnx)

# get a cursor first
mycursor = mydb.cursor();

# create a database
# mycursor.execute('create database pydb')

# show database
mycursor.execute('show databases')

for x in mycursor:
    print(x)

mycursor.execute('use dbmslab')
mycursor.execute('show tables')

for x in mycursor:
    print(x)

mydb.close()
