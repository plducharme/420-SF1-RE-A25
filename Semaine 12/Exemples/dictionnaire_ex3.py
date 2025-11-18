dict_personne_age = {"Alice": 18, "Bob": 37, "Charlie": 42, "David": 23}


while True:
    print("Ajouter au dictionnaire [1]")
    print("Supprimer du dictionnaire [2]")
    print("Afficher le dictionnaire [3]")
    print("Quitter [4]")
    print("Moyenne d'âge [5]")

    choix = input("Votre choix [1, 2, 3, 4, 5]: ")

    # while choix != "1" and choix != "2" and choix != "3" and choix != "4":
    while choix not in ["1", "2", "3", "4", "5"]:
        choix = input("Votre choix [1, 2, 3, 4, 5]: ")

    if choix == "1":
        ajout = input("Entrez un nom et l'âge sous la forme [nom/âge]")
        liste_ajout = ajout.split("/")
        # Après le split, le nom sera à l'index 0 et la str de l'âge à l'index 1 de liste_ajout
        dict_personne_age[liste_ajout[0]] = int(liste_ajout[1])
    elif choix == "2":
        suppression = input("Entrez le nom à supprimer: ")
        try:
            # Si la clé n'existe pas, une exception KeyError est levée.  Le try/except permet de gérer l'exception pour
            # pas que le programme crash
            del dict_personne_age[suppression]
        except KeyError as ke:
            print(f"Clé inexistante {ke}")
    elif choix == "3":
        print(dict_personne_age)
    elif choix == "4":
        break
    elif choix == "5":
        total = 0

        for age in dict_personne_age.values():
            total += age

        print(f"Moyenne âge {total / len(dict_personne_age)}")






