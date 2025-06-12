import math

# x appartenant à C privée de 1
# f(x) = 1 / (x - 1)²

def f(x):
    if x == 1:
        raise ValueError("x cannot be 1")
    return 1 / ((x - 1) ** 2)

# Question 1 :
# Determiner l'image du cercle trigo par la fonction f

def image_cercle_trigo(precision):
    angles=[0]
    x=[1]
    y=[0]

    while angles:
        angles.append(angles[-1] + precision)
        x.append(math.cos(angles[-1]))
        y.append(math.sin(angles[-1]))

    return (x, y) # Pour un index, x = partie réelle, y = partie imaginaire


