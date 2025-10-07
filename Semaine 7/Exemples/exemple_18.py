chaine = "Votez pour moi"

# split(str) va séparer une str en une liste d'élément selon la str passé en paramètre, par défaut " " (espace)
mots = chaine.split()
print(mots)

date = "2025/10/07"
liste_date = date.split("/")
print(f"On est le {liste_date[2]} du {liste_date[1]} ième mois de l'année {liste_date[0]}")


# str.join(liste) va créer une str en séparant les éléments passée en paramètre par la str sur laquelle join() est appelée
liste_mots = ["Bonjour", "les", "amis"]
phrase = " ".join(liste_mots)
print(phrase)
phrase_2 = "AAA".join(liste_mots)
print(phrase_2)
