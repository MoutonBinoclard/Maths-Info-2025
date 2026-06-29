# LE SUJET EN GROS
# --------------------------------------
# Le sujet parle des piles en python.
# Imaginez en gros une pile d'assietes,
# vous pouvez empiler des assiettes les unes sur les autres et les dépiler dans l'ordre inverse.
# First in, First out en gros
# ATTENTION, on pourrai penser qu'il s'agit de programmation bête mais il s'agit ici
# de programmation orienté objet, donc on va devoir créer des classes et des objets pour représenter les piles.


# FONCTION DONNEES DANS LE SUJET (Ne marche pas dans python en vrai)
# --------------------------------------
# On va recoder l'objet pour pourvoir l'utiliser ici (NON DEMANDÉ)

class Pile:

    def __init__(self):
        self.elements = []  # Initialisation de la pile avec une liste vide
    
    def est_vide(self):
        return len(self.elements) == 0  # Retourne True si la pile est vide, sinon False
    
    def empiler(self, element):
        self.elements.append(element)  # Ajoute un élément au sommet de la pile

    def depiler(self):
        if self.est_vide():
            print("La pile est vide, impossible de dépiler.")
        else:
            return self.elements.pop()  # Retire et retourne l'élément au sommet de la pile
        
    def regarder_sommet(self):
        if self.est_vide():
            print("La pile est vide, aucun élément au sommet.")
        else:
            return self.elements[-1]  # Retourne l'élément au sommet de la pile sans le retirer
        

# C'est interessant pour plus tard de savoir faire ça, mais la c'est pas important
# Retenez surtout que vous avez un objet, et pour appliquer une fonction dessus, 
# vous devez faire objet.fonction() et pas fonction(objet)


# PILE FACTICE
# --------------------------------------
# Pour tester le code plus tard on creer rapidement une pile

pile_test = Pile()
pile_test.empiler(1)
pile_test.empiler(6)
pile_test.empiler("Pizza")




# DEBUT DU SUJET
# --------------------------------------

############################
# 1 : Ecrire les instructions pour renvoyer les éléments d'une pile et la longueur de celle-ci
# On peut voir cette question de deux façon :
#    1 - On regarde par index montant, et on donne la longeur
#    2 - on UITLISE les FONCTIONS de l'énoncé !!!!!!! (on va faire ça)

def deplier_et_dire_elements_et_longeur(pile):

    compteur = 0  # Compteur pour la longueur de la pile

    while not pile.est_vide():  # Tant que la pile n'est pas vide
        
        element = pile.depiler()  # On dépile un élément
        print(element)  # On affiche l'élément dépilé
        
        compteur += 1  # On incrémente le compteur

    print("Longueur de la pile :", compteur)  # On affiche la longueur de la pile


# Attention cette fonction va vider la pile, donc si vous voulez garder les éléments, il faudra les stocker dans une autre pile ou liste avant de dépiler.

# Test de la fonction avec la pile de test
# deplier_et_dire_elements_et_longeur(pile_test)  # Cela va afficher les éléments et la longueur de la pile


############################
# 2 : Ecrire une fonction longueur qui prend en argument une pile et renvoie la longueur de celle-ci, la pile ne doit pas être modifiée.
# On gros on va transferer la pile dans une autre, puis faire le chemin inverse en compant
# Par challenge, on va pas utiliser copy.deepcopy, on va faire ça à la main

def longueur_sans_modification(pile):
    pile_temporaire = Pile()  # Création d'une pile temporaire pour stocker les éléments dépilés

    # Transfert dans une autre pile, donc ça sera inversé

    while not pile.est_vide():
        element = pile.depiler()  # On dépile un élément de la pile originale
        pile_temporaire.empiler(element)  # On empile cet élément dans la pile temporaire

    # pile est maintenant vide, pile_temporaire contient les éléments dans l'ordre inverse

    compteur = 0  # Compteur pour la longueur de la pile
    while not pile_temporaire.est_vide():
        element = pile_temporaire.depiler()  # On dépile un élément de la pile temporaire
        pile.empiler(element)  # On empile cet élément dans la pile originale pour la restaurer
        compteur += 1  # On incrémente le compteur

    # pile est de retour à la normale, pile_temporaire est vide

    return compteur  # On retourne la longueur de la pile

# Je trouve vraiment ça super nul, mais bon

# Test de la fonction avec la pile de test
# print(pile_test.elements)  # Affiche les éléments de la pile avant de calculer la longueur
# longueur_sans_modification(pile_test)  # Cela va renvoyer la longueur
# print(pile_test.elements) # Rien n'a été modifié, la pile est toujours intacte



############################
# 3 : Ecrire une fonction a_l_envers qui prend en argument une pile et 
# renvoie une pile qui possède les même éléments mais dans l'ordre inverse,
# la pile de départ ne doit pas être modifiée. On ne peut utiliser que des piles (pas de liste,tuple...)
# Attention, si on fait pile2 = pile ça ne marche pas, ça va juste copier l'adresse de la pile, donc on va devoir faire un truc à la main


# Donc quand on retournera, on mettra chaque élements dans deux piles, puis on n'en retournera qu'une seule à la fin


def a_l_envers(pile):
    pile_temporaire = Pile()  # Création d'une pile temporaire pour stocker les éléments dépilés
    pile_inverse = Pile()  # Création d'une pile pour stocker les éléments dans l'ordre

    while not pile.est_vide():
        element = pile.depiler()  # On dépile un élément de la pile originale
        pile_temporaire.empiler(element)  # On empile cet élément dans la pile temporaire
        pile_inverse.empiler(element)  # On empile cet élément dans la pile inverse
    
    # il faut maintenant remettre les éléments dans la pile originale pour ne pas la modifier
    while not pile_temporaire.est_vide():
        element = pile_temporaire.depiler()  # On dépile un élément de la pile temporaire
        pile.empiler(element)  # On empile cet élément dans la pile originale pour la restaurer

    return pile_inverse  # On retourne la pile inverse


# test de la fonction
# pile_retournee = a_l_envers(pile_test)  # Cela va renvoyer une pile avec les éléments dans l'ordre inverse
# print(pile_retournee.elements)  # Affiche les éléments de la pile retournée
# print(pile_test.elements)  # Affiche les éléments de la pile originale pour vérifier qu'elle n'a pas été modifiée
# Tout est bon !

############################
# 4 : Ah bah il s'en souvient pas, sacré Milos quand même (nan vraiment le compte rendu est bien rempli quand même gg)




############################
# 5 : On veut simplifier les calculs élémentaire.
# Ecrire une fonction f qui prend en argument un calcul élémentaire et qui renvoie toutes les combinaisons de calculs simplifiés.

# Exemple :
#  f("3*(2+2)+6*2") renvoie
# ["3*4+6*2", "3*(2+2)+12","3*4+13"]

# Indications: on utilisera deux piles, l'une qui à chaque fois que "(" apparait dans la phrase on empile son indice dans la phrase.
# L'autre qui a chaque fois que ")" apparait dans la phrase on extrait le terme entre parenthèses dans la phrase
# et on utilise val() + str() pour le calculer et le mettre sous forme de string.


"""
JE FERAI çA PLUS TARD MERDE !
"""