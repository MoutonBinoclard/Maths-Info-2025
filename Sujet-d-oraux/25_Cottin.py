"""
On représente un polynôme sous la forme d'une liste de tuple (k,ak) ou k est le degré et ak le coefficient associé.

1) donner les deux polynômes de l'énoncé sous la forme de deux listes L1 et L2

2) écrire une fonction, prenant L et k comme arguments, réalisant la multiplication d'un polynôme par un scalaire k

3) écrire une fonction, prenant L et k comme arguments, donnant le résultat de P*X^k

4) écrire une fonction prenant L et M comme arguments, donnant le résultat de la somme de deux polynômes 

5) écrire une fonction prenant L et M comme arguments, donnant le résultat du produit de deux polynômes.

6) il fallait convertir la liste des degrés/coefficients sous la forme d'un string, en respectant un formalisme (non traitée)
"""

#1
# Quelques exemples de polynômes sous forme de liste de tuples
L0 = [(0, 1), (1, 2), (2, 3)]  # P0 = 1 + 2X + 3X^2
L1 = [(0, 4), (1, 5), (2, 6)]  # P1 = 4 + 5X + 6X^2
L2 = [(0, 7), (1, 8), (3, 9)]  # P2 = 7 + 8X + 9X^3

#2
def multiplication_scalaire(L, k): # Juste multiplie chaque coefficient par k
    Nouveau_L = []
    for degre, coeff in L:
        Nouveau_L.append((degre, coeff * k))
    return Nouveau_L

# Essai de la fonction multiplication_scalaire
print(L0)
print(multiplication_scalaire(L0, 2))  # P0 * 2 = 2 + 4X + 6X^2

#3
def multiplication_par_X_k(L, k): # En gros ça augmente le degré de chaque terme de k
    Nouveau_L = []
    for degre, coeff in L:
        Nouveau_L.append((degre + k, coeff))
    return Nouveau_L

# Essai de la fonction multiplication_par_X_k
print(L0)
print(multiplication_par_X_k(L0, 2))  # P0 * X^2 = 1 + 2X^3 + 3X^4

#4
def somme_polynomes(L, M):  # Additionne les coefficients des mêmes degrés
    result = {}
    for degre, coeff in L + M:
        if degre in result:
            result[degre] += coeff
        else:
            result[degre] = coeff
    return sorted(result.items())

# Essai de la fonction somme_polynomes
print(L0)
print(L1)
print(somme_polynomes(L0, L1))  # P0 + P1 = 5 + 7X + 9X^2

#5
def produit_polynomes(L, M):
    result = {}
    for degre1, coeff1 in L:
        for degre2, coeff2 in M:
            new_degre = degre1 + degre2
            if new_degre in result:
                result[new_degre] += coeff1 * coeff2
            else:
                result[new_degre] = coeff1 * coeff2
    return sorted(result.items())

# Essai de la fonction produit_polynomes
print(L0)
print(L1)
print(produit_polynomes(L0, L1))  # P0 * P1 = 4 + 13X + 28X^2 + 18X^3 + 18X^4

#6
# Je comprends pas très bien ce qu'il faut faire ici
