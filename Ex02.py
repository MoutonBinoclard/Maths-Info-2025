# Part 1

# Matrice dimension 5x5 initialisée à -1
M = [[-1]*5 for _ in range(5)]

# Remplissage de la matrice avec des valeurs spécifiques
M[0][1] = M[1][0] = 9
M[1][2] = M[2][1] = 1
M[1][3] = M[3][1] = 8
M[0][2] = M[2][0] = 3
M[0][4] = M[4][0] = 7
M[2][4] = M[4][2] = 2
M[2][3] = M[3][2] = 4

# Mettre 1 dans la diagonale
for i in range(5):
    M[i][i] = 1

# Affichage de la matrice (ligne par ligne pour la lisibilité)
print("Matrice M:")
for row in M:
    print(row)

# --------------------

# Part 2 et 3

def voisins(i): # Retourne la liste des voisins du sommet i dans la matrice M
    voisins = []
    for j in range(5):
        
        # On vérifie si M[i][j] est un voisin (donc pas lui même, et pas -1)
        # On aurait aussi pu faire if M[i][j] > 0:
        if M[i][j] != -1 and i != j:
            voisins.append(j)
    return voisins

# Test pour le sommet 4
print("Voisins du sommet 4:", voisins(4))

# --------------------

# Part 4

def degre(i): # Retourne le degré du sommet i dans la matrice M
    return len(voisins(i)) # Il suffit de compter le nombre de voisins

# Degré du sommet 4
print("Degré du sommet 4:", degre(4))

# --------------------

# Part 5

def longueur(L): # Liste correspond à la liste des sommets par lesquels on passe
    total = 0
    for index in range(len(L) - 1):
        sommet_actuel, sommet_suivant = L[index], L[index + 1]
        
        if M[sommet_actuel][sommet_suivant] == -1: # Si le trajet n'est pas possible, -1
            return -1
        
        total += M[sommet_actuel][sommet_suivant] # Sinon on ajoute la distance entre les deux sommets
    
    return total

# Exemple :
print(longueur([0, 2, 4]))  # Affiche 5 (3 + 2)
