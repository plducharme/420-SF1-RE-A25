
phrase = input("Entrez une phrase: ")

lettre = input("Veuillez entrer la lettre: ")

nombre_occurences = 0

for c in phrase:
    if c == lettre:
        nombre_occurences += 1

print(f"Il y a {nombre_occurences} fois la lettre '{lettre}' dans la phrase: '{phrase}'")

