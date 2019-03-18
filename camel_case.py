"""
 @author    : macab (macab@debian)
 @file      : camel_case
 @created   : Tuesday Mar 19, 2019 00:06:42 IST
"""

import camelcase

c = camelcase.CamelCase()

txt = "hello world ! hows ewf thats"

print(c.hump(txt))

