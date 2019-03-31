#!/usr/bin/env python
# coding: utf-8

# In[181]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[182]:


import urllib.request
aD = "https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2028-201910/master/ejercicios/16/Cars93.csv"
aG = "Cars93.csv"
fG = urllib.request.urlopen(aD)
fichero = open(aG,"wb")
fichero.write(fG.read())
fichero.close()


# In[183]:


data = pd.read_csv('Cars93.csv')
#data[:10]


# In[184]:


#print(data.iloc(0)['Model'])


# In[185]:


data_selecta = data[['Price', 'MPG.city', 'EngineSize', 'Horsepower', 'RPM', 
                     'Fuel.tank.capacity', 'Length', 'Width', 'Turn.circle', 'Weight']]
data_selecta=(data_selecta-data_selecta.mean(axis=0) )/data_selecta.std(axis=0)


# In[186]:


_ = pd.plotting.scatter_matrix(data_selecta, figsize=(10,10))


# In[187]:


Mcov_data_selecta=np.cov(data_selecta.T)


# In[188]:


eig=np.linalg.eig(Mcov_data_selecta)
autoVa=eig[0]
autoVe1=eig[1][0]
autoVe2=eig[1][1]


# In[189]:


Caract=np.array(data_selecta)
Model=np.array(data['Model'])
Pos=[]
for i in range(len(Model)):
    pos=[0,0]
    for k in range(len(autoVe1)):
        pos[0]+=Caract[i][k]*autoVe1[k]
        pos[1]+=Caract[i][k]*autoVe2[k]
    Pos.append(pos)


# In[190]:


plt.figure(figsize=(12,12))

for i in range(len(Model)):
    plt.text(Pos[i][0], Pos[i][1], Model[i], ha='center', va='center', fontsize=10, color='blue')
plt.xlim(-6,6)
plt.ylim(-2.5,2.5)


# In[ ]:





# In[118]:


"""plt.annotate(Model[i],
             xy=(Pos[i][0], Pos[i][1]), xycoords='data',
             xytext=(1, 0.5), ha='center', va='center', fontsize=20, color='orange',
             arrowprops=dict(arrowstyle="<-", connectionstyle="arc3", color='orange'))"""


# In[119]:





# In[ ]:




