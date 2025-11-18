# Pour définir une structure de données en compréhension
# La notation est
# valeur for valeur in sequence conditions

liste_comp = [valeur for valeur in range(50) if valeur % 10 != 0]
print(liste_comp)

liste_comp2 = [str(i) for i in [1, 42, 64, 99]]
print(liste_comp2)

ensemble_comp = {y for y in range(25) if y != 12 and y != 23}
print(ensemble_comp)

dict_comp = {c: str(c) for c in (1, 2, 4, 6)}
print(dict_comp)
