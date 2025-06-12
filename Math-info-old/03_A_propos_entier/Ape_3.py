n = 1234

q = n // 10 # quotient
r = n % 10 # reste

import math

# ----------------------------------

def calcul_base10(n):
    reste_division=[]
    while n > 0:
         reste_division.append(n % 10)
         n = n // 10

    return reste_division[::-1] # reverse the list to get the correct order

# ----------------------------------

def somchiffre(n):
     liste_chiffres = calcul_base10(n)
     return sum(liste_chiffres)

# ----------------------------------

def somcube(n):
    liste_chiffres = calcul_base10(n)
    return sum([i**3 for i in liste_chiffres])

# ----------------------------------

def listechiffre(taille_parcours):
    liste_nombre_egal_somme_cube = []
    for i in range(1, taille_parcours + 1):
        if i == somcube(i):
            liste_nombre_egal_somme_cube.append(i)
    return liste_nombre_egal_somme_cube

# ----------------------------------

def fact(n):
    # Donne le factoriel de n
    if n == 0 or n == 1:
        return 1
    else:
        val=1
        while n > 1:
            val *= n
            n -= 1
        return val

# ----------------------------------

def fact_rec(n):
    # Donne le factoriel de n de façon récursive
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact_rec(n - 1)

# ----------------------------------

def sommefacto(n):
    # Donne la somme des factoriels des chiffres de n
    liste_chiffres = calcul_base10(n)
    somme=0
    for i in liste_chiffres:
        somme += math.factorial(i)
    return somme   

# ----------------------------------

def listesommefacto(taille_parcours):
    #donnant tous les nombres entiers strictement inférieurs à 1000 qui sont égaux à la somme des factorielles de leurs chiffres
    liste_nombre_egal_somme_facto = []
    for i in range(1, taille_parcours + 1):
        if i == sommefacto(i):
            liste_nombre_egal_somme_facto.append(i)
    return liste_nombre_egal_somme_facto

# ----------------------------------

#print(calcul_base10(n)) # test de la function calcul_base10 (on a bien [1,2,3,4])
#print(somchiffre(n)) # test de la function somme_chiffres (on a bien 10)

#print(somchiffre(math.factorial(100)))
# Somme des chiffres de 100! = 648

#print(somchiffre(2**1000))
# Somme des chiffres de 2^1000 = 1366

#print(listechiffre(10000))
# test de la function listechiffre (on a bien [1, 153, 370, 371, 407])

#print(fact(3))
#print(fact_rec(3))
# test de la function fact (on a bien 6)

#print(sommefacto(145))
# test de la function sommefacto (on a bien 145)

print(listesommefacto(1000))
# Il y'a seulement 1, 2 et 145
