import random as rnd

nombre_essais_max = 5
nombre_a_deviner = rnd.randint(1, 10)
nombre_essais = 1

while nombre_essais <= nombre_essais_max:
    tentative = int(input("Quel nombre j'ai choisi (entre 1 et 10): "))

    if tentative == nombre_a_deviner:
        print("Bravo c'est le bon nombre!")
        break
    else:
        print("Ce n'est pas le bon nombre!")
    nombre_essais += 1

if nombre_essais == nombre_essais_max + 1:
    print("Nombre d'essais maximum atteint. Vous avez perdu!")








