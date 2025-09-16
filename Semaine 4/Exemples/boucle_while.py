

nombre = int(input("Entrez le nombre pour la table de multiplication: "))

print("Table de multiplication de ", nombre)
print("**" * 5)

i = 1

while i < 11:
    print(i, " * ", nombre, " = ", i * nombre)
    i += 1  # même chose que i = i + 1

print("**" * 5)


