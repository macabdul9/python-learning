"""
 @author    : macab (macab@debian)
 @file      : insertdata
 @created   : Sunday Mar 24, 2019 20:41:18 IST
"""
import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "macab",
    passwd = "Sudo$0#1",
    database = "pydb"
)

cursor = db.cursor()

## defining the Query
query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"
## storing values in a variable
values = [
    ("Peter", "peter"),
    ("Amy", "amy"),
    ("Michael", "michael"),
    ("Hennah", "hennah")
]

## executing the query with values
cursor.executemany(query, values)

## to make final output we have to run the 'commit()' method of the database object
db.commit()

print(cursor.rowcount, "records inserted")

