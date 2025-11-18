import math
# Par défaut, les arguments de fonctions sont pris dans le même ordre que la défintion


def pythagore(oppose, adjacent):
    return math.sqrt(oppose**2 + adjacent**2)


print(pythagore(3.0, 4.0))


# Si vous avez des arguments obligatoires, ils doivent être placés au début de la liste d'arguments
# Si un argument est optionnel, il se trouve vers la fin et peut avoir une valeur par défaut
def personne(nom, prenom, age=18):
    print(nom, prenom, age)


personne("Pinard", "Gina")
personne("Latreille", "François", 32)


# arguments optionnels via le unpacking
def polygone(nom_du_polygone, *coords):
    print(nom_du_polygone, coords)


polygone("triangle", (0, 0), (1, 3), (0, 4))
polygone("carré", (0, 0), (0, 1), (1, 1), (1, 0))


def profile(prenom, nom, **caracteristiques):
    print(prenom, nom, caracteristiques)


profile("Malik", "Lafrance", yeux="Bleus", grandeur=5.3, poids=130)
profile("Joel", "Dubois", voix="haute", cheveux="blonds", grandeur=7.2)




