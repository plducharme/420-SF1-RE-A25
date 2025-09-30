import math, random

# random.seed() avec une valeur, permet de générer les mêmes nombres aléatoires à chaque exécution
random.seed(42)
nombre = random.random()

print("Nombre:", nombre)
log_nombre = math.log(nombre)
puissance = math.pow(log_nombre, 3.0)

print("le log du nombre", log_nombre)
print("le cube de", log_nombre, "est", puissance)


