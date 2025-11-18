# https://pokeapi.co/api/v2/pokemon/{id}/
import requests

numero_pokemon = input("Numéro de pokemon à consulter: ")

donnees_pokemon = requests.get("https://pokeapi.co/api/v2/pokemon/" + numero_pokemon + "/").json()

print(donnees_pokemon)
print(donnees_pokemon["name"])

liste_habiletes = donnees_pokemon["abilities"]

for hab in liste_habiletes:
    print(hab["ability"]["name"])





