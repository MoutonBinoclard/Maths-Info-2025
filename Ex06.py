# Part 1

def d(n):
    L=[1]
    for nombre in range(2, n+1):
        if n % nombre == 0:
            L.append(nombre)
    return L

print("appel avec 4:", d(4))
print("appel avec 10:", d(10))

# La fonction d(n) retourne la liste des diviseurs de n
# 1 et lui même inclus

# --------------------

# Part 2

def DNT(n): # DNT pour Diviseur Non Trivial
    L=[]
    for nombre in range(2, n): # On commence à 2 car 1 est trivial, on finit à n-1 car n est trivial
        if n % nombre == 0: # Si reste = 0, c'est un diviseur
            L.append(nombre)
    return L

# --------------------

# Part 3

def sommeCarresDNT(n): # somme des carrés des diviseurs non triviaux
    somme = 0
    for nombre in DNT(n):
        somme += nombre ** 2
    return somme

# --------------------

# Part 4

taille_parcours = 1000
for n in range(1, taille_parcours + 1):
    if n == sommeCarresDNT(n): # Si n est égal à la somme des carrés de ses diviseurs non triviaux
        print(n) # On affiche n