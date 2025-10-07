import random as rnd

# Si on veut supprimer un élément on peut utiliser del sur un élément ou remove(valeur) pour supprimer la première
# occurence de la valeur
voyelles = ["a", "e", "i", "o", "u", "y"]
# Supprime un élément en particulier, la liste sera réindexée après
del voyelles[2]
print(voyelles)
print(voyelles[2])

voyelles_2 = ["a", "e", "i", "o", "u", "y", "a"]
# remove(valeur) supprime la première occurrence de la valeur et réindexe la liste
voyelles_2.remove("a")
print(voyelles_2)
# try/except permet d'attraper des exceptions. Matière en extra
try:
    # Ceci génère une erreur, mais on peut l'attraper
    voyelles_2.remove("z")
except ValueError as ve:
    print("Erreur", ve)

print("Fin du programme")
