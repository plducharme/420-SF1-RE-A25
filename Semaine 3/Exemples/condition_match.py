
# Sans le match, il peut être long de créer plusieurs elif

# lettre = input("Entrez une lettre: ")
#
# if lettre == "a":
#     print("C'est un a")
# elif lettre == "b":
#     print("C'est un b")
# elif lettre == "c":
#     print("C,et un c")
# else:
#     print("Ce n'est pas a b ou c")

# Avec un match
lettre = input("Entrez une lettre: ")

match lettre:

    case "a":
        print("C'est une a")
    case "b":
        print("C'est un b")
    case "c":
        print("C'est un c")
    case _:  # cas par défaut _ veut dire "any" n'importe quoi
        print("Ce n'est pas un a b ou c")


