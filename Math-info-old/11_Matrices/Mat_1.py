import numpy as np
import numpy.linalg as la

A =np.array([[3, 0, 1],
             [2, 1, 1],
             [1, 1, 2]])

A = A * (1/4)
print(A)


# 1.a / Calculer A^50 et det(A)

A_50 = la.matrix_power(A, 50)
det_A = la.det(A)
print("A^50")
print(A_50)
print("det(A)")
print(det_A)


# 1.b / Valeurs propres de A
val_propres_A = la.eigvals(A)
print("Valeurs propres de A")
print(val_propres_A)
val_propres_arondies = [1, 0.25, 0.25]
# Controle ok (les multiplier = det(A))


# 1.c.I / matrice 2x3 consitué de 0
# 1.c.II / matrice 3x2 consitué de 0
# 1.c.III / matrice identité d'ordre 4
matrice_2x3 = np.zeros((2, 3))
matrice_3x2 = np.zeros((3, 2))
matrice_identite_4 = np.eye(4)


# 1.c.IV / taille d'une matrice, nombre de lignes et de colonnes
taille_matrice = A.shape
print("Taille de la matrice A")
print(taille_matrice)


# 1.c.V / calculer A x E, 3A, A + E
E = np.ones((3, 3))
A_x_E = np.dot(A, E)
A_3A = 3 * A
A_plus_E = A + E
print("A x E")
print(A_x_E)
print("3A")
print(A_3A)
print("A + E")
print(A_plus_E)


# 1.c.VI / verif matrice carrée, si oui dimension, si non 0
def test(M):
    if len(M[0]) == len(M): 
        return len(M)
    else:
        return 0


# 1.c.VII / calcul de la trace d'une matrice si elle est carrée
def trace(M):
    if test(M) != 0:
        return np.trace(M)
    else:
        return None
    
print(trace(A))