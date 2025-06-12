import random
def creer_liste_aleatoire(a, b, n):
    return [random.randint(a, b) for _ in range(n)]


A=creer_liste_aleatoire(1, 100, 10)
#print(A)

# ------------------------------

# Tri avec commande Python

liste_py = sorted(A)
#print(liste_py)

# ------------------------------

# Numérotation

B=[]
for i in range(len(A)):
    B.append(i)

# ------------------------------

# Tri par insertion, n'uitlise pas la liste B

def tri_insertion(liste):
    for i in range(1, len(liste)):
        valeur=liste[i]
        j=i-1
        while j>=0 and valeur<liste[j]:
            liste[j+1]=liste[j]
            j-=1
        liste[j+1]=valeur
    return liste

print("Tri par insertion")
print(tri_insertion(A))

# ------------------------------

# Tri fusion

def fusion(M, N):
    i, j = 0, 0
    resultat = []
    while i < len(M) and j < len(N):
        if M[i] < N[j]:
            resultat.append(M[i])
            i += 1
        else:
            resultat.append(N[j])
            j += 1
    resultat.extend(M[i:])
    resultat.extend(N[j:])
    return resultat

def fusion_recur(M, N):
    if not M:
        return N
    if not N:
        return M
    if M[0] < N[0]:
        return [M[0]] + fusion_recur(M[1:], N)
    else:
        return [N[0]] + fusion_recur(M, N[1:])

def tri_fusion(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    M = tri_fusion(L[:mid])
    N = tri_fusion(L[mid:])
    return fusion(M, N)

print("Tri fusion")
print(tri_fusion(A))

# ------------------------------

# Tri rapide

def tri_rapide(L):
    if len(L) <= 1:
        return L
    pivot = L[0]
    gauche = [x for x in L[1:] if x < pivot]
    droite = [x for x in L[1:] if x >= pivot]
    return tri_rapide(gauche) + [pivot] + tri_rapide(droite)

print("Tri rapide")
print(tri_rapide(A))
