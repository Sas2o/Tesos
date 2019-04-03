#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from datetime import datetime
import matplotlib.pylab as plt
import pandas as pd
import scipy.signal as signal


# In[2]:


nomDatos=['datos/transacciones2008.txt','datos/transacciones2009.txt','datos/transacciones2010.txt']
datos=[]
for nombre in nomDatos:
    datos.append(pd.read_csv(nombre,sep= ";", header = None))
datos=pd.concat(datos)


# In[3]:


fecha=pd.to_datetime(datos[0],format='%d/%m/%Y %H:%M:%S')+(pd.to_datetime(datos[1],format='%d/%m/%Y %H:%M:%S')-pd.datetime(1899,12,30))


# In[4]:


precio1=datos[2]
precio2=datos[3]
datos=pd.DataFrame()
datos['Fecha']=fecha
datos['Precio']=precio1
datos['Precio']=datos['Precio'].str.replace(',','.').astype(float)
datos=datos.set_index('Fecha')


# In[5]:


print(datos)


# In[6]:


#datos.plot(figsize=(20,7))


# In[7]:


datos.to_csv('datos.csv', header=True, index=True)


# In[ ]:





# In[28]:


datos=pd.read_csv('datos.csv', sep=',', index_col=0)


# In[8]:


datos.plot(figsize=(20,7))


# In[8]:


datos=pd.read_csv('datos.csv', sep=',')
fecha=datos['Fecha'].values
precio=datos['Precio'].values


# In[9]:





# In[10]:


N  = 2    # Orden del filtro
Wn = 0.01 # Corte de frecuancia
B, A = signal.butter(N, Wn)


# In[11]:


precio_filtrada = signal.filtfilt(B,A, datos['Precio'])


# In[14]:





# In[5]:


fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(211)
plt.plot(fecha,precio, 'b-')
plt.plot(fecha,precio_filtrada, 'r-',linewidth=2)
plt.ylabel("Precio")
plt.legend(['Original','Filtrado'])
plt.title("Precio Transacciones")
ax1.axes.get_xaxis().set_visible(False)
ax1 = fig.add_subplot(212)
plt.plot(fecha,precio-precio_filtrada, 'b-')
plt.ylabel("Precio")
plt.xlabel("Fecha")
plt.legend(['Residuales'])
plt.show()


# In[ ]:


plt.figure(figsize=(20,7))
ruido=precio-precio_filtrada
corr=signal.correlate(ruido,ruido,mode="full")
plt.plot(corr[len(corr)//2:])
plt.show()


# In[ ]:


plt.figure(figsize=(20,7))
corr=np.correlate(ruido,ruido,mode="full")
plt.plot(corr[len(corr)//2:])
plt.show()


# In[ ]:


plt.figure(figsize=(20,7))
corr=np.correlate(ruido,ruido,mode="full")
plt.plot(np.abs(corr[len(corr)//2:]))
plt.show()

