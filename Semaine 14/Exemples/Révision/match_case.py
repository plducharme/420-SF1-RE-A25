# match permet comparer une expression à un cas

choix = int(input("Donnez votre choix"))

match choix:

    case 1:
        print("Choix 1")
    case 2:
        print("Choix 2")
    case 42:
        print("Choix 42")
    case _:
        print("Choix défaut, aucun match des autres cases")


