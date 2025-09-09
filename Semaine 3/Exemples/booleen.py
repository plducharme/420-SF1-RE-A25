# Par convention True = 1, False = 0
print(int(True))
print(int(False))

print(True)

# Donc...
somme = 42 + True
print(somme)
mult = 8 * True
print(mult)

# opérateurs de comparaison
valeur_1 = 42
valeur_2 = 42
valeur_3 = 666

# égalité
print("Égalité")
print(valeur_1 == valeur_2)
# inégalité
print("Inégalité")
print(valeur_1 != valeur_2)
# plus grand / plus petit
print(valeur_1 < valeur_3)
print(valeur_1 > valeur_2)
# plus grand ou égal / plus petit ou égal
print(valeur_1 <= valeur_3)
print(valeur_1 <= valeur_2)
print(valeur_3 <= valeur_3)
print(valeur_1 >= valeur_3)
print(valeur_1 >= valeur_2)

# Comparaison de texte
# Utilise l'ordre alphabétique, attention les majuscules et minuscule sont deux caractères différents
# La comparaison utilise la valeur numérique des caractères (majuscule < minuscule)
print("Comparaison de texte")
print("aubergine" < "poire")
print("david" == "david")
print("David" == "david")
print("david" < "David")
print("david" < "davod")

# Comparaison booléenne
# False = 0, True = 1
print("Comparaison booléenne")
print(False < True)  # True
print(False == False)  # True
# On peut le faire avec tous opérateurs de comparaison (<, >, !=, >=, <=)

# opérateurs booléens
# not, and, or
vrai = True
faux = False
print(vrai or faux)  # True
print(vrai and faux)  # False
print((3 > 4) or (3 != 4))  # True







