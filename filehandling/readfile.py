"""
 @author    : macab (macab@debian)
 @file      : fileopen
 @created   : Wednesday Mar 20, 2019 22:32:41 IST
"""

'''

"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)


'''
def openfile():
    f = open('test.txt', 'r')

    # print(f.read());

    # read only some chars
    # print(f.read(5))

    # read line
    # print(f.readline())
    # print(f.readlines())

    # line by line:q
    
    for ch in f:
        print(ch)

    # don't forget to close the file
    f.close()


if __name__ == "__main__":
    openfile()

