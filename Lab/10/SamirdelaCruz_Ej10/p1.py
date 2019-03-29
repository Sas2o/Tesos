#!/usr/bin/env python
# coding: utf-8

# # Paradoja de Fredmann
# Llenamos las matrices de forma aleatoria con $\mu=0$ y $\sigma=1$

# In[40]:


import numpy as np
import random
import sys
from scipy.stats import f
from scipy.stats import norm


# In[60]:


#np.random.seed(500)
n=500 # mediciones efectuadas
p=50 # variables medidas
mu=0.0
sigma=1.0
X=np.random.normal(mu,sigma,size=(n,p))
Y=np.random.normal(mu,sigma,size=(n,1))
XT=X.T
YT=Y.T
Inv=np.linalg.inv(np.matmul(XT,X))
beta1=np.matmul(Inv,XT)
beta=np.matmul(beta1,Y)
Hhat=np.matmul(X,beta1)
Yideal=np.matmul(X,beta)


# In[61]:


SST1=np.matmul(np.identity(n)-(1.0/n)*np.ones((n,n)),Y)
SST=np.matmul(YT,SST1)
SSR1=np.matmul(Hhat-(1.0/n)*np.ones((n,n)),Y)
SSR=np.matmul(YT,SSR1)
SSE1=np.matmul(np.identity(n)-Hhat,Y)
SSE=np.matmul(YT,SSE1)


# Se calcula el $R^2$

# In[62]:


Rsq=SSR[0,0]/SST[0,0] #R^2


# Se calcula el valor de $\sigma^2$

# In[63]:


sigma2=SSE[0,0]/(n-1.)
sigmamatrix=sigma2*Inv
sigma_i=np.zeros(p)
for i in range(p):
    sigma_i[i]=sigmamatrix[i,i]
sigma_i=np.sqrt(sigma_i)


# In[64]:


MSE=SSE[0,0]/(n-p-1)
# Calculamos el MSR
MSR=SSR[0,0]/p
# Calculamos el MST
MST=SST[0,0]/(n-1)


# Calculamos F

# In[65]:


F=(Rsq*(n-p-1))/((1-Rsq)*p) #F

# In[66]:


Rango=0.9 # se define un rango, es decir cuanto porcentaje de la curva se quiere
Ftest=f.ppf(Rango,p,n-(p+1))
P_i=np.zeros(p)
if F > Ftest:
    tzeros=beta[:,0]/sigma_i
    P_value=2*(1-norm.cdf(tzeros)) # se integran las colas
    for i in range(p):
        if P_value[i]<0.5:
            P_i[i]=1
        else:
            P_i[i]=0
else:
    #print("paila")
    quit()


# In[75]:


p_prime=np.sum(P_i)
X_new=np.zeros((n,int(p_prime)))
Y_new=np.zeros((n,int(p_prime)))
aux=0
for i in range(p):
    if P_i[i]==1:
        X_new[:,aux]=X[:,i]
        Y_new[:,aux]=X[:,i]
        aux+=1
X=X_new
Y=Y_new
XT=X.T
YT=Y.T
Inv=np.linalg.inv(np.matmul(XT,X))
beta1=np.matmul(Inv,XT)


beta=np.matmul(beta1,Y)
Hhat=np.matmul(X,beta1)
Yideal=np.matmul(X,beta)


# In[61]:


SST1=np.matmul(np.identity(n)-(1.0/n)*np.ones((n,n)),Y)
SST=np.matmul(YT,SST1)
SSR1=np.matmul(Hhat-(1.0/n)*np.ones((n,n)),Y)
SSR=np.matmul(YT,SSR1)
SSE1=np.matmul(np.identity(n)-Hhat,Y)
SSE=np.matmul(YT,SSE1)


# Se calcula el $R^2$

# In[62]:


Rsq_new=SSR[0,0]/SST[0,0] #R_new^2


# Se calcula el valor de $\sigma^2$

# In[63]:


sigma2=SSE[0,0]/(n-1.)
sigmamatrix=sigma2*Inv
sigma_i=np.zeros(p)
for i in range(p):
    sigma_i[i]=sigmamatrix[i,i]
sigma_i=np.sqrt(sigma_i)


# In[64]:


MSE=SSE[0,0]/(n-p-1)
# Calculamos el MSR
MSR=SSR[0,0]/p
# Calculamos el MST
MST=SST[0,0]/(n-1)


# Calculamos F

# In[65]:


F_new=(Rsq*(n-p-1))/((1-Rsq)*p) #F_new

# In[66]:


Rango=0.9 # se define un rango, es decir cuanto porcentaje de la curva se quiere
Ftest=f.ppf(Rango,p,n-(p+1))
P_i=np.zeros(p)
if F > Ftest:
    tzeros=beta[:,0]/sigma_i
    P_value=2*(1-norm.cdf(tzeros)) # se integran las colas
    for i in range(p):
        if P_value[i]<0.5:
            P_i[i]=1
        else:
            P_i[i]=0
else:
    print("paila")
    #quit()


# In[75]:


p_prime=np.sum(P_i)
X_new=np.zeros((n,int(p_prime)))
aux=0
for i in range(p):
    if P_i[i]==1:
        X_new[:,aux]=X[:,i]
        aux+=1
X_newT=X_new.T
Inv_new=np.linalg.inv(np.matmul(X_newT,X_new))
beta1_new=np.matmul(Inv_new,X_newT)
