import numpy as np
import matplotlib.pyplot as plt
import sys

datos=np.loadtxt(sys.argv[1])
plt.figure(figsize=(15,10))
T=["$R^2$","F","$R_{new}^2$","$F_{new}$"]
for i in range(4):
	plt.subplot(2,2,i+1)
	h=datos[:,i]
	plt.title(T[i])
	plt.hist(h, bins=60, alpha=1, edgecolor = 'black',  linewidth=1)
plt.savefig("histogram.png")



