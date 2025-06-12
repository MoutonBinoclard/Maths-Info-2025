def verif_nombre_premier(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# -------------------------

def liste_diviseurs(n):
    return [i for i in range(1, n) if n % i == 0]

# -------------------------

def ajouter_premier_suivant(liste_premier):
    val=liste_premier[-1] + 1
    while not verif_nombre_premier(val):
        val += 1
    liste_premier.append(val)
    return liste_premier

#print(verif_nombre_premier(17))
# True

#print(verif_nombre_premier(21))
# False

#print(verif_nombre_premier(1))
# False

#print(liste_diviseurs(21))
# [1, 3, 7]

# -------------------------
# APPLICATIONS

# donner les n premiers nombres premiers
N = 40
liste_premier = []
for i in range(1, N):
    if verif_nombre_premier(i):
        liste_premier.append(i)
print(liste_premier)


# Trouver le 40ème nombre premier
N = 40
liste_premier = [2]
while len(liste_premier) < N:
    liste_premier=ajouter_premier_suivant(liste_premier)

print(liste_premier[-1])


print(sum(liste_premier))

    
# Trouver les entiers parfaits inférieurs ou égaux à 500
parfaits = []
for n in range(2, 501):
    if sum(liste_diviseurs(n)) == n:
        parfaits.append(n)
print("Entiers parfaits <= 500 :", parfaits)
