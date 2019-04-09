#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# let's create a two dimensional array !
x = np.array([[1, 2, 3], [3, 4, 5], [7, 8, 9]])
print(x.shape)


# In[3]:


v = np.array([1, 2, 4])
print(v.shape)


# In[10]:


z = np.empty_like(x)
print(z.shape)
print(z)


# In[ ]:


# add the vector v to the each row of z
for each in range(4):
    z[1,:] = 


# In[ ]:




