import random

# --------------------

# Part 1

def comptage(L, N): # N = jusqu'a où il faut compter et L une liste
    
    P=[] # P[i] sera le nombre d'occurence de i dans L

    for nombre_recherher_en_cours in range(N + 1): # on cherche chaque nombre de 0 à N
        compteur = 0
        for valeur in L:
            if valeur == nombre_recherher_en_cours:
                compteur += 1
        P.append(compteur)
    return P


# --------------------

# Part 2

def tri(L, N): # renvoi la liste triée
    P = comptage(L, N)
    liste_triee = []
    
    for i in range(len(P)):
        liste_triee.extend([i] * P[i])  # Ajoute i, P[i] fois
        # On utilise extend ici pour bien ajouter des elements et non pas des listes imbriquées
    
    return liste_triee

# --------------------

# Part 3

N = 5

def creation_liste(Longeur, N): # N = valeur max
    return [random.randint(0, N) for _ in range(Longeur)] # Génère une liste de longueur 'Longeur' avec des valeurs entre 0 et N

L = creation_liste(20, N) 

print("Liste non triée:", L)
print("Liste triée:", tri(L, N))

# --------------------

# Part 4

# On a fait ici un tri par comptage
# Complexité en O(longueur_liste + valeur_max) = O(n + N)

# Complexité tri insertion = O(n^2)
# Complexité tri fusion = O(n log n)

# On a un tri qui est donc linéaire, ce qui est très efficace pour des listes de taille importante

# Note : On pourrait trouver N au lieu de le definir en trouvant le max de la liste