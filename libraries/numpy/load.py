import numpy as np

# loading array from text file

arr = np.genfromtxt('in.txt', skip_header = 0)
print(arr)