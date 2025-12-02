# Déclaration d'une liste vide
ma_liste = []
ma_liste1 = list()

# Déclaration avec des éléments
ma_liste3 = [1, 2, 3, 4]

# Déclaration en compréhension
ma_liste4 = [x for x in range(10)]
print(ma_liste4)
ma_liste5 = [i for i in range(25) if i % 5 == 0]
print(ma_liste5)

liste_originale = [1, 2, 3, 4]
# Ajouter un élément à une liste
liste_originale.append(42)
print(liste_originale)

# ajouter une liste à une liste
liste_a_ajouter = [666, 98, 12, 22]
liste_originale.extend(liste_a_ajouter)
print(liste_originale)

# Faire attention
liste_a = [1, 2, 3]
liste_b = [4, 5, 6]
liste_a.append(liste_b)
print(liste_a)

# Les liste sont muables (modifiables)
liste_c = [1, 2, 3, 4]
liste_c[1] = 42
print(liste_c)

# les listes sont passées par référence
liste_src = ["a", "b", "c"]
liste_dst = liste_src
# Si je modifie liste_dst, liste_src sera modifiée, c'est la même liste
liste_dst[0] = "42"
print(liste_dst)
print(liste_src)


# Ceci veut dire qu'une liste passée en paramètre à une fonction peut être modifiée dans la fonction
def modif_liste(liste_a_modifier: list):
    for i in range(len(liste_a_modifier)):
        liste_a_modifier[i] = liste_a_modifier[i] + 1


liste = [1, 2, 3, 4]
modif_liste(liste)
print(liste)


