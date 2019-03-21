"""
 @author    : macab (macab@debian)
 @file      : writefile
 @created   : Wednesday Mar 20, 2019 22:46:12 IST
"""

def writefile():
    myfile = open('firstfile.txt', 'wt')
    myfile.write('adfhdsdssfsd\n')
    myfile.writelines('asfssdhd\n')
    myfile.write('sdfjhdsdasjdhfsdkasjfvd\n')
    myfile.write('dsdfdsf vdvscdc fvdvsd\n')
    myfile.write('fdjks')

if __name__ == "__main__":
    writefile()

