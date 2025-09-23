
while True:
    print("Veuillez choisir une option:")
    print("\toption 1")
    print("\toption 2")
    print("\toption 3")
    print("\toption 4")
    print("\toption 5 - quitter")

    choix = input("Votre choix: ")

    if not choix.isnumeric():
        print("Choix invalide")
        continue
    elif int(choix) not in range(1, 6):
        print("Le choix doit être entre 1 et 5")
        continue
    elif int(choix) == 5:
        break
    else:
        print("Vous avez choisi", choix)

    print("Fin du programme")
    break
