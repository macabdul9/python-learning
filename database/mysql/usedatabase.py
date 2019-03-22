"""
 @author    : macab (macab@debian)
 @file      : usedatabase
 @created   : Friday Mar 22, 2019 23:49:04 IST
"""

import mysql.connector

mydb  = mysql.connector.connect(
    host = 'localhost',
    user = 'macab',
    passwd = 'Sudo$0#1',
    database = 'pydb'
)

cursor = mydb.cursor()

# use the database
cursor.execute('use pydb')

# create the  table

#cursor.execute('create table schedule(task_id int not null, task_name varchar(100), task_period float(10,3), timing varchar(100))')

# update the table

# cursor.execute('update schedule add timing varchar(10)')

#cursor.execute('show tables')
#for tables in cursor:
#    print(tables)

# insert the values into table

cursor.execute('insert into schedule(task_id, task_name, task_period, timing) values(1, "sleeping", 6.0, "02:00-08:30")')
cursor.execute('insert into schedule(task_id, task_name, task_period, timing) values(2, "fresh&breakfast", 0.5, "08:30-09:00")')
cursor.execute('insert into schedule(task_id, task_name, task_period, timing) values(3, "study", 4.5, "09:00-13:30")')
cursor.execute('insert into schedule(task_id, task_name, task_period, timing) values(4, "lunch", 0.5, "13:30-14:00")')
cursor.execute('insert into schedule(task_id, task_name, task_period, timing) values(5, "rest", 1.0, "14:00-15:00")')
cursor.execute('insert into schedule(task_id, task_name, task_period, timing) values(6, "study", 3.0, "15:00-18:00")')
cursor.execute('insert into schedule(task_id, task_name, task_period, timing) values(7, "snack&break", 1.0, "18:00-19:00")')
cursor.execute('insert into schedule(task_id, task_name, task_period, timing) values(8, "study", 2.0, "19:00-21:00" )')
cursor.execute('insert into schedule(task_id, task_name, task_period, timing) values(9, "dinner&break", 1.0, "21:00-22:00")')
cursor.execute('insert into schedule(task_id, task_name, task_period, timing) values(10, "study", 4.0, "22:00-02:00")')


# get the whole table
cursor.execute('select * from schedule')
for x in cursor:
    print(x)

# run some fucking queries !

cursor.execute('select sum(task_period) from schedule where task_name = "study"')

for x in cursor:
    print(x)





mydb.close()

