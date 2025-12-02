# Passage d’un nombre arbitraire d’arguments
def f(*args):
    print(*args)


f(3, 5)  # affiche 3, 5
f(3)  # affiche 3
f(3, "Bonjour", 5, True, -0.25)  # affiche 3,Bonjour,5,true,-0.25


# Le *args est le tuple contenant tous les arguments passés
def somme(*args):
    total = 0
    for i in args:
        total += i
    return total


print(somme(1))
print(somme(1, 2, 3, 4, 5))
