"""
 @author    : macab (macab@debian)
 @file      : dbmethods
 @created   : Monday Mar 25, 2019 00:55:49 IST
"""



import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "macab",
    passwd = "Sudo$0#1",
    database = "pydb"
)

list_of_methods = db.__dir__()

print(list_of_methods)


