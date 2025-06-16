def permutations(liste): # Fonction récursive pour générer les permutations d'une liste
    if len(liste) == 0: 
        return [[]]
    
    result = []
    
    for i in range(len(liste)):
        elem = liste[i]
        reste = liste[:i] + liste[i+1:]
        for p in permutations(reste):
            result.append([elem] + p)
    return result






# Liste à cette forme : [1, 2, 3, ..., n]

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