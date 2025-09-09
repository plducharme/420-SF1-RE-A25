# Première manière, utiliser la fonction format() de str
message = "Bonjour {}"
print(message.format("les amis!"))
salut = "Je m'appelle {} {}"
print(salut.format("Pier Luc", "Ducharme"))

# deuxième façon
nom = "Ducharme"
prenom = "Pier Luc"
# Remarquer le "f" avant la chaîne pour la désigner comme format string
salutations = f"Je m'appelle {prenom} {nom}"
print(salutations)


