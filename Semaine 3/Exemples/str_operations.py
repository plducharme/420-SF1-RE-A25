chaine_de_base = "Ceci est ma chaîne de base"
# longueur de la chaîne
print(len(chaine_de_base))
# opérateur d'indexation / extraction de sous-chaînes
# Extraction des caractères à partir du début jusqu'au caractère à l'index 6
print(chaine_de_base[0:7])
# [debut:fin exclus]
print(chaine_de_base[5:23])
# si debut == fin, on obtient une chaîne vide
print(chaine_de_base[0:0])
# si débute > len(s), on obtient une chaîne vide
print(chaine_de_base[27:30])
# Si on omet de spécifier le début, cela débutera à 0
print(chaine_de_base[:23])
# Si on omet de spécifier la fin, ceci terminera à la fin de la chaîne
print(chaine_de_base[5:])
# Et de même...c'est un peu inutile
print(chaine_de_base[:])


