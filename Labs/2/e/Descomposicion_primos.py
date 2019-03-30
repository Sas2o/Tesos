from time import time
import matplotlib.pyplot as plt
import numpy as np



##Transcr

def transcribir(DNA):
    dna=""
    for i in DNA:
        if i=='T':
            dna+='U'
        else:
            dna+=i
    return dna

#Pi
def f(n):
    suma=0
    for i in range(1,n+1):
        suma+=1/(i**2)
    pi=(6*suma)**(0.5)
    error=100*abs(pi-np.pi)/np.pi
    return pi

x=[10**2,10**3,10**5,10**7]
y=[]
for i in x:
    y.append(f(i))
    
plt.plot(x,y)
plt.savefig("piError.png")

##Des
ls=[[2,0]]

def multiplos(n):
    if n!=1:
        k=ls[-1][0]
        s=True
        if n%k==0:
            ls[-1][1]+=1
            s=False
            multiplos(int(n/k))
        M=n
        k+=1
        while k<M and s:
            if n%k==0:
                ls.append([k,1])
                s=False
                multiplos(int(n/k))
            k+=1
            M=n/k
        if s:
            ls.append([n,1])

def descomposicion_primos(n):
    multiplos(n)
    global ls
    lr=ls
    ls=[[2,0]]
    return lr

def primos(n):
    r=""
    lp = descomposicion_primos(n)
    i=0
    if lp[0][1]==0:
        i=1
    for i in lp[i:]:
        r+="("
        if i[1]==1:
            r+=str(i[0])
        else :
            r+=str(i[0])+"**"+str(i[1])
        r+=")"
    return r

def tiempo(n):
    i=time()
    lr=primos(n)
    f=time()
    return n,lr,f-i

print(tiempo(86240))
print(tiempo(7775460))
print(tiempo(777546031))
print(tiempo(512345021))
