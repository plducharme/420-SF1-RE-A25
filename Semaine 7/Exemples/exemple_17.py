# pour copier une liste

couleur = ["Rouge", "vert", "bleu", "rose"]
print(couleur)
# en utilisant l'opérateur d'indexation
nouvelle_liste = couleur[:]
couleur.append("Magenta")
print(nouvelle_liste)
print(couleur)

# En utlisant la fonction copy()
nouvelle_liste_2 = couleur.copy()
print(nouvelle_liste_2)

# en itérant
nouvelle_liste_3 = []
for c in couleur:
    nouvelle_liste_3.append(c)

print(nouvelle_liste_3)


