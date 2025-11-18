liste_1 = [x for x in range(50)]
liste_2 = [x**2 for x in range(9)]

print(liste_1)
print(liste_2)

print("Combinaison des deux listes")
print(liste_1 + liste_2)

print("Combinaison des deux listes sans les doublons")
print(set(liste_1 + liste_2))

print("Combinaison des deux listes sans les doublons sous forme de liste")
print(list(set(liste_1 + liste_2)))