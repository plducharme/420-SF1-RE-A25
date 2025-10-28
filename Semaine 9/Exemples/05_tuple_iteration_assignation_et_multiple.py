x = (1, 2, 3, 4)

# On peut faire des assignations multiples (dans les faits, on fait du "unpacking")
a1, a2, a3, a4 = x
print(a1, a2, a3, a4)

# On peut itérer sur un tuple, c'est une séquence indexée
for i in x:
    print(i)

# Version while, peu utilisé
i = 0
while i < len(x):
    print(x[i])
    i += 1

# on peut retourner la longueur d'un tuple avec len()
print(len(x))


