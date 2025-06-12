def verif_ellipse(x, y):
    if (x - 2*y + 3)**2 + (3*x + 4*y - 1)**2 <= 100:
        return True
    return False

def verif_domaine(x, y):
    verif1, verif2 = False, False

    if 1 < x*y < 2 : verif1=True
    if x < y < 2*x : verif2=True

    if verif1 and verif2 : return True

    return False

# Manque les aires