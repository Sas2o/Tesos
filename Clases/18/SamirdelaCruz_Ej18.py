#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# In[3]:


import urllib.request
url = "https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2028-201910/master/ejercicios/18/monthrg.dat"
nombre=url[url.rfind('/')+1:]
fG = urllib.request.urlopen(url)
fichero = open(nombre,"wb")
fichero.write(fG.read())
fichero.close()


# In[4]:


datos=np.loadtxt(nombre)


# In[5]:


t0=datos[:,0]+datos[:,1]/12
promedio0=datos[:,4]
t=t0[t0>1800]
promedio=promedio0[t0>1800]


# In[6]:


plt.figure(figsize=(20,7))
plt.scatter(t,promedio,label="original",s=t*0 +6)
plt.legend()
plt.xlabel("Tiempo (yr)")
plt.ylabel("Numero de manchas")
plt.grid(True)
plt.grid(color = '0.5', linestyle = '--', linewidth = 1)
plt.savefig("1.png")


# In[104]:


def transformada_Fourier(y):
    dw=1200/len(y)
    X=[]
    w=[]
    for k in range(len(y)):
        suma=0
        for n in range(len(y)):
            suma+=y[n]*np.exp(-2j*np.pi*(dw*k-600)*n/len(y))
        w.append((dw*k-600)/100)
        X.append(suma/len(y))
    w=np.array(w)
    X=np.array(X)
    X=np.sqrt(X.real**2+X.imag**2)
    return w,X


# In[105]:


x,y=transformada_Fourier(promedio)


# In[ ]:





# In[106]:



plt.figure(figsize=(20,7))
plt.scatter(x,y,label="original",s=t*0 +6)
plt.legend()
plt.xlabel("frecuencia (1/yr)")
plt.ylabel("Norma FFT")
plt.grid(True)
plt.grid(color = '0.5', linestyle = '--', linewidth = 1)
plt.savefig("2.png")


# In[107]:


y[abs(x)>0.2]=0


# In[108]:


plt.figure(figsize=(20,7))
plt.scatter(x,y,label="original",s=t*0 +6)
plt.legend()
plt.xlabel("frecuencia (1/yr)")
plt.ylabel("Norma FFT")
plt.grid(True)
plt.grid(color = '0.5', linestyle = '--', linewidth = 1)
plt.savefig("3.png")


# In[109]:


x1,y1=x.copy(),y.copy()


# In[ ]:


def transformada_inv_Fourier(z):
    dt=2/len(z)
    Y=[]
    t=[]
    for k in range(len(z)):
        suma=0
        
        for n in range(len(z)):
            suma+=y[n]*np.exp((dt*k+18)*n/len(y))
            print(np.exp((dt*k+18)*n/len(y)))
        t.append((dt*k+18))
        Y.append(suma/len(z))
    t=np.array(t)
    Y=np.array(Y)
    return t,Y


# In[ ]:



x,y=transformada_inv_Fourier(y1)


# In[93]:





# In[91]:


plt.figure(figsize=(20,7))
plt.scatter(x,y,label="original",s=t*0 +6)
plt.legend()
plt.xlabel("frecuencia (1/yr)")
plt.ylabel("Norma FFT")
plt.grid(True)
plt.grid(color = '0.5', linestyle = '--', linewidth = 1)
plt.savefig("4.png")


# In[86]:





# In[ ]:




