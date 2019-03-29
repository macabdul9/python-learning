# training model !
import os
clear = lambda:os.system('clear')
clear()
def freqtable(input_data, k = 3):
    # frequency table initially empty
    table = {}
    for i in range(len(input_data) - k):
        ip = input_data[i : i + k] # input chunk
        op = input_data[i + k] # next char
        # if chunk is present in the table
        if ip in table:
            # if char already has some freq ! increase the freq by 1
            if op in  table[ip]:
                table[ip][op] += 1
            else:
                table[ip][op] = 1

        # if chunk is not there in frequency table !
        else:
            table[ip] = {
                op : 1
            }


    return table;

table = freqtable('hello world hello world hello hello')
print(table)
# for chunk in table:
#    print(chunk)


