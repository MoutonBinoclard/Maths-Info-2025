import numpy as np
import matplotlib.pyplot as plt


N=np.linspace(-4,4,701)
n=np.linspace(-4,4,701)
u=[]
v=[]
for x in N:
    for y in n:
        a=x+y*1j
        Z=(a**2+1j)/(a-1j)
        if abs(Z.imag)<=0.01:
            u.append(x)
            v.append(y)

r=[]
s=[]
for x in N:
    for y in n:
        a=x+y*1j
        Z=(a**2+1j)/(a-1j)
        if abs(Z.real)<=0.01:
            r.append(x)
            s.append(y)
plt.plot(u,v,'.')
plt.scatter(r,s,color='r')
plt.show()
