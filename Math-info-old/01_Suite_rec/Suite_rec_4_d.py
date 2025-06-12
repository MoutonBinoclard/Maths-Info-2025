import math

u=[1]

def suite(utot, terme):
    somme = 0
    for i in range(terme):
        somme += math.comb(terme, i)*utot[i]
    return somme

for i in range(50):
    u.append(
        suite(u, i)
    )

terme=range(len(u))
import matplotlib.pyplot as plt
plt.plot(terme, u)
plt.show()

# Pas de convergence
# Si on mettait u0 = 0, on aurait une suite convergente