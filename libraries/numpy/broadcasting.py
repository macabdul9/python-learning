#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[19]:


# let's create a two dimensional array !
x = np.array([[1, 2, 3], [3, 4, 5], [7, 8, 9], [10, 11, 12]])
print(x.shape)


# In[20]:


v = np.array([1, 2, 4])
print(v.shape)


# In[21]:


y = np.empty_like(x)
print(y.shape)
print(y)


# In[22]:


# Add the vector v to each row of the matrix x with an explicit loop
for each in range(4):
    y[each,:] = x[each, :] + v 


# In[23]:


print(y)


# In[ ]:




