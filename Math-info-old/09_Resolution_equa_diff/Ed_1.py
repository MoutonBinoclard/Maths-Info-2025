import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return y * np.cos(x) - 1

x0 = -10
xf = 10
h = 0.01  # pas
n = int((xf - x0) / h)  # nombre d'étapes

x = np.linspace(x0, xf, n+1)
y = np.zeros(n+1)

y0 = 0

# Trouver l'indice où x = 0 (le point de départ)
start_index = np.argmin(np.abs(x - 0))
y[start_index] = y0

# Vers la droite
for i in range(start_index, n):
    y[i+1] = y[i] + h * f(x[i], y[i])

# Vers la gauche
for i in range(start_index, 0, -1):
    y[i-1] = y[i] - h * f(x[i], y[i])

# Affichage
plt.plot(x, y, label="Méthode d'Euler")
plt.title("Résolution de y' = y cos(x) - 1")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()
