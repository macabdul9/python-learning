"""
 @author    : macab (macab@debian)
 @file      : readcsv
 @created   : Sunday Apr 07, 2019 05:01:02 IST
"""

import csv
import pandas as pd


df = pd.read_csv('titanic.csv', dtype={'uid':str})
# before  modifying
print(df)
string = df.to_string(header=False,index=False)
#after modifying
print(string)

