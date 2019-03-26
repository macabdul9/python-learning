"""
 @author    : macab (macab@debian)
 @file      : sqlconnectivity
 @created   : Tuesday Mar 26, 2019 16:10:41 IST
"""

import mysql.connector as mysql

class mysqlconnect:
    def connection():
        db = mysql.connect(
            host = '127.0.0.1',
            user = 'macab',
            passwd = 'Sudo$0#1',
            database = 'login_module'
        )
        
