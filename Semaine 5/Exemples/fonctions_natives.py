phrase = "La mer est calme!"
# len retourne la longueur
print(len(phrase))
# int() converti une str en entier
entier = int("42")
# de la même façon, il y a str() pour convertir en str et float() pour convertir en nombre flottant
ma_str = str(42)
mon_float = float("2.36")

# sum() fait la somme de l'itérable (ex: liste) passé en argument
print(f"Somme:{sum([1, 2, 5, 67, 99])}")

# max() et min() retourne le maximum et le minimum d'un itérable
liste_nb = [5, 1, 6, 9, 2, 42]
print(max(liste_nb))
print(min(liste_nb))

# sorted() pour trier un itérable
print(sorted(liste_nb))
print(sorted(liste_nb, reverse=True))

# range(debut, fin exclus, pas) génère une séquence itérable
for i in range(0, 10):
    print(i)
print("===============")
for i in range(1, 12, 2):
    print(i)

