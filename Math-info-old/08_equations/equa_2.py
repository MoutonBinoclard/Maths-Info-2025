import math

def f1(x):
    return 2 * math.sin(x) - 1

def f2(x):
    return x + math.log(x) # log base e

# Trouver la solution f(x) = 0 avec la méthode newton
# La derivé sera calculée numériquement

def calculer_equation_tangeante_et_trouver_intersection(f, x0, présision_derive):
    # Calcule de la dérivée en x0
    derive = (f(x0 + présision_derive/2) - f(x0 - présision_derive/2)) / présision_derive

    # Calcul de l'ordonnée à l'origine de la tangente
    ordonnée_origine = f(x0) - derive * x0 # ax + b = f(x0) - f'(x0) * x0

    # Calcul de l'abscisse de l'intersection de la tangente avec l'axe des abscisses
    x1 = -ordonnée_origine / derive # ax + b = 0 -> x = -b/a

    return x1

def newton(f, x0, présision_derive=1e-7, tol=1e-7):
    while True: # Tant que la solution n'est pas trouvée
        x1 = calculer_equation_tangeante_et_trouver_intersection(f, x0, présision_derive) # Calcul de l'intersect
        if abs(f(x1)) < tol: 
            return x1
        x0 = x1


print("Résolution de l'équation 2 * sin(x) - 1 = 0")
x0 = 0
print(newton(f1, x0))