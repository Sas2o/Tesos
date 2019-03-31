#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import matplotlib.pyplot as plt


# In[14]:


def invert(A):
    I=np.identity(A.shape[1])
    for i in range(A.shape[1]):
        n=A[i,i]
        A[i]=A[i]/n
        I[i]=I[i]/n
        for j in range(A.shape[0]):
            if j!=i:
                p1=A[j,i]
                A[j]=A[j]-A[i]*p1
                I[j]=I[j]-I[i]*p1
    return I


# In[15]:



x=np.random.rand(100,100)
y=np.random.rand(100,1)


# In[16]:


H=x.dot(invert(x.T@x))@x.T


# In[17]:


n=len(y)
SSR=y.T.dot(H-np.ones((n,n))/n).dot(y)


# In[18]:


SST=y.T.dot(np.identity(n)-np.ones((n,n))/n).dot(y)


# In[19]:


R2=SSR/SST


# In[20]:


s2=SST/-1


# In[21]:


s2[0][0]


# In[25]:


def Exp_N(N,p=10,n=50):
    r2=[]
    for i in range(N):
        x=np.random.rand(n,p)
        y=np.random.rand(n,1)
        H=x.dot(invert(x.T@x))@x.T
        SSR=y.T.dot(H-np.ones((n,n))/n).dot(y)
        SST=y.T.dot(np.identity(n)-np.ones((n,n))/n).dot(y)
        R2=SSR/SST
        r2.append(R2[0][0])
    return r2


# In[26]:


R2=Exp_N(200)


# In[27]:


plt.title('MOS')
plt.hist(R2, bins = 60)
plt.grid(True)
plt.show()
plt.clf()


# In[ ]:





# In[ ]:





# In[ ]:




