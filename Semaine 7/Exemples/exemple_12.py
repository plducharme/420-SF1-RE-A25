nombres = [17, 38, 10, 25, 72]

# append(elem) va rajouter elemen à la fin de la liste
nombres.append(42)
print(nombres)
# Faire attention, faire un append d'une liste va rajouter la liste en tant qu'élément
nombres_2 = [666, -42]
nombres.append(nombres_2)
print(nombres)
nombres.append("Teste")
print(nombres)

# On peut ajouter les éléments d'une liste au bout de la liste en utilisant extend(liste)
nombres_3 = [1, 2, 3, 4, 5]
nombres_4 = [6, 7, 8, 9, 10]
nombres_3.extend(nombres_4)
print(nombres_3)

# de façon similaire, l'opérateur + est implémenté, équivalent du extend()
nombres_5 = [1, 2, 3]
nombres_6 = [4, 5, 6]
print(nombres_5 + nombres_6)

