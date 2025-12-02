# On définit une fonction en utilisant le mot clé réservé "def"
def ma_fonction():
    print("Ma fonction")


# on appelle une fonction avec son nom et les arguments entre paraenthèses
ma_fonction()


# Les arguments sont déclarés dans les parenthèses
def afficher_nom(nom, prenom):
    print(f"{prenom} {nom}")


# Les arguments sont passés dans l'ordre
afficher_nom("Ducharme", "Pier Luc")


# Les arguments d'une fonction (dans la définition) sont des variables locales
def calcul_fois_x(valeur, x):
    # x et valeur sont des variables locales à la fonction, elles n'existent dans le code global
    return valeur * x


calcul_fois_x(3, 4)
calcul_fois_x(4, 5)


# Les fonctions peuvent retourner une ou plusieurs valeurs
def fonction_retour_une_valeur(x, y):
    return x * y


retour = fonction_retour_une_valeur(3, 4)
print(retour)


def fonction_valeurs_carres(x, y):
    return x**2, y**2


retour1, retour2 = fonction_valeurs_carres(5, 9)
print(retour1)
print(retour2)


# Une fonction qui ne retourne rien, retourne None
def afficher_bonjour():
    print("bonjour")


retour_bonjour = afficher_bonjour()
print(retour_bonjour)
print(afficher_bonjour())


# Ce qui est immuable ne sera pas modifié dans la fonction
def fonction_2(x):
    x = x + 2
    print(f"x dans la fonction {x}")


a = 42
fonction_2(a)
print(f"a après la fonction {a}")


# Les structures passées par référence (muables) comme les listes, vont être modifiées si passé en argument
ma_liste = [1, 2, 3, 4]


def fonction_3(y: list):
    y.append(42)


fonction_3(ma_liste)
print(ma_liste)

retour_print = print("Allo")
print(retour_print)


# On peut ajouter des indices pour la documentation, donnant les types
# ici on sait que la fonction va retourner un float
def calcul_hypothenuse(adjacent: float, oppose: float, nom: str) -> float:
    print(nom)
    return ((adjacent**2) + (oppose**2))**0.5


# Les arguments sont de portée locale, pour utiliser une variable provenant de la portée globale (script principal),
# on utilise le mot clé global
# Il est généralement déconseillé d'utiliser global
z = 42


def fonction_42(x, y):
    # à ce point si, seul x et y existe
    total = x + y
    global z
    z = total + 1


print(z)






