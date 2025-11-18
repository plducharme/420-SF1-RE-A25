# Déclaration d'un dictionnaire vide
vide = {}
# Équivaut à
vide = dict()

# Déclaration d'un dictionnaire avec des valeurs
mon_dict = {'Nathan': 75, 'Lina': 84, 'Arthur': 69}

# Les clés et les valeurs peuvent être n'importe quels objets (types) de python
# On peut même mélanger les types (pas recommandé)
mon_autre_dict = {1: 2.3, "clé2": "valeur2", 42: [1, 2, 3, 4]}

# Afficher une valeur à partir d'une clé
# On utilise le nom de la clé
print(mon_dict["Lina"])

# On peut aussi utiliser la fonction get(cle) pour retourner la valeur
print(mon_dict.get("Lina"))

# Retirer une paire clé-valeur
# on utilise la fonction del sur la clé du dictionnaire
del mon_dict['Arthur']

# Ajout par assignation
# Si la clé n'existe pas dans le dictionnaire, elle sera ajouté
mon_dict['Bart'] = 92

# Afficher le dictionnaire
print(mon_dict)

# Afficher la liste des clés
print(list(mon_dict))

# Mise à jour de la valeur associée à la clé "Lina"
# Si la clé existe, elle est remplacée par la nouvelle paire de clé-valeur
mon_dict['Lina'] = 88
print(mon_dict)

# Teste l'appartenance à un dictionnaire
# Vérifier si une clé appartient au dictionnaire
print('Arthur' in mon_dict)

# Déclaration d'un dictionnaire en compréhension
coords_y_carre = {x: x**2 for x in (4, 8, 9)}

# Déclaration d'un dictionnaire via le constructeur
# On peut passer une liste de tuples, la clé sera le premier élément du tuple, la valeur, le deuxième
y = dict([(1, 8), (3, 90), (4, 44)])

# Parcourir les clefs et les valeurs
# dict.items() retourne une liste de tuples clé, valeurs
for cle, valeur in coords_y_carre.items():
    print(cle, valeur)

# Si on veut juste la liste des clés
for cle in coords_y_carre.keys():
    print(cle)

# Si on veut juste les valeurs
for val in coords_y_carre.values():
    print(val)

