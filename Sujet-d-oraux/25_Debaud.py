matrice_1 = [
    [0, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0]
]



matrice_2 = [
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    [1, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 1, 1, 1, 1]
]

def afficher_matrice(matrice):
    for ligne in matrice:
        print(ligne)


def creer_points_accessibles(matrice):
    # création matrice vide
    matrice_pt_accessibles = []
    for i in range(len(matrice)):
        ligne = []
        for j in range(len(matrice[i])):
            ligne.append(0)
        matrice_pt_accessibles.append(ligne)

    # Copie de la ligne 0 dans la matrice
    matrice_pt_accessibles[0] = matrice[0]
    return matrice_pt_accessibles


def augmenter_matrice(matrice, matrice_acces):
    import copy
    matrice_acces_clone = copy.deepcopy(matrice_acces)
    #afficher_matrice(matrice_acces_clone)

    for ligne in range(len(matrice_acces)):
        for colonne in range(len(matrice_acces[ligne])):
            if matrice_acces[ligne][colonne] == 1:
                # en haut
                if ligne > 0 and matrice[ligne-1][colonne] == 1:
                    matrice_acces_clone[ligne-1][colonne] = 1
                # en bas
                if ligne < len(matrice_acces)-1 and matrice[ligne+1][colonne] == 1:
                    matrice_acces_clone[ligne+1][colonne] = 1
                # à gauche
                if colonne > 0 and matrice[ligne][colonne-1] == 1:
                    matrice_acces_clone[ligne][colonne-1] = 1
                # à droite
                if colonne < len(matrice_acces[ligne])-1 and matrice[ligne][colonne+1] == 1:
                    matrice_acces_clone[ligne][colonne+1] = 1
    return matrice_acces_clone



def verif_parcours_possible(matrice):
    matrice_acces = creer_points_accessibles(matrice)
    while matrice_acces != augmenter_matrice(matrice, matrice_acces):
        matrice_acces = augmenter_matrice(matrice, matrice_acces)
    afficher_matrice(matrice_acces)
    return any(matrice_acces[-1])

print(verif_parcours_possible(matrice_1))
print(verif_parcours_possible(matrice_2))

