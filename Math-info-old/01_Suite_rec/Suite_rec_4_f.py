import math


u=[1]

def suite(u):

    n=len(u)-1

    somme = 0

    for k in range(0, n+1):
        print(k)
        somme += (math.comb(n, k)*u[k]*u[n-k])/2

    u.append(somme)
    return u

for i in range(100):
    u = suite(u)

import matplotlib.pyplot as plt
plt.plot(range(len(u)), u, 'x')
plt.show()

# Divergence venere