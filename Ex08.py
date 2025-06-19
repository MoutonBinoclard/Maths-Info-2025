# On pose
M = 20
m = 10

import numpy as np
import matplotlib.pyplot as plt

# --------------------

# Part 1

def f(c):
    u = 0
    
    for k in range(1, 1 + m): # k est plus grand que 0 et plus petit ou egal à m. On faisant comme ça, la premiere condition sur k est verifié
        u = u**2 + c
        if abs(u) >= M:
            return k # dès qu'un k marche et qu'il rempli la deuxieme condition, on le renvoi
    
    return m+1 # Si aucun k ne marche, on renvoi m+1

# --------------------

# Part 2

nombre_pt=200
min = -2
max = 2

LX = np.linspace(min, max, nombre_pt)
LY = [f(x) for x in LX]

plt.plot(LX, LY, 'r.')
plt.show()

# --------------------

# Part 3

val_min_x = -2
val_max_x = 0.5
val_min_y = -1.1
val_max_y = 1.1
nombre_points = 500

# Creation des listes de valeur pour x et y (reel et imaginaire)
x_vals = np.linspace(val_min_x, val_max_x, nombre_points)
y_vals = np.linspace(val_min_y, val_max_y, nombre_points)

# Création du tableau pour stocker les résultats
tableau = np.zeros((len(x_vals), len(y_vals)), dtype=int)


# On va calculer f(c) pour chaque combinaison de x et y
for i, x in enumerate(x_vals): # Partie reel
    for j, y in enumerate(y_vals): # Partie imaginaire
        c = x + 1j * y
        tableau[i, j] = f(c)

# --------------------

# Part 4

plt.imshow(tableau.T, extent=[val_min_x, val_max_x, val_min_x, val_min_y], origin='lower', cmap='magma', aspect='auto')
# Affichage de l'image avec les valeurs de f(c)
# extent définit les limites des axes x et y
# origin='lower' place l'origine en bas à gauche
# cmap='plama' ça correspond à une palette de couleurs (on peut aussi utiliser 'hot')

plt.xlabel('Partie réelle de c')
plt.ylabel('Partie imaginaire de c')
plt.title('Fractale de Mandelbrot')
plt.colorbar(label='Valeur de f(c)')
plt.show()


# --------------------

# Voici le code fait par Alec, il est très propre


M = 20
m = 10

def f(c):
    M = 20
    m = 10
    u = [0]
    k = 0
    while k <= m:
        if np.sqrt((u[-1].real**2) + (u[-1].real**2)) > M :
            return k
        uk1 = u[-1]**2 + c
        u.append(uk1)
        k += 1
    return m+1

c = np.linspace(-2,2,100)
F = [f(x) for x in c]

plt.plot(c,F,'x')
plt.show()

x = np.linspace(-2,0.5,101)
y = np.linspace(-1.1,1.1,101)

F = np.zeros((101,101))
print(F)
for i in range(len(x)):
    for j in range(len(y)):
        F[i,j] = f(x[i] + y[j]*1j)

plt.imshow(F)
plt.colorbar()
plt.show()