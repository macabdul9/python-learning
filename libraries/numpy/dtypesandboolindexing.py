#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[8]:


arr = np.array([[5, 2], [2, 3], [4, 5]])
b_index = (arr > 2)
print(b_index)


# In[13]:


# another magic
print(arr[b_index])


# In[14]:


# data types 
print(arr.dtype)


# In[ ]:




