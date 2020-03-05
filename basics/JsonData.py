"""
 @author    : macab (macab@debian)
 @file      : json
 @created   : Monday Mar 18, 2019 23:37:27 IST
"""

'''
JSON is a syntax for storing and exchanging data.
JSON is text, written with JavaScript object notation.
'''
import json
# some JSON:

json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data = json.loads(json_string)
print(data)
