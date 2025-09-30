

def trouver_combinaison():
    # boucler sur les nombres possibles
    for i in range(600, 701):
        # S'il n'est pas pair, on continue la prochaine itération
        if i % 2 != 0:
            continue
        # On transforme le nombre en str pour en extraire les chiffres
        nombre_str = str(i)
        chiffre_1 = int(nombre_str[0])
        chiffre_2 = int(nombre_str[1])
        chiffre_3 = int(nombre_str[2])

        if nombre_str.find("3") != -1:
            if chiffre_1 + chiffre_2 + chiffre_3 == 11:
                print(f"Combinaison trouvée: {i}")
                break


# Cette version est pour vous montrer qu'il y a plusieurs façons de résoudre un problème
# On peut le raccourcir en utilisant des fonctions existantes.
# On est passé de 11 lignes à 5 lignes. Cependant, sans les commentaires, cette version pourrait paraître cryptique pour
# un débutant.
def trouver_combinaision_simplifie():
    # Comme il est pair, on va boucler seulement sur les pairs
    for i in range(600, 701, 2):
        # on transforme le nom en str puis en liste de caractères et on vérifie si 3 existe
        if "3" in list(str(i)):
            # Vérifie si la somme des chiffres est 11
            if sum(int(c) for c in list(str(i))) == 11:
                print(f"Combinaison trouvée: {i}")
                break


trouver_combinaison()
trouver_combinaision_simplifie()

