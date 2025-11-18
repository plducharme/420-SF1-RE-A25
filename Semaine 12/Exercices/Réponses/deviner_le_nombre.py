import random

# Écrivez un programme qui demande à l'utilisateur de deviner un nombre entre 1 et 20
# Demandez le nombre à l'utilisateur tant qu'il n'est pas correct
# Si le nombre de l'utilisateur n'est pas le bon, afficher "plus haut" ou "plus bas", le cas échéant
# Si le nombre est le bon, afficher "Bravo" avec le nombre d'essais

nombre_a_deviner = random.randint(1, 21)
print("Génération d'un nombre entre 1 et 20")
nb_essais = 0

while True:

    essai = input("Essayez de deviner le nombre entre 1 et 20: ")

    # Validation de l'input (pas dans les consignes), lorsque l'on met plusieurs conditions,
    # l'ordre des conditions peut être importante
    while not essai.isnumeric() or int(essai) < 1 or int(essai) > 20:
        print("Nombre invalide")
        essai = input("Essayez de deviner le nombre entre 1 et 20: ")

    nb_essais += 1
    if int(essai) == nombre_a_deviner:
        print(f"Bravo! nombre d'essais {nb_essais}")
        break
    elif int(essai) < nombre_a_deviner:
        print("Plus haut!")
    else:
        print("Plus bas!")

