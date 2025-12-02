# On échappe les caractères pour pouvoir les afficher si autrement impossible
print("Marie a dit: \"bonjour!\" ")
print('Marie dit: \'bonjour!\'')

print("tab:\ttab")
# pour le \ dans un str, on doit l'échapper
print("le caractère \\")

print("nouvelle ligne\n")

print("dsafsadf a sfdsa f a sdf dsaf  sad fds   ffsad f f f sa f  f sad f fdsfasdf sa fsad fdsa fa sf fsad fas dfssas "
      "fsa fa sdf  af ")

# Pour utiliser les caractères unicode utf-9, on utilise \u pour les valeurs jusqu'à quatre positions \U pour ceux à plus
print(f"pi \u03c0")
# Pour le \U, on complète pour avoir 8 positions hexadécimales (précède de zéros)
print(f"pêche \U0001f351")
print(f"pi \U000003c0")


