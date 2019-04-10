#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# In[6]:


# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3*np.pi, 0.1)
y = np.sin(x)


# In[8]:


plt.plot(x, y)
plt.show()


# In[ ]:




