import numpy as np

import matplotlib.pyplot as plt

# Définir la fonction f(x, y)
def f(x, y):
    return 13*x**2 + 7*y**2 - 8*x*y + 14*x - 2*y

# Créer une grille de points
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Tracer la courbe de niveau f(x, y) = 0
plt.contour(X, Y, Z, levels=[0], colors='b')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axis('equal')
plt.show()