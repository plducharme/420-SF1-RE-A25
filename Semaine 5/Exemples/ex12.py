
def moyenne(nom, pratique_1, pratique_2, examen_1, examen_2, exercices):
    moyenne_etudiant = (pratique_1 * 20 + pratique_2 * 25 + examen_1 * 20 + examen_2 * 20 + exercices * 15) / 100
    print(f"{nom} a obtenu la moyenne: {moyenne_etudiant}")


moyenne("Alain", 90, 85, 88, 89, 90)
moyenne("Jessica", 60, 85, 95, 89, 90)

# Appel avec arguments nommés
moyenne(pratique_1=98, examen_1=85, pratique_2=68, examen_2=86, exercices=90, nom="Alice")

