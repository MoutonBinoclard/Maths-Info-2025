def suitea(un):
    if un==1:
        return 1
    
    elif un%3==0:
        return un/3
    
    else :
        return un + 1

def suiteb(un):
    if un==1:
        return 1
    
    elif un%3==0:
        return un/3

    elif un%3 == 1:
        return 2*un +1
    
    else:
        return 2*un -1

def suitec(un):
    if un==1:
        return 1
    
    elif un%2==0:
        return un/2
  
    else:
        return 3*un +1

Nombre_parcours=10000
Nombre_iter=10000

def verif():

    for i in range(1, Nombre_parcours+1):
        liste_base=[i, i, i]
        liste_2=[suitea(i), suiteb(i), suitec(i)]
        while liste_2 != [suitea(liste_2[0]), suiteb(liste_2[1]), suitec(liste_2[2])]:
            liste_2=[suitea(liste_2[0]), suiteb(liste_2[1]), suitec(liste_2[2])]

    print("ok")

#verif()
# Pas de boucle infinie, on a bien des suites stationnaires


def nombre_a_1(taille_parcours):
    """
    Fonction qui renvoie le nombre d'itérations avant d'arriver à 1
    """
    u=[]
    n1=[]
    n2=[]
    n3=[]

    for i in range(1, taille_parcours+1):
        u.append(i)

        liste_base=[i, i, i]
        liste_2=[suitea(i), suiteb(i), suitec(i)]
        compteur =[1,1,1]


        while liste_2[0] != 1 :
            liste_2[0]=suitea(liste_2[0])
            compteur[0] += 1
        
        while liste_2[1] != 1 :
            liste_2[1]=suiteb(liste_2[1])
            compteur[1] += 1
        
        while liste_2[2] != 1 :
            liste_2[2]=suitec(liste_2[2])
            compteur[2] += 1
        
        n1.append(compteur[0])
        n2.append(compteur[1])
        n3.append(compteur[2])
    return u, n1, n2, n3

u, n1, n2, n3 = nombre_a_1(10000)

print(max(n1))
print(max(n2))
print(max(n3))

import matplotlib.pyplot as plt
plt.plot(u, n1, label="suitea")
plt.plot(u, n2, label="suiteb")
plt.plot(u, n3, label="suitec")
plt.legend()
plt.show()
        
