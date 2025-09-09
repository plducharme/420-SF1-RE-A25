# Les fonctions sur les strings
serie = "Mercredi est disponible sur Netflix!"
brosse = "J'ai posé ma brosse sur le bureau."
# mettre en majuscule
print(serie.upper())

# mettre en minuscule
print(serie.lower())

# Compter le nombre d'occurrences d'une str dans une autre
# On peut spécifier de où (début) à où (fin inclus) compter
print(brosse.count("os"))
print(serie.count("e", 2, 16))

# Recherche de chaîne, retourne l'index où elle se trouve
# Supporte aussi de spécifier un début et la fin
print(serie.find("dis"))
print(brosse.find("os", 8, 30))
# Cherche à partir de la droite (fin)
print(serie.rfind("i"))

# Remplacement
print(serie.replace("e", "3"))

# split() permet de séparer sur un caractère et retourne une liste (sera vu plus tard)
# Par défaut, sépare sur les espaces ou on peut spécifier le caractère
print(serie.split())





