# En python, une str est en fait une séquence dhe chr
ma_str = "Bonjour le monde!"

for caractere in ma_str:
    print(f"'{caractere}'", end="")

print("\n##########")
# str() est le constructeur de str
mon_int = 42
str_42 = str(mon_int)
print(str_42)

# chr() est le constructeur pour un caractère, son paramètre est la valeur numérique du caractère
caractere = chr(80)  # P
print(caractere)


