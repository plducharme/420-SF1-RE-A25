
ma_string = "L'homme est un animal politique"
auteur = "Aristote"
nombre = 42.26999999

# print régulier
print(ma_string, "-", auteur, nombre)

# print régulier avec séparateur
print(ma_string, "-", auteur, nombre, sep="->")

print(ma_string, "-", auteur, round(nombre, 2))

print("La citation:\t" + ma_string + " est de " + auteur + str(round(nombre, 2)))
print("La citation:\t", ma_string, " est de ", auteur, round(nombre, 2), sep="")
# Formatage avec fstring (format string)
print(f"La citation:\t{ma_string} est de {auteur}{nombre:.2f}")

