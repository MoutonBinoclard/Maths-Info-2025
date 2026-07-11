import matplotlib.pyplot as plt
import random


# On a deux pions, qui sont initialement sur la case 0,
# on lance un débat et on fait systématiquement avancer le pion qui est derrière.
# On s'arrête quand les deux pions sont sur la même case.

# 1) écrire une fonction lancer() qui simule le lancer du dé à 6faces (à l'aide bibliothèques random)



def lancer():
    return random.randint(1, 6)  # On retourne un entier aléatoire entre 1 et 6 inclus


# 2) écrire une fonction avancer (P) qui avance le pions le plus en arrière
# avec P=[a,b] la position des pions A et B.

def avancer(P):

    valeur_de = lancer()

    if P[0] < P[1]:  # Si le pion A est derrière le pion B
        P[0] += valeur_de  # On avance le pion A
    else:  # Sinon
        P[1] += valeur_de  # On avance le pion B

    return P



# 3) écrire une fonction qui simule une partie complète.


def partie_complete():
    P = [0, 0]  # Initialisation des positions des pions A et B

    # On fait avancer une fois pour pas qu'il ne comence sur la même case

    avancer(P)

    # Puis maintenant on fait tourner

    while P[0] != P[1]:  # Tant que les deux pions ne sont pas sur la même case
        avancer(P)

    return P


# 4) tracer la probabilité que les deux pions arrivent sur la case k 

def enregistrer_n_partie(n):
    compteur_cases = {}  # Dictionnaire pour compter le nombre de fois que les pions se retrouvent sur chaque case

    for _ in range(n):  # On simule n parties

        position_finale = partie_complete()  # On joue une partie complète

        case_finale = position_finale[0]
        
        if case_finale in compteur_cases:
            compteur_cases[case_finale] += 1
        else:
            compteur_cases[case_finale] = 1


    # On va afficher la case finale la plus fréquente juste pour voir

    case_finale_max = max(compteur_cases, key=compteur_cases.get)
    print(case_finale_max)


    # Maintenant il faut tracer


    valeurs_cases = []
    compteur_cases_values = []

    for keys in compteur_cases:
        valeurs_cases.append(keys)
        compteur_cases_values.append(compteur_cases[keys])

    
    plt.bar(valeurs_cases, compteur_cases_values)  # On crée un histogramme
    plt.xlabel('Case finale')  # Label de l'axe des x
    plt.ylabel('Nombre de parties')  # Label de l'axe des y

    plt.show()



enregistrer_n_partie(20000)  # On simule 1000 parties et on trace les résultats
