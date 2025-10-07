voyelles = ["a", "e", "i", "o", "u", "y"]

for lettre in enumerate(voyelles):
    print(lettre)
# Une liste est un itérable... on peut boucler dessus
# enumerate(itérable) retourne un tuple contenant (index de l'itération, l'élément à l'index de l'itération de l'itérable)
for index, lettre in enumerate(voyelles):
    print(f"La voyelle à l'itération {index} est {lettre}")

