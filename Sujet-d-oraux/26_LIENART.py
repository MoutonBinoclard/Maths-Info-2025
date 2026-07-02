# LE SUJET EN GROS
# --------------------------------------
# Le sujet parle de rang, de la mediane et de tri


# CREATION D'UNE LISTE FACTICE
# --------------------------------------
# Pour tester notre code

liste_test1 = [1, 6, 3, 2, 5, 4]
liste_test2 = [1, 6, 3, 2, 5, 4, 7,]
liste_test3 = [1, 6, 3, 2, 5, 4, 7, 8, 9, 10, 3, 6, 4]




# DEBUT DU SUJET
# --------------------------------------

############################
# 1 : Créer une fonction rang(L,a),
# qui renvoie le rang de a dans la liste L
# ( le rang étant défini dans le sujet comme le nombre d'éléments inférieur ou égal à a dans la liste)

def rang(L, a):
    compteur = 0
    for element in L:
        if element <= a :
            compteur += 1
    return compteur

# On va tester pour voir
# print(rang(liste_test1, 6))  # C'est l"élément le plus grand, donc le rang doit être 6
# print(rang(liste_test1, 3))  # Il y a 3 éléments inférieurs ou égaux à 3 (1,2,3), donc le rang doit être 3
# Et c'est ok !





############################
# 2 : Créer une fonction médiane(L),
# la médiane étant ici définie comme le plus petit élément de la liste
# dont le rang est supérieur ou égal a n/2 (n=len(L))

def mediane(L):
    n = len(L)
    element_retenu = None
    for element in L:
        if rang(L, element) >= n / 2:
            if element_retenu is None or element < element_retenu: # Si c'est le premier élément retenu ou si l'élément actuel est plus petit que l'élément retenu
                element_retenu = element
    return element_retenu

# On va tester pour voir
# print(mediane(liste_test1))  # La médiane doit être 3
# print(mediane(liste_test2))  # La médiane doit être 4
# Bien !


############################
# 3 : améliorer la fonction médiane
# pour qu'elle s'arrête si elle trouve
# un nombre dont le rang vaut exactement n/2

def mediane_opti(L):
    n = len(L)
    element_retenu = None
    for element in L:
        rang_element = rang(L, element)
        if rang_element == n / 2:
            return element  # On retourne immédiatement si le rang est exactement n/2
        elif rang_element > n / 2:
            if element_retenu is None or element < element_retenu:  # Si c'est le premier élément retenu ou si l'élément actuel est plus petit que l'élément retenu
                element_retenu = element
    return element_retenu

# On va pas tester, flemme


############################
# 4 : Créer une fonction tri(L)
# qui renvoie la liste triée de L


# Voici ce que LIENART avait noté sur le rapport :
# a l'aide du rang, créér une fonction de tri
# ( il nous donne un bout d'algorithmes qui sert de base;
# en gros, connaissant le nombre d'éléments inférieur ou égaux à un élément de la liste,
# on sait où le repositionner)


# On va essayer de faire ça


def tri(L):
    n = len(L)
    L_triee = [None] * n  # On crée une liste vide de la même taille que L

    for element in L:
        rang_element = rang(L, element)  # On calcule le rang de l'élément
        index = rang_element - 1  # On calcule l'index où placer l'élément (rang - 1 car les indices commencent à 0)

        # On place l'élément à l'index calculé
        # Si cet index est déjà occupé,on recule (une liste avec deux 1, leurs rang sera le meme )
        while L_triee[index] is not None:  
            index -= 1
        L_triee[index] = element

    return L_triee

# On va tester pour voir
# print(tri(liste_test1))  # La liste triée doit être [1, 2, 3, 4, 5, 6]
# print(tri(liste_test2))  # La liste triée doit être [1, 2, 3, 4, 5, 6, 7]
# print(tri(liste_test3))  # La liste triée doit être [1, 2, 3, 3, 4, 4, 5, 6, 6, 7, 8, 9, 10]


############################
# 5 : comparer la complexité de ce tri par rapport aux autres tris classiques

# Tri par rang : O(n^2) car pour chaque élément, on calcule son rang en parcourant toute la liste. Donc pour n éléments, on a n * n = n^2.
# Tri par insertion : O(n^2) dans le pire des cas (liste inversée), mais O(n) dans le meilleur des cas (liste déjà triée).
# Tri fusion : O(n log n) dans tous les cas.

# Le tri par rang reste quand même utilisable