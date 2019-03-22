"""
 @author    : macab (macab@debian)
 @file      : file
 @created   : Saturday Mar 23, 2019 00:19:58 IST
"""

#myfile = open('queries.txt', 'w')
#myfile.write('sjdfb csdd dds sdj\n')
#myfile.write('sdhds vdsjj dvsd vds\n')

r = open('queries.txt', 'r')
for line in r:
    for words in line.split():
        print(words, end="")


