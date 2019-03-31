import urllib.request
import numpy as np

aD = "https://raw.githubusercontent.com/ComputoCienciasUniandes/MetodosComputacionalesDatos/master/hands_on/PCA/data_A.txt"
aG = "data_A.txt"
fG = urllib.request.urlopen(aD).read()
fichero = open(aG,"wb")
fichero.write(fG)
fichero.close()

aD = "https://raw.githubusercontent.com/ComputoCienciasUniandes/MetodosComputacionalesDatos/master/hands_on/PCA/data_B.txt"
aG = "data_B.txt"
fG = urllib.request.urlopen(aD).read()
fichero = open(aG,"wb")
fichero.write(fG)
fichero.close()

def matrix_cov(A):
    x=A[:,0]
    y=A[:,1]
    x_promed=np.average(x)
    y_promed=np.average(y)
    C=np.zeros((2,2))
    S=[sum(x-x_promed)/len(x),sum(y-y_promed)/len(y)]
    
    for i in range(2):
        for j in range(2):
            C[i,j]=S[i]*S[j]
    return C
A=np.loadtxt("data_A.txt")
B=np.loadtxt("data_B.txt")
print(matrix_cov(A))
print(matrix_cov(B))