# insert(idx, elem) insert elem à l'index idx

jours = ["Lundi", "Jeudi", "Vendredi", "Samedi"]
jours.insert(1, "Mardi")
print(jours)

jours.insert(0, "Dimanche")

# Pour insérer à la fin
# append()
jours.append("Patate")
print(jours)
# en utilisant l'index du dernier élément
jours.insert(len(jours), "Toto")
print(jours)


