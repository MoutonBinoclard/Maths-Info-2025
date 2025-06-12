def somme1(nombre_terme):
    somme=0
    for n in range(1, nombre_terme):
        somme+=1/(n**(2.5))
    
    return somme

print(somme1(500))
# Environ 1.3414275392542614

import math as mt

def somme2(nombre_terme):
    somme=0
    for n in range(2, nombre_terme):
        somme += ((-1) ** n) / (mt.log(n) ** 4)
    
    return somme

print(somme2(500))
# Environ 3.8241793362995327