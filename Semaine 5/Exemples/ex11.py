
def anniversaire(langue: str, nom: str):
    if langue == "fr":
        print("Joyeux anniversaire", nom)
    elif langue == "an":
        print("Happy Birthday", nom)
    else:
        print("Langue non supportée")


langue_input = input("Entrez la langue désirée: ")
nom_input = input("Entrez votre nom: ")

anniversaire(langue_input, nom_input)



