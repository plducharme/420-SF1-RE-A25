liste_noms = ["Alice", "Bob", "Charlie", "David"]
liste_animaux = ["Chien", "Chat", "Furet", "Hamster"]
liste_fruits = ["Pomme", "Orange", "Mandarine", "Goyave"]
liste_sports = ["Hockey", "Soccer", "Judo", "Pelotte basque"]

# Nous voulons faire une liste de dictionnaires où les éléments à l'index x des listes appartiennent à la même personne.
liste_personnes = []

for i in range(len(liste_noms)):
    print(f"index de l'itération\t{i}")
    dictionnaire_personne = {}
    dictionnaire_personne["Nom"] = liste_noms[i]
    dictionnaire_personne["Animal"] = liste_animaux[i]
    dictionnaire_personne["Fruit"] = liste_fruits[i]
    dictionnaire_personne["Sport"] = liste_sports[i]
    print(dictionnaire_personne)
    liste_personnes.append(dictionnaire_personne)

print(liste_personnes)


