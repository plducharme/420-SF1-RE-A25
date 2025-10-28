import math
# Le unpacking (dépaquetage) de python utilise les tuples à l'interne
val1, val2 = 2, 3
print(val1, val2)
# est équivalent à:
val1, val2 = (2, 3)
print(val1, val2)


# C'est aussi ce que python utilise pour le retour de fonctions
def hypothenuse(a, b):
    c = math.sqrt(a**2 + b**2)
    return a, b, c


adjacent, oppose, hypo = hypothenuse(3, 4)
print(adjacent, oppose, hypo)
