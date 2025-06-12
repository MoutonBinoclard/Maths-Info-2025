import math

def f(x):
    return math.sin(x**2)

def Rn(fonction, borne_inf, borne_sup, n): # Rectangle à gauche
    largeur_rect = (borne_sup - borne_inf) / n  # Largeur de chaque rectangle
    somme = 0.0
    
    for i in range(n):
        x_i = borne_inf + i * largeur_rect  # Position du coin gauche du rectangle
        somme += fonction(x_i) * largeur_rect  
    
    return somme

def Sn(fonction, borne_inf, borne_sup, n): # Rectangle à droite
    largeur_rect = (borne_sup - borne_inf) / n  # Largeur de chaque rectangle
    somme = 0.0
    
    for i in range(1, n + 1):
        x_i = borne_inf + i * largeur_rect  # Position du coin droit du rectangle
        somme += fonction(x_i) * largeur_rect  
    
    return somme

def Tn(fonction, borne_inf, borne_sup, n): # Trapèze
    largeur_rect = (borne_sup - borne_inf) / n  # Largeur de chaque rectangle
    somme = 0.0
    
    for i in range(n):
        x_i = borne_inf + i * largeur_rect  # Position du coin gauche du rectangle
        x_i_plus_1 = borne_inf + (i + 1) * largeur_rect  # Position du coin droit du rectangle
        somme += (fonction(x_i) + fonction(x_i_plus_1)) * largeur_rect / 2  
    
    return somme



# -------------------------------

# Comparaison de int de sin(t**2) entre 0 et 1 pour les trois methodes avec 100 rectangle

print(Rn(f, 0, 1, 100)) # Rectangle à gauche
print(Sn(f, 0, 1, 100)) # Rectangle à droite
print(Tn(f, 0, 1, 100)) # Trapèze

# Trapèze plus précis

