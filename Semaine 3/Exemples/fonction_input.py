# input() permet à l'utilisateur d'entrer une str
# prend en paramètre un str de ce que l'on veut afficher / demander à l'utilisateur
# retourne une str
age = input("Quel est ton âge?")
print(age)
print(type(age))

# Faire attention aux types, input retourne une str
n1 = input("Nombre 1: ")
n2 = input("Nombre 2: ")
# n1 + n2 donne la concatenation des deux str et non l'addition des nombres
print(n1 + n2)
# pour additionner les nombres, il faut les convertir avec int() ou float()
somme = int(n1) + int(n2)
print(somme)







