#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt


#10.3
    #1
T=1
"""Sawtooth function"""
def f_sawtooth(t,T=T):
    while t<0:
        t+=T
    while t>T:
        t-=T
    if 0<=t<=T/2:
        return t/(T/2)
    else :
        return (t-T)/(T/2)
    
"""or"""
def f1_sawtooth(t,T=T):
    while t<-T/2:
        t+=T
    while t>T/2:
        t-=T
    return t/(T/2)


# In[3]:



a_0=0

def a(n):
    return 0

def b(n):
    return 2*(-1)**(n+1)/(n*np.pi)

def Fourier_serie(t,n,T=1):
    w=2*np.pi/T
    suma = a_0/2
    for i in range(1,n+1):
        suma+=a(i)*np.cos(i*w*t)+b(i)*np.sin(i*w*t)
    return suma


# In[ ]:





# In[4]:


x=np.linspace(-1,1,1000)
ns=[2,4,10,20]

plt.figure(figsize=(10,7))
plt.subplot(2,1,1)

T=1
y_o=[]
y=[]

for t in x:
    y_o.append(f_sawtooth(t,T))
    
plt.plot(x,y_o,c="black",label="Original")
    
for n in ns:
    y_t=[]
    for t in x:
        y_t.append(Fourier_serie(t,n,T))
    y.append(y_t)

for n in range(len(y)):
    plt.plot(x,y[n],label="$n=$ "+str(ns[n]))
plt.legend()
plt.title("$T=$ "+str(T))

plt.grid(True)
plt.grid(color = '0.5', linestyle = '--', linewidth = 1)

plt.subplot(2,1,2)

T=0.25
y=[]
y_o=[]
y=[]

for t in x:
    y_o.append(f_sawtooth(t,T))
    
plt.plot(x,y_o,c="black",label="Original")

for n in ns:
    y_t=[]
    for t in x:
        y_t.append(Fourier_serie(t,n,T))
    y.append(y_t)
    
for n in range(len(y)):
    plt.plot(x,y[n],label="$n=$ "+str(ns[n]))
plt.legend()
plt.title("$T=$ "+str(T))

plt.grid(True)
plt.grid(color = '0.5', linestyle = '--', linewidth = 1)
plt.savefig("10.3_1.png")
print("En los puntos de discontinuida la funcion toma valores por la izquierda de 1 y por la derecha de -1 por tanto el valor medio seria 0\n Este es precisamente el valor obtenido para las series como es facil observar en la figura")


# In[5]:


#10.3
    #2
"""Half-wave"""
def f_HalfWave(t,T):
    w=2*np.pi/T
    while t<0:
        t+=T
    while t>T:
        t-=T
    if 0<=t<=T/2:
        return np.sin(w*t)
    else :
        return 0


# In[6]:


a_0=2/np.pi
def a(n):
    if n%2==0:
        return -2/(np.pi*(n**2-1))
    else :
        return 0

def b(n):
    if n==1:
        return 1/2
    else :
        return 0

def Fourier_serie(t,n,T=1):
    w=2*np.pi/T
    suma = a_0/2
    for i in range(1,n+1):
        suma+=a(i)*np.cos(i*w*t)+b(i)*np.sin(i*w*t)
    return suma


# In[7]:


x=np.linspace(-1,1,1000)
ns=[2,4,10]

plt.figure(figsize=(10,7))
plt.subplot(2,1,1)

T=1
y_o=[]
y=[]

for t in x:
    y_o.append(f_HalfWave(t,T))
    
plt.plot(x,y_o,c="black",label="Original")
    
for n in ns:
    y_t=[]
    for t in x:
        y_t.append(Fourier_serie(t,n,T))
    y.append(y_t)

for n in range(len(y)):
    plt.plot(x,y[n],label="$n=$ "+str(ns[n]))
plt.legend()
plt.title("$T=$ "+str(T))

plt.subplot(2,1,2)

T=0.25
y=[]
y_o=[]
y=[]

for t in x:
    y_o.append(f_HalfWave(t,T))
    
plt.plot(x,y_o,c="black",label="Original")

for n in ns:
    y_t=[]
    for t in x:
        y_t.append(Fourier_serie(t,n,T))
    y.append(y_t)
    
for n in range(len(y)):
    plt.plot(x,y[n],label="$n=$ "+str(ns[n]))
plt.legend()
plt.title("$T=$ "+str(T))
plt.savefig("10.3_2.png")


# In[8]:


def f_1(x):
    return 3*np.cos(x)+2*np.cos(3*x)+np.cos(5*x)
def f_2(t):
    return np.sin(t)+2*np.sin(3*t)+3*np.sin(5*t)
def f_3(t):
    return 5*np.sin(t)+2*np.sin(3*t)+np.sin(5*t)
def f_4(t):
    return np.sin(t)
def f_5(t):
    return np.sin(t/4)+np.sin(t)

x_Max=2*np.pi

N=1000
Xx=np.linspace(0,x_Max,N)
plt.plot(Xx,f_1(Xx))
plt.savefig("señal.png")


# In[14]:


def transformada_Fourier(y,Np):
    X=[]
    ns=[]
    for k in range(Np):
        suma=0
        for n in range(len(y)):
            suma+=y[n]*np.exp(-2j*np.pi*k*n/len(y))
        ns.append(k+1)
        X.append(suma/len(y))
    X=np.array(X)
    X=np.sqrt(X.real**2+X.imag**2)
    return ns,X


# In[15]:


NS=[16,32,32]
x_max=[2*np.pi,2*np.pi,4*np.pi]

plt.figure(figsize=(15,20))
for i in range(6):
    Xx=np.linspace(0,x_max[int(i/2)],1000)
    plt.subplot(3,2,i+1)
    if i%2==0:
        plt.plot(f_1(Xx),label="Señal")
    else:
        freq,F=transformada_Fourier(f_1(Xx),NS[int(i/2)])
        plt.scatter(freq,F,label="Transformada de Fourier")
    plt.legend()
    plt.title("$N=$ "+str(NS[int(i/2)]))
    plt.grid(True)
    plt.grid(color = '0.5', linestyle = '--', linewidth = 1)
plt.savefig("Ejemplo_1.png")


# In[16]:


f=[f_1,f_2,f_3,f_4,f_5]


plt.figure(figsize=(15,20))
for i in range(10):
    Xx=np.linspace(0,2*np.pi,1000)
    plt.subplot(5,2,i+1)
    if i%2==0:
        plt.plot(Xx,f[int(i/2)](Xx),label="Señal")
    else:
        freq,F=transformada_Fourier(f[int(i/2)](Xx),16)
        plt.scatter(freq,F,label="Transformada de Fourier")
    plt.legend()
    plt.title("$N=$ "+str(16))
    plt.grid(True)
    plt.grid(color = '0.5', linestyle = '--', linewidth = 1)
plt.savefig("Dos_1.png")


# In[17]:


plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
N=500
signal=np.zeros(N+1,float)
dftz=np.zeros(N,complex)
def f(signal):
    step=6/N
    x=0
    xs,ys=[],[]
    for i in range(N+1):
        signal[i]=3*np.cos(x)+2*np.cos(3*x)+np.cos(5*x)
        xs.append(x)
        ys.append(signal[i])
        x+=step
    return xs,ys
x1,y1=f(signal)
plt.plot(x1,y1)

N=16
signal=np.zeros(N+1,float)
dftz=np.zeros(N,complex)
def f(signal):
    step=6/N
    x=0
    xs,ys=[],[]
    for i in range(N):
        signal[i]=3*np.cos(x)+2*np.cos(3*x)+np.cos(5*x)
        xs.append(x)
        ys.append(signal[i])
        x+=step
    return xs,ys
x,y=f(signal)
plt.scatter(x,y)

plt.subplot(1,2,2)
def fourier(dftz):
    xs,ys=[],[]
    x,y=f(signal)
    for n in range(N):
        zsum=complex(0,0)
        for k in range(N):
            zexpo=complex(0,2*np.pi*k*n/N)
            zsum+=y[k]*np.exp(-zexpo)
        dftz[n]=zsum/np.sqrt(2*np.pi)
        if dftz[n].real !=0:
            xs.append(n)
            ys.append(abs(dftz[n].real))
    return xs,ys
"""def fourier(dftz):
    ys=[]
    ns=[]
    for n in range(0,N):
        zsum=0
        for k in range(len(y1)):
            zexpo=complex(0,6*x1[k]*n/N)
            zsum+=y1[k]*np.exp(-zexpo)
        dftz[n]=abs(zsum)
        ns.append(n+1)
        ys.append(dftz[n].real)
    return ns,ys"""
x,y=fourier(dftz)
print(len(x))
plt.scatter(x,y)

plt.savefig("TR.png")


# In[ ]:





# In[ ]:




