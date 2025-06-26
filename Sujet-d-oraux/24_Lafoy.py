# Partie 1

def nbD(mot):
    # Compte le nombre de D dans le mot
    compteur = 0
    for lettre in mot :
        if lettre == 'D':
            compteur += 1
    return compteur

def nbH(mot):
    # Compte le nombre de H dans le mot
    compteur = 0
    for lettre in mot :
        if lettre == 'H':
            compteur += 1
    return compteur

mot_choisi = "DHHDDDHDH"
print(nbD(mot_choisi))
print(nbH(mot_choisi))


# Partie 2

def liste_co(mot):
    # Retourne la liste des coordonées
    liste_co_x = [0]
    liste_co_y = [0]
    for lettre in mot :
        if lettre == 'D':
            liste_co_x.append(liste_co_x[-1]+1)
            liste_co_y.append(liste_co_y[-1])
        if lettre == 'H':
            liste_co_x.append(liste_co_x[-1])
            liste_co_y.append(liste_co_y[-1]+1)
    return (liste_co_x, liste_co_y)

co_x, co_y = liste_co(mot_choisi)

import matplotlib.pyplot as plt

plt.plot(co_x, co_y, 'o-')
plt.plot([co_x[0], co_x[-1]], [co_y[0], co_y[-1]])  # Point de départ et d'arrivée
plt.axis("equal")
plt.show()

# Partie 3

# On demande les points qui sont au dessus ? Si oui alors

def pt_au_dessus_du_segment(cox, coy):
    # Definir l'équation entre le debut et la fin du segment
    a = (coy[-1] - coy[0]) / (cox[-1] - cox[0]) # pente
    b = coy[0] - a * cox[0] # ordonnée à l'origine

    liste_index_au_dessus = []

    # On regarde si les points sont au dessus de la droite
    for index in range(len(cox)):
        if coy[index] > a * cox[index] + b :
            liste_index_au_dessus.append(index)
    return liste_index_au_dessus

print(pt_au_dessus_du_segment(co_x, co_y))