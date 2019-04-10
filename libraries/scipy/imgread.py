#!/usr/bin/env python
# coding: utf-8

# In[22]:


from scipy.misc import imread, imsave, imresize, imshow


# In[23]:

img = imread('cat.jpg')


# In[24]:


print(img.dtype, img.shape)
#print(img)


# In[20]:


# image tinting 
img_tinted = img * [1, 0.95, 0.9]


# In[28]:


print(imshow(img))


# In[ ]:




