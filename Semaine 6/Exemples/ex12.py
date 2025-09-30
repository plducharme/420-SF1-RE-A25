# Si on importe de cette façon, on doit utiliser le nom du module comme préfix
import math

print(dir(math))

nombre = 121
angle = math.pi / 6

print("Racine carré", math.sqrt(nombre))
print("Sinus", math.sin(angle))
