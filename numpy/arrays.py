#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[21]:


arr = np.array([[1, 2, 4, 5], [1, 2, 5, 2], [5, 2, 4, 7], [5, 2, 4, 7]])


# In[22]:


print(arr)


# In[23]:


print(type(arr))


# In[17]:


print(arr.shape)


# In[26]:


print(arr[1][0], arr[2][1], arr[3][0])


# In[39]:


# zero matrics
zero = np.zeros((2,2))
print(zero)


# In[40]:


# unity matrics 
one = np.ones((3, 3))
print(one)


# In[31]:


# full matrix
full = np.full((3, 3), 5)
print(full)


# In[41]:


# identity matrix
identity = np.eye((3))
print(identity)


# In[46]:


# random array !
randarr = np.random.random((3,3))
print(randarr)


# In[ ]:





# In[ ]:





# In[ ]:




