def palindrome (mot):
    # Verifie si le mot est un palindrome
    return mot == mot[::-1]
    # Pensez au slicing, c'est vraiment pas mal

# test de la fonction
mot_choisi = "kayak"
mot_choisi2 = "bonjour"
print(palindrome(mot_choisi))
print(palindrome(mot_choisi2))


