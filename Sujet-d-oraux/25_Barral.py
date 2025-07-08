# Sujet sur le déplacement d'une cavalier sur un plateau d'échecs

# Partie 1 :
# à l'aide de tuples, il fallait écrire les déplacements possibles par un cavalier sur le plateau

sauts = ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2))

# Partie 2 :
# écrire une fonction qui regarde quelles sont les déplacements autorisés pour un cavalier

def deplacements_ok(position, sauts):
    sauts_ok = []
    for saut in sauts:
        if 1<= position[0] + saut[0] <=8 and 1 <= position[1] + saut[1] <= 8:
            sauts_ok.append(saut)
    return sauts_ok

# Partie 3 :
# on prend une position, on choisi aléatoirement un saut autorisé et on déplace le cavalier

import numpy as np

def deplacer_cavalier(position, sauts):
    sauts_ok = deplacements_ok(position, sauts)
    index_choisi = np.random.randint(0, len(sauts_ok))
    saut_choisi = sauts_ok[index_choisi]
    nouvelle_position = (position[0] + saut_choisi[0], position[1] + saut_choisi[1])
    return nouvelle_position

# Partie 4 :
# On deplace le cavalier jusqu'il revienne à sa position initiale
# Puis on renvoi le parcours effectué

def jeu(position_initiale, sauts):
    position = position_initiale
    parcours = [position, deplacer_cavalier(position, sauts)]
    while parcours[-1] != position_initiale:
        parcours.append(deplacer_cavalier(parcours[-1], sauts))
    return parcours

# Partie 5 :
# Ecrire les instructions pour afficher le parcours du cavalier
# Je vais mettre la grille pour mieux voir mais ce n'est pas demandé dans l'énoncé
# Un pltplot et pltshow suffisent


def afficher_parcours(parcours):
    import matplotlib.pyplot as plt
    x = [p[0] for p in parcours]
    y = [p[1] for p in parcours]
    
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, marker='o')
    
    # Afficher la grille décalée de 0.5 pour centrer les cases
    plt.xticks([i + 0.5 for i in range(8)], range(1, 9))
    plt.yticks([i + 0.5 for i in range(8)], range(1, 9))
    plt.grid(True)
    plt.show()
    
afficher_parcours(jeu((3, 5), sauts))

# Partie 6 :
# Nombre moyen de cases visitées avant de revenir à la position initiale
# Ainsi que nombre unique de cases visités moyen
# Sur 200 parties

def statistiques(jeu, position_initiale, sauts, n=200):
    cases_visitees = []
    cases_uniques = []
    
    for _ in range(n):
        parcours = jeu(position_initiale, sauts)
        cases_visitees.append(len(parcours))
        co_uniques = []
        for co in parcours:
            if co not in co_uniques:
                co_uniques.append(co)
        cases_uniques.append(len(co_uniques))
    
    moyenne_cases_visitees = sum(cases_visitees) / n
    moyenne_cases_uniques = sum(cases_uniques) / n
    
    return moyenne_cases_visitees, moyenne_cases_uniques

print(statistiques(jeu, (3, 5), sauts, n=200))

# Partie 7 :
# Pas faite
# Fallait tracer le rapport de case unique sur case parcourue en fonction de la case de départ pour toute les cases ? 
# Je sais plus trop