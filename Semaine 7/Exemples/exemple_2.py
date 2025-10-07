# le premier élément de la liste est un tuple qui n'est pas modifiable
fruits = [("pomme", "banane", "raisin"), "autre élément", "dernier élément"]

fruits[0][0] = "orange" # donnera une erreur