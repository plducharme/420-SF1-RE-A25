# Écrivez un programme qui demande à l'utilisateur de deviner un nombre entre 1 et 20
# Demandez le nombre à l'utilisateur tant qu'il n'est pas correct
# Si le nombre de l'utilisateur n'est pas le bon, afficher "plus haut" ou "plus bas", le cas échéant
# Si le nombre est le bon, afficher "Bravo" avec le nombre d'essais
import random

nombre_a_deviner = random.randint(1, 20)
nombre_essais = 0

while True:

    choix = int(input("Veuillez choisir un nombre entre 1 et 20: "))

    nombre_essais += 1

    if choix < nombre_a_deviner:
        print("Le nombre est plus haut")
    elif choix > nombre_a_deviner:
        print("Le nombre est plus bas")
    else:
        print(f"Bravo! Nombre d'essais: {nombre_essais}")
        break

