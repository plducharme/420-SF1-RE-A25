fruits = [["raisin", "papaye", "pomme"], "pamplemousse", "ananas", "citron", "poire", "banane", ["lime", "papaye"]]

# affiche la liste en entier
print(fruits)
# Affiche le premier élément de la liste (qui est une liste)
print(fruits[0])
# Affiche le premier élément de la liste dans la liste
print(fruits[0][0])

# Affiche le dernier élément de la liste
print(fruits[len(fruits) - 1])
# Autre façon... les index négatifs partent de la fin
print(fruits[-1])
# Avant-dernier élément
print(fruits[-2])

# On peut retourner une partie de la liste en utilisant l'opérateur d'indexation [:]
# [debut:fin exclus]
print(fruits[0:3])
print(fruits[2:8])
# Si on omet la valeur de début, le début de la liste est utilisé: index = 0
print(fruits[:3])
# Si on omet la fin, retourne jusqu'à la fin de la liste
print(fruits[2:])
# on peut retourner la liste au complet en tant que nouvelle liste
print(fruits[:])
# on peut spécifier le pas (step) [debut : fin exclus : pas] pour retourner chaque "pas" élément
print(fruits[::2])
