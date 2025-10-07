ma_str = "abcdefgh"

lettres = list(ma_str)
print(lettres)
# pop() supprime et retourne le dernier élément de la liste
lettre_poppee = lettres.pop()
print(lettre_poppee)
print(lettres)

# pop(index) peut prendre un index pour faire une pop d'un autre élément de la liste
lettre_poppee_2 = lettres.pop(2)
print(lettre_poppee_2)
print(lettres)

# del supprime, mais ne retourne pas l'élément
del lettres[1]
print(lettres)

# on peut utiliser l'opérateur d'indexation pour supprimer une partie de la liste
del lettres[1:4]
print(lettres)

# clear() supprime tous les éléments de la liste... donne une liste vide
lettres.clear()
print(lettres)
