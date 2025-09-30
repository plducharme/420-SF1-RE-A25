import math as m
import random as rnd

rnd.seed(42)
nombre = rnd.random()

log_nombre = m.log(nombre)
puissance = m.pow(log_nombre, 3.0)

print(log_nombre)
print(puissance)
