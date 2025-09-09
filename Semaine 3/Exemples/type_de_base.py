# Les types de base
# String
# Déclaration
ma_string = "Ceci est ma chaîne de caractères"
mon_autre_string = 'Ceci est ma chaîne de caractères'

str_3 = "L'appel de la nature"
str_4 = 'Léa a dit: "Bonjour!"'

# Caractères d'échappement
str_5 = 'L\'appel'
str_6 = "Léa a dit: \"Bonjour!\""
str_multilignes = "Première ligne\nDeuxième ligne"
print(str_multilignes)
str_tab = "Prénom:\tPier Luc\tNom:\tDucharme"
print(str_tab)
caracteres_multilignes = "Ceci est une chaîne de \
continuation de la chaîne"
print(caracteres_multilignes)
char_multi_autre_facon = ("Ceci est une chaîne de "
                          "continuation de la chaîne")
print(char_multi_autre_facon)
# Pour échapper (et afficher) le caractère d'échappement "\", on utilise "\\"
char_echap = "Ceci est un backslash:\\"
print(char_echap)

# Unicode et UTF-8
print("\u03c0 est un nombre irrationnel")
print("\u2654 \u2655 \u2656 \u265e")
print("Bélier: \u2648")






