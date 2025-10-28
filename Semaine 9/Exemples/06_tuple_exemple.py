langue = ()
data = ((1, "Français", 20), (2, "Français", "Anglais", 30), (3, "Espagnole", "Arabe", 40))

# parcourir les codes de personnes
for t in data:
    print(t[0])

# On parcours les tuples
for t in data:
    # On parcours la partie du sous-tuple dans data, le sous-tuple est le tuple ou l'on enlève le premier et dernier
    # élément
    for j in t[1:len(t)-1]:
        if j in langue:
            continue
        else:
            langue = langue + (j, )

print(langue)

# Extraction de l'âge
age = ()
for i in data:
    age = age + (i[len(i)-1], )

print(age)