
import numpy as np

import matplotlib.pyplot as plt



# In[22]:


mean_01 = np.array([0.0, 0.0])
cov_01 = np.array([[1.1, 0.1], [0.1, 1.0]])
mean_02 = np.array([6.0, 6.0])
cov_02 = np.array([[1.1, 0.1], [0.1, 1.0]])
dist_01 = np.random.multivariate_normal(mean_01, cov_01, 500)
dist_02 = np.random.multivariate_normal(mean_02, cov_02, 500)


# In[30]:


print(dist_01.shape)
print(dist_02.shape)


# In[35]:


for ix in list(range(dist_01.shape[0])):
    plt.scatter(dist_01[ix, 0], dist_01[ix, 1], c = 'r')
    plt.scatter(dist_02[ix, 0], dist_02[ix, 1], c = 'g')
plt.show()


# In[ ]:





# In[ ]:



