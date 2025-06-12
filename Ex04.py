# Contexte

# n = entier naturel strictement positif
# 0 <= p <= 1
# X et Y deux variables aléatoires dans N sur un espace probabilisé donné

# X suit un loi de Poisson de paramètre lambda = n*p
# Y suit une loi binomiale de paramètres n et p

# --------------------

# Part 1

# On rappelle la loi de Poisson :
# P(X = k) = exp(-lambda) * lambda^k / k! pour k >= 0

from math import exp, factorial, comb

def Px(k, n, p): # Renvoie P(X = k) pour X suivant une loi de Poisson
    
    lam = n * p # lambda n'est pas autorisé comme nom de variable dans Python
    return exp(-lam) * lam**k / factorial(k)

n = 30
p = 0.1
probs_poisson = [Px(k, n, p) for k in range(n+1)] # On fait une liste des probabilités pour k de 0 à n
print("Probabilités de la loi de Poisson:", probs_poisson)

# --------------------

# Part 2

# On rapelle la loi binomiale :
# P(Y = k) = (k parmi n) * p^k * q^(n-k) pour 0 <= k <= n

def Py(k, n, p): # Renvoie P(Y = k) pour Y suivant une loi binomiale
    return comb(n, k) * p**k * (1 - p)**(n - k)

n= 30
p = 0.1
probs_binomiale = [Py(k, n, p) for k in range(n + 1)]
print("Probabilités de la loi binomiale:", probs_binomiale)

# --------------------

# Part 3

def Ecart(n, p):
    # Renvoi le plus grand écart entre les probabilités de la loi de Poisson et de la loi binomiale
    max_ecart = 0
    for k in range(n + 1):
        ecart= abs(Px(k, n, p) - Py(k, n, p))
        if ecart > max_ecart:
            max_ecart = ecart
    
    return max_ecart

# --------------------

# Part 4

def N(e, p): # Renvoie le plus petit entier n tel que l'écart entre les probabilités de la loi de Poisson et de la loi binomiale est inférieur à e
    n = 1
    while Ecart(n, p) > e:
        n += 1 # Tant que l'écart est supérieur à e, on incrémente n
    return n

# --------------------

# Part 5

# Application numérique

# Cas 1 : p = 0.075, e = 0.008
n1 = N(0.008, 0.075)
print(f"Pour p = 0.075 et e = 0.008, n = {n1}")

# Cas 2 : p = 0.075, e = 0.005
n2 = N(0.005, 0.075)
print(f"Pour p = 0.075 et e = 0.005, n = {n2}")

# Cas 3 : p = 0.1, e = 0.008
n3 = N(0.008, 0.1)
print(f"Pour p = 0.1 et e = 0.008, n = {n3}")

# Erreur dans le cas 4, valeur trop grande pour python ? 
"""
# Cas 4 : p = 0.1, e = 0.005
n4 = N(0.005, 0.1)
print(f"Pour p = 0.1 et e = 0.005, n = {n4}")
"""

# Interprétation du dernier résultat :
print("Lorsque p augmente ou que e diminue, il faut un n plus grand pour que la loi de Poisson soit une bonne approximation de la loi binomiale.")