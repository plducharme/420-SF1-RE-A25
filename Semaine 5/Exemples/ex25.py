
def saisie_personne():
    nom = input("Nom: ")
    prenom = input("Prénom: ")
    ville = input("Ville: ")
    pays = input("Pays: ")

    return nom, prenom, ville, pays


# Les variables seront assignées dans le même ordre que le retour de la fonction
nom1, prenom1, ville1, pays1 = saisie_personne()
print(f"{nom1} {prenom1} {ville1} {pays1}")

# Si on spécifie seulement une variable, le tuple contenant les retours sera retourner
reponse = saisie_personne()
print(reponse)
print(f"premier élément retourné {reponse[0]}, deuxième élément retourné {reponse[1]} ...")
