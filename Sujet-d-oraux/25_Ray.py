# 1
# Faire une fonction P telle que P renvoie le produit scalaire entre 2 listes. Par exemple P([1,2,3],[4,1,0])=6

def P(liste1, liste2):
    if len(liste1) != len(liste2): # Verif si listes de même longueur
        return None

    else :
        produit_scalaire = 0
        for index in range(len(liste1)):
            produit_scalaire += liste1[index] * liste2[index]
        return produit_scalaire


# 2
# Ecrire une fonction pal1 qui prend une liste et qui renvoie True si la liste est un palidrome et False sinon. Par exemple pal1([1,0,2,0,1]) renvoie True

def pal1(liste):
    return liste == liste[::-1]  # Vérifie si la liste est égale à sa version inversée 

# 3
# Ecrire une fonction pal2 qui prend deux listes L et C et qui renvoie true si L est un palindrome, si les longueurs des deux listes sont égales et si
# sum de 0 à d-1 de l(i) * c(d-1-i) = sum de 0 à d-1 de c(i) * l(i)

def pal2(L, C):
    if len(L) != len(C):
        return False  # Les listes doivent être de même longueur

    d = len(L)
    if L != L[::-1]:  # Vérifie si L est un palindrome
        return False

    somme1 = sum(L[i] * C[d - 1 - i] for i in range(d))
    somme2 = sum(C[i] * L[i] for i in range(d))

    return somme1 == somme2  # Vérifie l'égalité des sommes

