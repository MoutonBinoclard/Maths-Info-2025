from math import cos, sin, pi
import matplotlib.pyplot as plt

# --------------------

# Part 1

b = 0.5
w = 6.0

def p(t):
    return (cos(t) + b*cos(w*t),
            sin(t) + b*sin(w*t))

def v(t):
    return (-sin(t) - b*w*sin(w*t),
            cos(t) + b*w*cos(w*t))
def a(t):
    return (-cos(t) - b*w*w*cos(w*t),
            -sin(t) - b*w*w*sin(w*t))

# Verification sur un exemple
t = 0.0
print("Position:", p(t))
print("Vitesse:", v(t))
print("Accélération:", a(t))

# --------------------

# Part 2

def linspace(valeurmin, valeurmax, pas): # renvoie une liste de valeurs entre valeurmin et valeurmax avec un pas donné
    Liste=[]
    while valeurmin <= valeurmax:
        Liste.append(valeurmin)
        valeurmin += pas
    return Liste

val_t = linspace(-pi, pi, 0.01*pi)

L= [p(t) for t in val_t]

# --------------------

# Part 3

plt.plot([L[i][0] for i in range(len(L))], [L[i][1] for i in range(len(L))], label='Trajectoire')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal') # Pour que les axes soient à la même échelle
plt.title('Trajectoire d\'un point') # antislash pour éviter l'erreur de syntaxe
plt.grid()
plt.show()

# --------------------

# Part 4

# Définition de la fonction c (qui donne le centre de courbure)

def c(t): # Définit le centre de courbure en fonction de t
    composante_x = p(t)[0] - d(t) * v(t)[1]
    composante_y = p(t)[1] + d(t) * v(t)[0]
    return (composante_x, composante_y)

def d(t):
    numerateur = v(t)[0]**2 + v(t)[1]**2
    denominateur = v(t)[0]*a(t)[1] - v(t)[1]*a(t)[0]
    return numerateur / denominateur

# test de la fonction c
t = 0.0
print("Centre de courbure:", c(t))

# --------------------

# Part 5

# On calcul toute les coordonées des centres de courbure
C=[c(t) for t in val_t]


plt.plot([C[i][0] for i in range(len(C))], [C[i][1] for i in range(len(C))], label='Centre de courbure', color='orange')
plt.plot([L[i][0] for i in range(len(L))], [L[i][1] for i in range(len(L))], label='Trajectoire')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal') # Pour que les axes soient à la même échelle
plt.title('Trajectoire d\'un point') # antislash pour éviter l'erreur de syntaxe
plt.grid()
plt.show()

# --------------------

# Part 6

def distance(p1, p2): # p1 et p2 sont des tuples (x, y)
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def longeur_courbe(liste_co): # liste_co est une liste de tuples (x, y) (comme L et C)
    longueur = 0.0
    for i in range(len(liste_co) - 1):
        longueur += distance(liste_co[i], liste_co[i + 1])
    
    longueur += distance(liste_co[-1], liste_co[0])  # Pour fermer la courbe
    return longueur

print("Longueur de la courbe:", longeur_courbe(L))
print("Longueur de la dévelopé:", longeur_courbe(C))

# Ce qui a été fait correspond à une valeur de delta_précise
# pour avoir une evolution on peut faire comme ça

L_evo_longueur = []
C_evo_longueur = []

for precision in linspace(0.001, 1, 0.001):
    val_t_evo = (linspace(-pi, pi, precision*pi))
    L_evo = [p(t) for t in val_t_evo]
    C_evo = [c(t) for t in val_t_evo]

    L_evo_longueur.append((longeur_courbe(L_evo), precision))
    C_evo_longueur.append((longeur_courbe(C_evo), precision))

plt.plot([L_evo_longueur[i][1] for i in range(len(L_evo_longueur))], [L_evo_longueur[i][0] for i in range(len(L_evo_longueur))], label='Longueur de la trajectoire')
plt.plot([C_evo_longueur[i][1] for i in range(len(C_evo_longueur))], [C_evo_longueur[i][0] for i in range(len(C_evo_longueur))], label='Longueur de la développée', color='orange') 
plt.xlabel('Précision')
plt.ylabel('Longueur')
plt.show()


# Les distances augmentent lorsqu'on diminue la précision
# On peut aussi faire ça avec les frontières des pays :
# Si on detourait chaque grain de sable, la distance serait enorme
# Alors qui si on utilser des polygones grand et simple, la distance serait plus courte

