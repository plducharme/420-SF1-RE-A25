# Assignation
ma_str = "L'apprentissage du python, ca \"kick\" des culs!"
ma_str2 = 'L\'école, c\'est cool!'

print(ma_str)
print(ma_str2)

# Les str sont indexés à partir de 0 pour les caractères
citation = "La beauté est dans les yeux de celui qui regarde."
for i in range(len(citation)):
    print(citation[i], end="")

# On peut utiliser l'opérateur d'indexation
print(citation[1])


# pour l'opérateur d'indexation [debut:fin:pas], aussi appelé slicing
# ceci retourne un nouvelle str à partir du 3ième caractère jusqu'à la fin
print(citation[2:])
# retourne une nouvelle str à partir du début jusqu'à l'index 15
nouvelle_str = citation[:15]
print(nouvelle_str)

# compter le nombre d'occurrences d'une chaîne de caractères dans une autre
print(citation.count("ui"))

# startswith et endswith permet de vérifier si une chaîne commence ou fini par une autre chaîne de caractères
print(citation.startswith("L"))

# find permet de trouver l'index si l'on trouve une sous-chaîne dans une chaîne, -1 si non-trouvé
# rfind() cherche à partir de la droite (lit de droite à gauche)
print(f"find(): {citation.find("é")}")
print(f"find(): {citation.find("beauté")}")

# join() permet de joindre la chaîne entre les éléments d'une liste
liste_str = ["Bonjour", "les", "amis!"]
print("****".join(liste_str))

# split() permet de séparer les éléments d'une str sur une chaîne en une liste de str
# Par défaut, le caractère est l'espace
str_a_splitter = "Bonjour****les****amis!"
print(str_a_splitter.split("****"))
print(citation.split())

# replace() remplace une chaîne par une autre dans une chaîne
print(citation.replace("beauté", "joie"))
print(citation.replace(" ", ""))

# strip() permet d'enlever une chaîne de caractères au début et à la fin d'une chaîne
# par défaut l'espace
# il existe aussi lstrip() pour seulement le début et rstrip() pour seulement la fin
str_avec_espace = "    Vive les ornithorynques       "
print(str_avec_espace.strip())
str_strip = "!!Super Duper!"
print(str_strip.strip("!"))

# upper() et lower() permettent de retourner la str en majuscules ou minuscules
print(citation.upper())
print(citation.lower())

# Les formats strings (fstrings) permettent le formatage de str. L'expression entre accolades est évaluée et l'on
# peut ajouter des options de formatage.
# fstring convertie en str automatiquement
prix_du_gaz = 1.78
print(f"Le prix du gaz est {prix_du_gaz}")
# Attention sans les fstrings
# print("Le prix du gaz est " + prix_du_gaz)
print("Le prix du gaz est " + str(prix_du_gaz))
pi = 3.141592
# :.nf où n est le nombre de décimales
print(f"Constante de PI: {pi:.3f}")








