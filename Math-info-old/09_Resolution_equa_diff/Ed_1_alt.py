# Methode d'euler pour résolution d'equa diff

# Resolution du problème suivant sur [-10, 10]:
# y' = y * cos(x) - 1
# y(0) = 0



import math as mt

def f(x, y):
    """
    Renvoie y'
    """
    return y * mt.cos(x) - 1


def euler(xini, xfin, yini, pas):
    nombre_points = int((xfin - xini) / pas) + 1

    # création de la liste des x
    x = [xini + i * pas for i in range(nombre_points)]

    # Initialisation de la liste des y
    y = [0] * nombre_points

    # Condition initale
    y[0] = yini

    # On calcul les y pour chaque x en utilisant la méthode d'Euler donc utiliser x[i-1] et y[i-1]
    for i in range(nombre_points - 1):
        y[i + 1] = y[i] + pas * f(x[i], y[i]) # Le y suivant est le précédent plus la dérivée multipliée par le pas

    return x, y


x_ini = 0
x_fin = 10
y_ini = 0
pas = 0.001

# Résolution pour x ∈ [0, 10]
x_pos, y_pos = euler(x_ini, x_fin, y_ini, pas)

# Résolution pour x ∈ [-10, 0] (en remontant le temps)
x_neg, y_neg = euler(x_ini, -x_fin, y_ini, -pas)

# Combinaison des résultats
x = x_neg[::-1] + x_pos[1:]  # Inverser la partie négative et combiner
y = y_neg[::-1] + y_pos[1:]  # Inverser la partie négative et combiner


# Affichage
import matplotlib.pyplot as plt
plt.plot(x, y, label="Méthode d'Euler")
plt.title("Résolution de y' = y * cos(x) - 1")
plt.show()