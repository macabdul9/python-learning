#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[22]:


# creating a 2D array

twodarr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(twodarr)


# In[23]:


# slicing
# slicing is quite similar to slicing of string
# first two rows 
print(twodarr[:2, 0:3])


# In[24]:


# rank 1 view of
row = twodarr[1, :]
col = twodarr[0:3, 0:1]
print(row)
print(row.shape)
print(col)
print(col.shape)


# In[32]:


# array of indices !
indices = np.array([0, 1, 2, 0])
print(twodarr[np.arange(3), indices])


# In[33]:


# Create a new array from which we will select elements
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
# Create an array of indices
b = np.array([0, 2, 0, 1])

# Select one element from each row of a using the indices in b
print(a[np.arange(4), b])  # Prints "[ 1  6  7 11]"


# In[ ]:




