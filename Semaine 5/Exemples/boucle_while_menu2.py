
while True:
    print("Veuillez choisir une option:")
    print("\toption 1")
    print("\toption 2")
    print("\toption 3")
    print("\toption 4")
    print("\toption 5 - quitter")

    choix = input("Votre choix: ")

    match int(choix):

        case 1:
            print("option 1")
            break
        case 2:
            print("option 2")
            break
        case 3:
            print("option 3")
            break
        case 4:
            print("option 4 - retour au menu")
        case 5:
            break
        case _:
            print("Choix invalide")
            continue

