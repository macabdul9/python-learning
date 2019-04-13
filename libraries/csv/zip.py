"""
 @author    : macab (macab@debian)
 @file      : zip
 @created   : Sunday Apr 07, 2019 04:54:28 IST
"""

import zipfile

archive = zipfile.ZipFile('titanic.zip', 'r')

df = archive.read('titanic.csv')

print(df)

