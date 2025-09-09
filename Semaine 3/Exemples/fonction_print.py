passe_partout = "Pousse, pousse, pousse, les bons bons légumes!"
nombre = 42

# Impression / affichage de base
print(passe_partout)
# si on print() un nombre (int, float, complexe), il sera converti en str
print(nombre)
# pour faire un print() d'un mixte de str et nombre, on doit explicitement convertir le nombre en str
print(passe_partout + str(nombre))
print("Choix: \n1) choix 1\n2) choix 2")
# print() prend un nombre illimité d'arguments de type str, il va les concatener en ajoutant un espace
print("pomme", "poire", str(nombre), "autre str")


# Conversion implicite
print(42)  # va implicitement faire un str(42)
print(True)  # str(True)
print(type(True))
print(False)
print(type(False))

