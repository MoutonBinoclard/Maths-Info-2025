# Création du fichier exemple

import os
import math

def creer_fichier_exemple():
    donnees = [
        (0.0, 1.00988282142),
        (0.1, 1.07221264497),
        (0.2, 1.1487212707),
        (0.3, 1.240818385),
        (0.4, 1.351600233),
        (0.5, 1.484131591),
        (0.6, 1.642013568),
        (0.7, 1.829568788),
        (0.8, 2.052053199),
        (0.9, 2.315841784),
        (1.0, 2.628657544),
        (1.1, 2.999796063),
        (1.2, 3.440427265),
        (1.3, 3.964035706),
        (1.4, 4.586894527)
    ]
    chemin = "ex_001.csv"
    with open(chemin, 'w') as f:
        for x, y in donnees:
            f.write(f"{x};{y}\n")
    print(f"Fichier '{chemin}' créé avec succès.")

#creer_fichier_exemple()

debut= 0.0
fin = 1.4
pas = 0.1

def g(x): # On met g et non f car la lecture de fichier ecrase f lors de son utilisation
    return math.sin(7*x)+1.1 # Fonction qui varie assez rapidement pour voir les trapèzes

def calcule_un_couple_de_valeurs(x, fonction):
    return (x, fonction(x))

def calcule_liste_de_couples_de_valeur(fonction, debut, fin, pas):
    liste = []
    x = debut
    while x <= fin:
        liste.append(calcule_un_couple_de_valeurs(x, fonction))
        x += pas
    return liste

def creer_fichier_exemple_2(fonction, debut, fin, pas):
    chemin = "ex_001.csv"
    with open(chemin, 'w') as f:
        for x, y in calcule_liste_de_couples_de_valeur(fonction, debut, fin, pas):
            f.write(f"{x};{y}\n")
    print(f"Fichier '{chemin}' créé avec succès.")

creer_fichier_exemple_2(g, debut, fin, pas)

# --------------------

# Part 1

LX = []
LY = []

chemin = "ex_001.csv"

with open(chemin, 'r') as f:
    for ligne in f:
        x_str, y_str = ligne.strip().split(';') # Sépare les valeurs par le point-virgule

        # On convertit les chaîne de caractère en float
        LX.append(float(x_str))
        LY.append(float(y_str))

print("LX:", LX)
print("LY:", LY)

# --------------------

# Part 2

import matplotlib.pyplot as plt



# Non demandé : Tracer les trapèzes sur le graph
LX_trapezes = []
LY_trapezes = []
LX_trapezes.append(LX[0])
LY_trapezes.append(0)
for i in range(1, len(LX)):
    LX_trapezes.append(LX[i - 1])
    LY_trapezes.append(LY[i - 1])
    LX_trapezes.append(LX[i])
    LY_trapezes.append(LY[i])
    LX_trapezes.append(LX[i])
    LY_trapezes.append(0)
plt.plot(LX_trapezes, LY_trapezes, 'r-', label='Représentation des trapèzes')  # 'r--' pour une ligne rouge en pointillés


# Non demandé : Tracé de la fonction en haute précision (bien comparer avec less trapèzes)
LX_prec = [x / 1000 for x in range(int(debut * 1000), int(fin * 1000) + 1)]
LY_prec = [g(x) for x in LX_prec]
plt.plot(LX_prec, LY_prec, 'g-', label='Fonction f(x) (Haute précsion)')  # 'g-' pour une ligne verte continue


# Tracer la courbe Y en fonction de X
plt.plot(LX, LY, '--o', label='LY en fonction de LX')  # '--o' pour une ligne en tirets avec des points marqués
# '-o' correspond à une ligne avec des points marqués
# y'a des variate comme '-x', '--', etc. pour changer le style de la ligne
plt.title('Y en fonction de X')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.axhline(0, color='black', linewidth=2)
plt.legend()
plt.show()


# --------------------

# Part 3

def trapeze(LY, LX):
    somme = 0.0
    
    for i in range(1, len(LX)):
        
        l = LX[i] - LX[i - 1] # largeur de l'intervalle
        h = (LY[i] + LY[i - 1]) / 2 # hauteur moyenne de l'intervalle
        
        somme += l*h # on ajout l'aire du trapèze à la somme totale

    return somme

# Calcul de l'intégrale
integrale = trapeze(LY, LX)
print("Valeur de l'intégrale:", integrale)

# --------------------

# Part 4

"""
from scipy.integrate import trapz

integrale_scipy = trapz(LY, LX)
print("Valeur de l'intégrale (scipy):", integrale_scipy)
"""
# Note : La fontction traps ne marchait pas, j'utilise numpy à la place

import numpy as np
integrale_numpy = np.trapezoid(LY, LX)
print("Valeur de l'intégrale (numpy):", integrale_numpy)

# On a la même valeur avec numpy et la fonction trapeze
