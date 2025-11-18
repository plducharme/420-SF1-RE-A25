
def creer_personne(nom: str, prenom: str, age: int, couleur_preferee: str) -> dict:
    dictionnaire_personne = {"nom": nom, "prenom": prenom, "âge": age, "couleur préférée": couleur_preferee}
    return dictionnaire_personne


def afficher_personne(personne_dict: dict):
    print(f"Nom: {personne_dict["nom"]}")
    print("Prénom:" + personne_dict["prenom"])
    print("Âge: " + str(personne_dict["âge"]))
    print(f"Couleur préférée: {personne_dict["couleur préférée"]}")


jeanne = creer_personne("Durand", "Jeanne", 19, "bleu")

afficher_personne(jeanne)
