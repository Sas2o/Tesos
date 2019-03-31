#1

import numpy as np
import matplotlib.pyplot as plt

def D1(f,x,h):
    return (f(x+1j*h)).imag/h
def f(x):
    return np.sin(x)**5
def DF(f,x,h):
    return (f(x+h)-f(x))/h
def CD(f,x,h):
    return (f(x+h/2)-f(x-h/2))/h
def ER(D,f,x,h):
    return (4*D(f,x,h/2)-D(f,x,h))/3
print(D1(f,np.pi/2,0.1))

#2
#2.a

def F(x):
    return np.exp(x)/(np.cos(x)**3+np.sin(x)**3)
hs=np.logspace(-6,-1,20)
error_DF=[]
error_CD=[]
error_D1=[]
H=[]
a=np.sqrt(2)*np.exp(np.pi/4)
for h in hs:
    H.append(h)
    error_DF.append(abs(DF(F,np.pi/2,h)-a)/a)
    error_CD.append(abs(CD(F,np.pi/2,h)-a)/a)
    error_D1.append(abs(D1(F,np.pi/2,h)-a)/a)
plt.figure()
plt.plot(H,error_DF,label="error_DF")
plt.plot(H,error_CD,label="error_CD")
plt.plot(H,error_D1,label="error_D1")
plt.xlabel("$h$")
plt.legend()
plt.savefig("Figura_1.png")

#2.b

error_DF=[]
error_CD=[]
error_D1=[]
H=[]
a=np.sqrt(2)*np.exp(np.pi/4)
for h in hs:
    H.append(h)
    error_DF.append(abs(ER(DF,F,np.pi/2,h)-a)/a)
    error_CD.append(abs(ER(CD,F,np.pi/2,h)-a)/a)
    error_D1.append(abs(ER(D1,F,np.pi/2,h)-a)/a)
plt.figure()
plt.plot(H,error_DF,label="error_DF")
plt.plot(H,error_CD,label="error_CD")
plt.plot(H,error_D1,label="error_D1")
plt.xlabel("$h$")
plt.legend()
plt.savefig("Figura_2.png")