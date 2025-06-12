def f(x,y,z):
    return x + y + z

def g(x,y,z):
    return x + 2*y + 5*z



def trouver_solu_entier_pos(n, fonction):
    tuple_solu = []
    for x in range(1, n):
        for y in range(1, n):
            for z in range(1, n):
                if fonction(x,y,z) == n:
                    tuple_solu.append((x,y,z))
    return tuple_solu


print(trouver_solu_entier_pos(10, f))
print(trouver_solu_entier_pos(10, g))

#print(trouver_solu_entier_pos(100, f))
#print(trouver_solu_entier_pos(100, g))

#print(trouver_solu_entier_pos(1000, f))
#print(trouver_solu_entier_pos(1000, g))
