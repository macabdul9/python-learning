import numpy as np

# save a numpy array into a from

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.savetxt('out.txt', arr, delimiter = ', ')