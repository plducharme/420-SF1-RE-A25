
fruits = [["pomme", "banane", "raisin"], "kiwi", "orange"]
# le premier élément de la liste retourne une liste
print(fruits[0])

# Comme c'est une liste qui est retourner, on peut accéder à un élément de la sous-liste
print(fruits[0][1])  # retourne la str "banane"
print("Liste avant modification", fruits)
print(fruits)
print("Liste après réassignation d'un élément de la sous-liste")
fruits[0][2] = "melon"
print(fruits)