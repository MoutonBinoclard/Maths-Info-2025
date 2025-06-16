def permutations(liste): # Fonction récursive pour générer les permutations d'une liste

    if len(liste) == 0: # Simple verification, si la liste est vide, aucune permutation
        return [[]]
    
    result = []
    
    for i in range(len(liste)):
        elem = liste[i]
        reste = liste[:i] + liste[i+1:]
        for p in permutations(reste):
            result.append([elem] + p)
    return result

def permu_non_recursif(liste):
    result = [[]]    
    for elem in liste :
        new_result = []
        for p in result:
            for i in range(len(p) + 1):
                new_result.append(p[:i] + [elem] + p[i:])
        result = new_result
    return result


n = 3
print(permutations(list(range(1, n+1))))
print(permu_non_recursif(list(range(1, n+1))))


"""
Explication étape par étape de la fonction permu_non_recursif (Avec liste = [1, 2, 3]) :

result = [[]]

-----------------------
premiere boucle

elem = 1
new result = []
p = []
On insère 1 à chaque position possible dans p -> ici il n'y a qu'une position
new_result = [[1]]
result = [[1]]

-----------------------
deuxieme boucle

elem = 2
new_result = []
p = [1]
On insère 2 à chaque position possible dans p -> il y a 2 positions possibles
new_result = [[2, 1], [1, 2]]
result = [[2, 1], [1, 2]]

-----------------------
troisieme boucle
elem = 3
new_result = []
p = [2, 1] puis p = [1, 2]
On insère 3 à chaque position possible dans p -> il y a 3 positions possibles
new_result = [[3, 2, 1], [2, 3, 1], [2, 1, 3], [1, 2, 3], [1, 3, 2], [3, 1, 2]]
result = [[3, 2, 1], [2, 3, 1], [2, 1, 3], [1, 2, 3], [1, 3, 2], [3, 1, 2]]
"""