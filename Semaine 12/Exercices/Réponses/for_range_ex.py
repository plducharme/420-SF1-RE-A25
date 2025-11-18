# Parcourir la str suivant avec une boucle for pour en extraire la première lettres et tous les trois lettres
# subséquentes. La solution peut se faire en deux lignes

cypher = "Awrp1+p>7rL[e6qn-md,tr[meAd dslRqe,i |ppU=y@=t-<h^no(ynpj j$eoMs}<t<u uXc<#o6fo0Tl@&!ZG"

for i in range(0, len(cypher)-1, 3):
    print(cypher[i], end="")

print("*" * 8)
# Imprimer la liste des éléments d'une liste dans l'ordre inverse en utilisant une boucle for
liste_elems = ["Phasmophobia", "Total War: Warhammer 3", "Paladins", "Tavern Keeper"]

for i in range(len(liste_elems)-1, -1, -1):
    print(liste_elems[i])

for i in range(-1, -len(liste_elems)-1, -1):
    print(liste_elems[i])


# Imprimer la liste des éléments d'une liste dans l'ordre inverse en utilisant un built-in de python
liste_valeurs = [42, 666, 89, 26, 99]

# Utiliser des boucles pour aplatir la liste tableau_2d dans tableau_1d: extraire les éléments des listes imbriquées
# pour en faire une liste à 1D
tableau_2d = [["Ils", "ne", "sont"], ["grands", "que", "parce", "que", "nous"], ["sommes", "à", "genoux"]]
tableau_1d = []

for sous_liste in tableau_2d:
    for mot in sous_liste:
        tableau_1d.append(mot)

print(tableau_1d)

tableau_1d_2 = []
for i in range(len(tableau_2d)):
    for j in range(len(tableau_2d[i])):
        tableau_1d_2.append(tableau_2d[i][j])

print(tableau_1d_2)


# Parcourir tableau_2d pour imprimer la phrase sur la même ligne


# Reconstituer la phrase dans la variable "phrase" en ajoutant des espaces entre chaque mot
# i.e. il y a une fonction de str pour cela
phrase = ""


# Imprimer sur une même ligne les 15 premiers nombres de la suite Fibonacci


# Imprimer les multiples de 4 entre 1 et 100 séparés par les caractères "***"


# Utiliser une boucle for avec un range() pour parcourir la liste suivante à partir de la fin en affichant les éléments
# séparés par "-"
liste_inversee = ["croque!", "me", "cric", "grand", "le", "Que"]
