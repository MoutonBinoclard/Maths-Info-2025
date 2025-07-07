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
    """
    Fonction qui affiche une matrice dans le terminal
    """
    for ligne in matrice:
        print(ligne)

def creation_matrice_vide(matrice):
    """
    Crée une matrice rempli de zero de la même taille que la matrice donnée
    """
    matrice_vide = []
    for i in range(len(matrice)):
        ligne = []
        for j in range(len(matrice[i])):
            ligne.append(0)
        matrice_vide.append(ligne)
    return matrice_vide


def creer_points_accessibles(matrice):
    """
    Crée une matrice avec les point accessible sur la première ligne
    """
    # Création d'une matrice vide, de la même taille que la matrice
    matrice_pt_accessibles = creation_matrice_vide(matrice)
    # Copie de la ligne 0 dans la matrice
    matrice_pt_accessibles[0] = matrice[0]
    return matrice_pt_accessibles


def augmenter_matrice(matrice, matrice_acces):
    import copy
    matrice_acces_clone = copy.deepcopy(matrice_acces)
    # Le deepcopy c'est pour eviter des bugs

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