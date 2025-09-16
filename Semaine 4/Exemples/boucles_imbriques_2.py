
nbr_str = input("Nombre épiceries: ")
nombre_epiceries = int(nbr_str)

for i in range(1, nombre_epiceries + 1):
    total = 0.0
    for j in range(1, 4):
        montant = float(input(f"Entrer le montant pour épicerie {i} pour le mois {j}"))
        total += montant
    print(f"Total pour épicerie {i}: {total}")

