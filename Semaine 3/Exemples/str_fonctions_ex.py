citation = ("La plus grande gloire de la vie ne réside pas dans la chute, mais dans le fait de se relever chaque fois"
            " que l'on tombe.")

citation_2 = 'Walt Disney a dir: "La façon de commencer est d\'arrêter de parler et de commencer à faire."'

citation_3 = """Votre temps est limité, alors ne le gaspillez pas en vivant les échecs de la vie de quelqu'un d'autre.
Ne vous laissez pas piéger par le dogme 
qui consiste à vivre avec les résultats de la pensée des autres. 
"""
print(citation)
# print(citation_2)
# print(citation_3)

for mot in citation.split(" "):
    print(mot.capitalize())

