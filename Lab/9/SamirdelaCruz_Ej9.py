#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[6]:


import urllib.request
url = "https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2028-201910/master/ejercicios/18/monthrg.dat"
nombreArchivo=url[url.rfind('/')+1:]
fG = urllib.request.urlopen(url)
fichero = open(nombreArchivo,"wb")
fichero.write(fG.read())
fichero.close()


# In[11]:


datos = np.loadtxt(nombreArchivo)
nombre = datos[:,0]
DATOS = datos[:,1:] #depende de la estructura de los datos
for i in range(DATOS.shape[1]):
    DATOS[i] = (DATOS[i] - np.mean(DATOS[i]))/np.std(DATOS[i])


Mcov = np.cov(DATOS.T)
AutoValores, Autovectores = np.linalg.eig(Mcov)

Vpc1 = Autovectores[:,0]
Vpc2 = Autovectores[:,1]


plt.figure(figsize=(12,12))


for i in range(DATOS.shape[0]):
    p = np.array(DATOS[i])
    x = np.dot(Vpc1, p)
    y = np.dot(Vpc1, p)
    plt.text(x,y, nombre[i], fontsize=10, color='blue')
    plt.scatter(x, y, s=0.001)

# Proyeccion de los autovectores
for j in range(DATOS.shape[1]):
    plt.arrow(0.0, 0.0, 5*Vpc1[j], 5*Vpc2[j], color='red', head_width=0.1)
    plt.text(5.5*Vpc1[j][j], 5.5*Vpc2[j], 1, color='red')

plt.xlabel('Primera Componente Principal')
plt.ylabel('Segunda Componente Principal')
plt.savefig('componentes_principales.png', bbox_inches='tight')


# In[ ]:




