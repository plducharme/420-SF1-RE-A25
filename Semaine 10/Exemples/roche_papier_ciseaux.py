import random

options = ["Roche", "Papier", "Ciseaux"]


def afficher_choix(choix_joueur, choix_ordi):
    print(f"Joueur: {choix_joueur}\tOrdi: {choix_ordi}")


print(f"Bienvenue à Roche Papier Ciseaux\n")
score_joueur = 0
score_cpu = 0
while True:
    choix = input("[1] Roche\n[2] Papier\n[3] Ciseaux\nVotre choix: ")
    choix_cpu = random.choice(options)

    match choix:
        case "1":
            if choix_cpu == "Roche":
                afficher_choix("Roche", choix_cpu)
                print("Égalité")
            elif choix_cpu == "Papier":
                afficher_choix("Roche", choix_cpu)
                print("Vous avez perdu!")
                score_cpu = score_cpu + 1
            else:
                afficher_choix("Roche", choix_cpu)
                print("Vous avez gagné!")
                score_joueur = score_joueur + 1
        case "2":
            if choix_cpu == "Roche":
                afficher_choix("Papier", choix_cpu)
                print("Vous avez gagné!")
                score_joueur = score_joueur + 1
            elif choix_cpu == "Papier":
                afficher_choix("Papier", choix_cpu)
                print("Égalité")
            else:
                afficher_choix("Papier", choix_cpu)
                print("Vous avez perdu!")
                score_cpu = score_cpu + 1
        case "3":
            if choix_cpu == "Roche":
                afficher_choix("Ciseaux", choix_cpu)
                print("Vous avez perdu!")
                score_cpu = score_cpu + 1
            elif choix_cpu == "Papier":
                afficher_choix("Ciseaux", choix_cpu)
                print("Vous avez gagné!")
                score_joueur = score_joueur + 1
            else:
                afficher_choix("Ciseaux", choix_cpu)
                print("Égalité")
        case _:
            print(f"Choix invalide! {choix}")
            continue

    print(f"Scores:\tJoueur: {score_joueur}\tOrdi: {score_cpu}")

    reponse = input("Voulez-vous continuer à jouer [o/n]")

    if reponse == "o":
        continue
    else:
        break





