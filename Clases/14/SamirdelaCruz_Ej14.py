import numpy as np
import matplotlib.pyplot as plt


# In[94]:


def coe_fit_poly(x1,y1,N=2):
    x=np.array(x1)
    y=np.array(y1)
    Num_x=len(x1)
    
    if Num_x==len(y1): 
        #generar S
        S=np.zeros((N,Num_x))
        for i in range(Num_x):
            for j in range(N):
                S[j][i]=x[i]**(j)
    S1=np.linalg.pinv(S)
    return y.dot(S1)

def f(cs,x):
    y=[]
    for j in range(len(x)):
        suma =0
        for i in range(len(cs)):
            suma+=cs[i]*(x[j]**(i))
        y.append(suma)
    return y
        
x1=[0.0,0.2,0.4,0.6,0.8,1.0]
y1=[0.892,1.44,1.31,1.66,1.10,1.19]
cs=coe_fit_poly(x1,y1) 
print(cs)
x=np.linspace(0,1,100)
y=f(cs,x)

plt.scatter(x1,y1,c="black")
plt.plot(x,y,c="r")
plt.title("Ajuste $N=2$")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.savefig("Ajuste_polinominal_de_segundo_grado.png")