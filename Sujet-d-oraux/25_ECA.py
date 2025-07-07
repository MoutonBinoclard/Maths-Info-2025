mot1 = "kayak"
mot2 = "examinateur_de_merde"

def palindrome_via_str(mot):
    return mot==mot[::-1]

def palindrome_via_list(mot):
    liste=[]
    for lettre in mot:
        liste.append(lettre)
    return liste==liste[::-1]


print(palindrome_via_list(mot1))  # True
print(palindrome_via_list(mot2))  # False
print(palindrome_via_str(mot1))  # True
print(palindrome_via_str(mot2))  # False