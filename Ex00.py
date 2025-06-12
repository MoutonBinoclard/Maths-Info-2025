# Part 1

n = 1234

q = n // 10 # quotient de n par 10
r = n % 10 # reste de n par 10

print("quotient de n par 10:", q) #123
print("reste de n par 10:", r) #4

# Si on recommence, les restes feront : 4, 3, 2, 1

# --------------------

# Part 2 et 3 simultanément

def somcube(n): # fonction qui retourne la somme des cubes des chiffres de n
    chiffres = []
    while n > 0:
        chiffres.append(n % 10)
        n //= 10
    
    # On a la liste des chiffres d'un nombre, il suffit de la mettre au cube
    
    somme = 0
    for chiffre in chiffres:
        somme += chiffre ** 3
    
    return somme

print(somcube(n))
# On obtient 100 (n=1234), qui correspond à 1^3 + 2^3 + 3^3 + 4^3

# --------------------

# Part 4

distance_parcours=1000

nombre_egal_somme_cubes = [] 
for nombre in range(distance_parcours+1):
    if somcube(nombre) == nombre: # Si la somme des cubes des chiffres de i est égale à i
        nombre_egal_somme_cubes.append(nombre) # On ajoute i à la liste

print("Nombres égaux à la somme de leurs cubes:", nombre_egal_somme_cubes)
# On obtient [0, 1, 153, 370, 371, 407]

# --------------------

# Part 5

def somcube2(n): # On convertit le nombre en chaîne de caractères pour itérer sur les chiffres
    somme = 0
    
    for chiffre in str(n): # str(n) convertit le nombre en chaîne de caractères
        somme += int(chiffre) ** 3 # On reconvertit ensuite en entier pour que la somme marche bien
    
    return somme

print(somcube2(n))
# On obtient à nouveau 100 pour n = 1234