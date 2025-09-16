import time


# While True est toujours vrai
while True:
    print("Heure courante: ", time.strftime("%H:%M:%S"))
    reponse = input("Voulez-vous quitter [o/n]")
    if reponse == "o":
        break

print("fin du programme")


