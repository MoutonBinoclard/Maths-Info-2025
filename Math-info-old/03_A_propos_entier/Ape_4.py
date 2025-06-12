def calcul_base_p(n,p): # On prendra soin à ne pas mettre p=1 ou p=0
    reste_division=[]
    while n > 0:
         reste_division.append(n % p)
         n = n // p

    return int(''.join(str(x) for x in reste_division[::-1]))

# ----------------------------------

def base_p_vers_base_10(valeur, p):

    liste_chiffres = []
    for c in str(valeur):
        liste_chiffres.append(int(c))

    n = 0
    for i, chiffre in enumerate(reversed(liste_chiffres)):
        n += chiffre * (p ** i)
    return n

# ----------------------------------

def palindrome_base_p(n, p):
    # On vérifie si n est un palindrome dans la base p
    s = str(calcul_base_p(n, p))
    return s == s[::-1]

# ----------------------------------

def somme_base_2(a, b):
    n1 = base_p_vers_base_10(a, 2)
    n2 = base_p_vers_base_10(b, 2)
    somme = n1 + n2
    return calcul_base_p(somme, 2)

# ----------------------------------

def produit_base_2(a, b):
    n1 = base_p_vers_base_10(a, 2)
    n2 = base_p_vers_base_10(b, 2)
    produit = n1 * n2
    return calcul_base_p(produit, 2)

# ----------------------------------

print(calcul_base_p(10, 2)) # 1010
print(base_p_vers_base_10(1010, 2)) # 10


N=1000
liste_palindrome_base_2_et_10 = []
for i in range(1, N):
    if palindrome_base_p(i, 2) and palindrome_base_p(i, 10):
        liste_palindrome_base_2_et_10.append(i)
print(liste_palindrome_base_2_et_10)
# [1, 3, 5, 7, 9, 33, 99, 313, 585, 717]





