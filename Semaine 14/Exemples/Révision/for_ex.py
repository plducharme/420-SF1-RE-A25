# for element in sequence parcours la séquence élément par élément
for i in range(10):
    print(i)

ma_liste = ["Pierre", "Jean", "Jacques"]
for nom in ma_liste:
    print(nom)

# enumerate permet d'itérer sur les éléments en gardant l'index
for index, element in enumerate(ma_liste):
    print(f"itération {index} élément:{element}")

# range(debut: fin_exclus: pas)
for i in range(0, 10, 2):
    print(i)
