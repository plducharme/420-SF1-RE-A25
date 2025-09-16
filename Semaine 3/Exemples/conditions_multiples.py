

nombre = int(input("Entrez un nombre:\t"))

if (nombre % 5 == 0) and (nombre % 3 == 0):
    print("divisible par 5 et 3")
elif nombre % 5 == 0:
    print("divisible par 5")
elif nombre % 3 == 0:
    print("divisible par 3")
else:
    print("N'est pas divisible par 5 ou par 3")

print("Fin du programme!")
