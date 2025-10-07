lettres = ["a", "b", "c", "b"]

# index() retourne l'index de la première occurrence de l'élément passé en paramètre; déclanche une erreur si non-existant
print(lettres.index("b"))
# count() retourne le nombre d'occurrences de l'élément dans la liste, déclanche une erreur si non existant
print(lettres.count("b"))

# teste pour la présence
if "z" in lettres:
    print(lettres.index("z"))
else:
    print("z n'est pas dans la liste")

if "b" in lettres:
    print(lettres.count("b"))

if "j" not in lettres:
    print("j n'est pas dans la liste")

