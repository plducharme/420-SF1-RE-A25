chaine_acides_amines = input("Entrez la chaîne d'acides aminés: ")
chaine_acides_amines = chaine_acides_amines.upper()


def valider_chaine(chaine: str) -> bool:

    for c in chaine:
        match c:
            case "A":
                continue
            case "R":
                continue
            case "W":
                continue
            case "G":
                continue
            case _:
                return False
    return True


def afficher_frequence(chaine: str):
    longueur_chaine = len(chaine)
    print("Fréquence % de A", chaine.count("A")/longueur_chaine*100)
    print("Fréquence % de R", chaine.count("R")/longueur_chaine*100)
    print("Fréquence % de W", chaine.count("W")/longueur_chaine*100)
    print("Fréquence % de G", chaine.count("G")/longueur_chaine*100)


if valider_chaine(chaine_acides_amines):
    afficher_frequence(chaine_acides_amines)
else:
    print("Chaîne non valide")

