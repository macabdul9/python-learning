"""
 @author    : macab (macab@debian)
 @file      : dataFrame
 @created   : Friday May 24, 2019 19:20:34 IST
"""

import pandas as pd

data ={
    "companies" :["Google", "Apple", "Facebook", "Microsoft", "Tesla", "Ford", "Samsung", "Huawei", "Nestle",
                  "Walmart"],
    "marketValue" :[980, 1020, 540, 670, 130, 129, 356, 350, 120, 490],
    "founder":["Lary Page", "Steve Jobs", "Mark Zuckerberg", "Bill Gates", "Elon Musk", "Micheal Ford", "Someone",
               "Someone", "Someone",  "Someone"],
    "revenue" : [100, 120, 30, 67, 20, 30, 80, 90, 34, 135]
}


df = pd.DataFrame(data)

# print(df["founder"])
# print(df)


print(df["revenue"].median())
