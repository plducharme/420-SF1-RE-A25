import random

random.seed(42)

liste_nombres = []

for i in range(10):
    liste_nombres.append(random.randint(0, 100))

print(liste_nombres)

# sort(liste) trie la liste en la modifiant
liste_nombres.sort()
print(liste_nombres)

# sorted trie la liste sans la modifier et retourne une nouvelle (triée)
liste_nombres_2 = [42, 66, 3, -4, 81]
liste_triee = sorted(liste_nombres_2)
print(liste_nombres_2)
print(liste_triee)

# on peut triee en ordre décroissant avec le paramètre reverse=True
liste_decroissante = sorted(liste_nombres_2, reverse=True)
print(liste_decroissante)


