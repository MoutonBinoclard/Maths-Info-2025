import numpy as np


def liste_astroide(nombre_pt):

    t = np.linspace(0, 2 * np.pi, nombre_pt)
    x = np.cos(t) ** 3
    y = np.sin(t) ** 3

    return x, y

def liste_cardioide(nombre_pt, a):

    t = np.linspace(0, 2 * np.pi, nombre_pt)
    x = a * np.cos(t) * (1 + np.cos(t))
    y = a * np.sin(t) * (1 + np.cos(t))

    return x, y

import matplotlib.pyplot as plt


x, y = liste_astroide(1000)
plt.plot(x, y)
plt.title('Astroide')
plt.gca().set_aspect('equal', adjustable='box')  # Ratio 1:1 obligatoire
plt.show()


x, y = liste_cardioide(1000, 1)
plt.plot(x, y)
plt.title('Cardioide')
plt.gca().set_aspect('equal', adjustable='box')  # Ratio 1:1 obligatoire
plt.show()

