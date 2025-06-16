# le graph
M = [[0, 3, 7, -1, 4],
     [3, 0, 6, -1, -1],
     [7, 6, 0, 3, 6],
     [-1, -1, 3, 0, 2], 
     [4, -1, 6, 2, 0]]

# Fonction voisins qui renvoie la liste des voisins d'un sommet
def voisins(Matrice, sommet):
    voisins = []
    for i in range(len(Matrice)):
        if Matrice[sommet][i] != -1 and sommet != i:
            voisins.append(i)
    return voisins

print("Voisins du sommet 3 :", voisins(M, 3))

