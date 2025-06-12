# Ecriture de la liste exemple

t1= [0,1,1,1,0,0,0,1,0,1,1,0,0,0,0]

# --------------------

# Part 1

def nombreZeros(t, i):
    #  renvoie combien de 0 il y a à la suite à partir de l'indice i
    # 0 si t[i] = 1
    if i >= len(t) or t[i] != 0:
        return 0
    else:
        return 1 + nombreZeros(t, i + 1)
        # Recursivité pas forcement opti ici, mais bon pour une petit liste c'est stylé


print("Nombre de 0 à partir de l'indice 4:", nombreZeros(t1, 4)) # 3
print("Nombre de 0 à partir de l'indice 1:", nombreZeros(t1, 1)) # 0
print("Nombre de 0 à partir de l'indice 8:", nombreZeros(t1, 8)) # 1

# --------------------

# Part 2

# Si on connait la liste des nombres de 0 à partir de chaque indice
# Il suffit de trouver la valeur max de cette liste

def nombreZerosMax(t):
    return max(nombreZeros(t, i) for i in range(len(t)))

# pour l'ecrire de manière de manière plus simple, on peu faire comme ça :

def nombreZerosMaxSimple(t):
    liste_zeros=[]
    for i in range(len(t)):
        liste_zeros.append(nombreZeros(t, i))
    return max(liste_zeros)

print("Nombre maximal de 0 consécutifs:", nombreZerosMax(t1)) # 4
print("Nombre maximal de 0 consécutifs (simple):", nombreZerosMaxSimple(t1)) # 4

# --------------------

# Part 3

# Complexité de nombreZeros :
# O(n) car on parcourt la liste à partir de l'indice i jusqu'à un 0 ou la fin de la liste

# Complexité de nombreZerosMax :
# O(n^2) car on parcourt la liste pour chaque indice i, donc n fois O(n)

# --------------------

# Part 4

# On saute directement à la fin de chaque séquence de zéros.

def nombreZerosMaxOptimise(t):
    i = 0
    max_zeros = 0
    while i < len(t):
        n = nombreZeros(t, i) # n et le nombre de 0 consécutifs
        if n > max_zeros:
            max_zeros = n
        
        if n == 0: # Si on est sur un 1, on passe à l'indice suivant
            i += 1
        else: # Si on est sur un 0, on saute toute la séquence de 0
            i += n
    return max_zeros

print("Nombre maximal de 0 consécutifs (optimisé):", nombreZerosMaxOptimise(t1))