import math


def pythagore(a: float, b: float) -> float:
    return math.sqrt(a**2 + b**2)


hypothenuse = pythagore(3.0, 4.0)
print(hypothenuse)

print(pythagore(2.3, 4.5))

# Faire attention au type retourné
# ex: .append() retourne None
liste1 = [1, 2, 3]
# liste2 sera à None
liste2 = liste1.append(4)
print(liste2)
