import random

nombre = random.uniform(1.0, 100.0)
print(f"Nombre généré {nombre}")

print(f"arrondissement à 2 décimales: {round(nombre, 2)}")

# Garde les 2 décimales
print(f"arrondissement à 2 décimales: {nombre:.2f}")



