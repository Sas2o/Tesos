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
