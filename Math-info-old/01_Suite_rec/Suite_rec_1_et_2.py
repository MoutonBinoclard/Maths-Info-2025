import numpy as np
import math as mt

# 1


N=20
deb=10
fin=30

# 1.a
def f (x):
    return np.sin(x)-x

# 1.b
X1=[]
Y1=[]
for i in range(N+1):
    X1.append(deb+(i*N/(fin-deb)))
for X in X1:
    Y1.append(f(X))

# 1.c
X2 = np.array([deb + i * (fin - deb) / (N) for i in range(N+1)])
Y2 = np.array([f(X) for X in X2])

# 1.d
X3 = np.linspace(deb, fin, N+1)
Y3 = f(X3)





# 2

# 2.a



def f1(x):
    if 0 <= x < 1:
        return x
    elif 1 <= x <= 2:
        return 1

def f2(x):
    return mt.sin(x) + 0.1


def intervale(pas, deb1, fin1):
    XX = []
    i = deb1
    while i <= fin1:
        XX.append(i)
        i += pas
    return XX

X4=intervale(0.05, 0, 2)
print(X4)

Yf1=[]
Yf2=[]

for i in X4:
    Yf1.append(f1(i))
    Yf2.append(f2(i))


import matplotlib.pyplot as plt
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Tracé de fonction")
plt.xlim(0, 2)
plt.ylim(0, 1.5)
plt.plot(X4, Yf1, 'b+-')
plt.plot(X4, Yf2, 'ro-')
plt.show()


# 2.b

def F1(x):
    return np.where((0 <= x) & (x < 1), x, 1)

def F2(x):
    return np.sin(x) + 0.1


X5 = np.linspace(0, 2, int((2 - 0) / 0.05) + 1)

YF1 = F1(X5)
YF2 = F2(X5)

plt.plot(X5, YF1, 'k--', linewidth=3, label='F1')
plt.plot(X5, YF2, 'b-', label='F2')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Tracé de fonctions")
plt.xlim(0, 2)
plt.ylim(0, 1.5)
plt.grid(True)
plt.legend()
plt.show()



