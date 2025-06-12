from matplotlib import pyplot as plt
import math as mt

# --------------------

# Part 1

def g(x): # définie sur [0, 2[
    if 0 <= x < 1:
        return x
    elif 1 <= x < 2:
        return 1
    else :
        return "Valeur non définie"
    
# Tracé de la fonction g

def creation_x(valeur_min, valeur_max, pas): # Creer une liste de valeurs x entre valeur_min et valeur_max avec un pas donné
    val_x=[]
    while valeur_min < valeur_max:
        val_x.append(valeur_min)
        valeur_min += pas
    return val_x


val_x = creation_x(0, 2, 0.01)
val_y = [g(x) for x in val_x] # Pareil que for i in val_x: val_y.append(g(i))

# Tracé de la fonction
plt.plot(val_x, val_y, label='g(x)', color="#6A3275")
plt.title('Tracé de la fonction g')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.show()

# --------------------

# Part 2

def f(x):
    if 0 <= x < 2: # Condition d'arret de la recursion
        return g(x)
    else:
        return mt.sqrt(x) * f(x - 2)

# --------------------

# Part 3

# Tracé de la fonction f sur l'intervalle [0, 6]

val_x2 = creation_x(0, 6, 0.01)
val_y2 = [f(x) for x in val_x2]

# Tracé de la fonction
plt.plot(val_x2, val_y2, label='f(x)', color="#9B312D")
plt.title('Tracé de la fonction f')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

# --------------------

# Part 4

# Calcul de la plus petite valeur alpha > 0 telle que f(alpha) > 4 à 10^-2 près

alpha = 0.01 # On calcul a 10^-2 près
while f(alpha) <= 4:
    alpha += 0.01

print(f"La plus petite valeur alpha > 0 telle que f(alpha) > 4 est : {alpha:.2f}") # .2f correspond à 2 chiffres après la virgule
