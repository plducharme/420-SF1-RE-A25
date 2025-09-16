
# range(10) génère une séquence de 0 à 9
# for i in range(10):
#     print(i)


nombre = int(input("Entrez un nombre: "))
print("Table de multiplication de ", nombre)

print("*" * 20)

for base in range(1, 11):
    print(f"{base} * {nombre} = {base*nombre}")

print("*" * 20)
