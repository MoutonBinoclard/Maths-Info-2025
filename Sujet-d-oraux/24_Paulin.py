liste_choisi = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def separation_deux_paquet(liste):
    index_millieu = int(len(liste)/2)
    L1 = [liste[i] for i in range(index_millieu)]
    L2 = [liste[i] for i in range(index_millieu, len(liste))]
    return L1, L2

def melange_americain(liste):
    L1, L2 = separation_deux_paquet(liste)
    liste_melangee = []
    for i in range(len(L1)):
        liste_melangee.append(L1[i])
        liste_melangee.append(L2[i])
    if len(L1) < len(L2):
        liste_melangee.append(L2[-1])
    return liste_melangee



print(melange_americain(liste_choisi))
