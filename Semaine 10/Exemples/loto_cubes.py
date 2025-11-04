import random

# Liste représentant les cubes dans le sac de loto. Ne pas modifier cette liste
sac_cubes = ["bleu", "rouge", "vert", "bleu", "bleu", "rouge"]


solde = 10

while solde > 0:

    cube1 = random.choice(sac_cubes)
    cube2 = random.choice(sac_cubes)
    cube3 = random.choice(sac_cubes)
    print(f"tirage {cube1} {cube2} {cube3}")
    solde = solde - 1

    if cube1 == cube2 == cube3:
        if cube1 == "vert":
            solde += 10
        elif cube1 == "rouge":
            solde += 5
        else:
            solde += 3
    elif cube1 != cube2 != cube3 != cube1:
        solde = solde + 1

    if solde > 0:
        reponse = input("Continuer à jouer [o/n]?")

        if reponse == "o":
            continue
        else:
            break

if solde == 0:
    print("Vous avez perdu!")
elif solde > 10:
    print(f"total des gains: {solde - 10}")
elif solde < 10:
    print(f"total des pertes: {10 - solde}")
else:
    print("kif-kif")