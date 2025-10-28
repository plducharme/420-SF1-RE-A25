x = (1, 2, 3, 4)
y = ("a", "b", "c")

# concaténation
z = x + y
print(z)

# Répétition
t = y * 4
print(t)

# On ne peut pas ajouter un type autre qu'un tuple à un tuple
# z = z + "d"  #  Donne une erreur
# print(z)

# Mais on peut ajouteur une tuple à un tuple (concaténation)
z = z + x
print(z)