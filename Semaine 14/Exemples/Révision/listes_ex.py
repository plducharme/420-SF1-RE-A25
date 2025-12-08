ma_liste = ["Alice", "Bob", "Charlie", "David", "Eloi"]

# l'opérateur de tranchage [debut: fin_exclue: pas](slicing) retourner une sous-liste
nouvelle_liste = ma_liste[1:3]
print(nouvelle_liste)

print(ma_liste[0::2])

# Si on appelle l'opérateur de tranchage (slicing) comme ceci, cela va inverser la séquence (liste, str, etc)
print(ma_liste[::-1])

