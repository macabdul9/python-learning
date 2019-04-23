#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


# creating series with pandas
df = pd.Series([1, 2, 3, None, 4, 5])


# In[4]:




# In[5]:


# date range with pandas
dates = pd.date_range('20190422', periods = 10)


# In[6]:


dates


# In[7]:


df = pd.DataFrame(np.random.randn(10, 5), index = dates, columns = list('12345'))
# the above process is called data genration and organizing data into strucutred manner
df


# In[8]:


# Creating a DataFrame by passing a dict of objects that can be converted to series-like

df2 = pd.DataFrame({
                     'A':pd.Timestamp('20190423'),
                     'B':1.,
                     'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                     'D': np.array([3] * 4, dtype='int32'),
                     'E': pd.Categorical(["test", "train", "test", "train"]),
                     'F': 'foo'
    })


# In[9]:


df2


# In[10]:


df2.dtypes


# In[11]:


# veiwing data
df.head()


# In[12]:


df.index


# In[13]:


df2.index


# In[14]:


df.columns


# In[15]:


print(df.to_numpy())



# In[ ]:




