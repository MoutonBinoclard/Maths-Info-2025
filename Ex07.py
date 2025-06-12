# Part 1

alphabet = "abcdefghijklmnopqrstuvwxyz"

# On peut aussi faire
# import string
# alphabet = string.ascii_lowercase

# ou encore
# alphabet = ''.join([chr(i) for i in range(ord('a'), ord('z') + 1)])
# --------------------

# Part 2

def decalage(n, alphabet=alphabet): # retourne l'alphabet décalé de n lettres
    return alphabet[n:] + alphabet[:n] # De n jusqu'à la fin de l'alphabet, puis du début jusqu'à n-1

# --------------------

# Part 3

def indice(x, phrase): # Renvoie les indices de x (un caractère) dans phrase
    indices = []
    for i, char in enumerate(phrase): # enumerate permet d'avoir l'index et la valeur
        # i est l'index, char est la valeur
        if char == x:
            indices.append(i)
    return indices

# --------------------

# Part 4

def codage(n, phrase, alphabet=alphabet):
    alphabet_decale = decalage(n, alphabet)
    resultat = list(phrase) # On transforme la phrase en liste pour pouvoir modifier les caractères
    for lettre in alphabet: # Pour chaque lettre de l'alphabet
        for i in indice(lettre, phrase):
            resultat[i] = alphabet_decale[alphabet.index(lettre)] # On remplace la lettre par sa version décalée (index permet de trouver la position de la lettre dans l'alphabet)
    return ''.join(resultat) # On transforme la liste en chaîne de caractères

# exemple
phrase = "bonjour"
n = 3
print(codage(n, phrase))  # "erqmxur"

# --------------------

# Part 5

# pour décoder, on peut utiliser la fonction codage avec un décalage négatif
