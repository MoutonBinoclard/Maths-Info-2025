import numpy as np

# --------------------

# Part 1

R = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

S = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Matrice R :")
print(R)
print("\nMatrice S :")
print(S)

# --------------------

# Part 2

def test(M): # Prend une matrice M, si carrée, renvoi sa dimension, sinon 0
    if len(M[0]) == len(M): # On compare la longueur de la première ligne avec le nombre de lignes
        return len(M)
    else:
        return 0
    
print("Test de la matrice R :", test(R))
print("Test de la matrice S :", test(S))

# --------------------

# Part 3

# Création d'une fonction pour generer le fichier demandé
def creation_matrice_carre_dans_fichier(dimension, valeur_min, valeur_max, nombre_apres_virgule):
    with open("ex_006.txt", "w") as f:
        for i in range(dimension):
            ligne = []
            for j in range(dimension):
                val = np.random.uniform(valeur_min, valeur_max)
                val = round(val, nombre_apres_virgule)
                ligne.append(str(val))
            f.write('\t'.join(ligne) + '\n')

creation_matrice_carre_dans_fichier(5, 0, 10, 2)


def lecture_matrice_fichier(nom_fichier):
    with open(nom_fichier, "r") as f:
        lignes = f.readlines()
        matrice = []
        for ligne in lignes:
            valeurs = ligne.strip().split('\t')
            matrice.append([float(valeur) for valeur in valeurs])
        return np.array(matrice)

M1 = lecture_matrice_fichier("ex_006.txt")
print("dimension de la matrice lue")
print(test(M1)) # verficiation si la matrice est carrée

# --------------------

# Part 4

# Methode 1 : utilisation des fonctions numpy = ultrarapide = ultra_un_peu_triche_aussi_mdr

valeurs_propres = np.linalg.eigvals(M1)
print("Valeurs propres de la matrice M1 :")
print(valeurs_propres)

# Methode 2 : Faire un truc honnête

def calculer_valeurs_propres(M):
    dimension = test(M)
    if dimension == 0:
        return "La matrice n'est pas carrée."
    
    # Calcul du polynôme caractéristique
    matrice_identite = np.eye(dimension) # On pourrait la faire aussi
    polynome = np.poly(M - matrice_identite)

    # Résolution du polynôme pour trouver les valeurs propres
    valeurs_propres = np.roots(polynome)
    return valeurs_propres

valeur_propores=calculer_valeurs_propres(M1)
# On remarque des racines complexes

# --------------------

# Part 5

# Précision :
# Comme on n'a pas la matrice de base, on ne peut verfier pour la matrice M1
# On peut cependant coder la fonction de vérification

# On considère que les racines sont toutes réelles et stockées
# dans une liste de la forme [racine1, racine2, ..., racineN]
liste_racines_juste = [0.2, 0.5, 0.7, 0.8, 0.01] # Exemple de liste de racines
liste_racines_fausse = [0.2, 0.5, 0.7, 0.8, 0.01, 1.5] # Exemple de liste de racines avec une fausse racine

# Celle la fait tout en une ligne
def dansIntervalle_tres_cool(liste_racines, a, b): # a et b forment un intervalle
    return all(a <= racine <= b for racine in liste_racines)

# Celle la est compréhensible et fait la même chose
def dansIntervalle(liste_racines, a, b): # a et b forment un intervalle
    for racine in liste_racines:
        if racine < a or racine > b:
            return False
    return True

# Test de la fonction dansIntervalle
print("Test de la fonction dansIntervalle avec liste_racines_juste :", dansIntervalle(liste_racines_juste, 0, 1)) # Doit renvoyer True
print("Test de la fonction dansIntervalle avec liste_racines_fausse :", dansIntervalle(liste_racines_fausse, 0, 1)) # Doit renvoyer False

    