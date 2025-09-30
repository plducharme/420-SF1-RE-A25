import math


def hypothenuse(oppose: float, adjacent: float) -> float:
    return math.sqrt(carre(oppose) + carre(adjacent))


def distance(x1, y1, x2, y2):
    return hypothenuse(x2-x1, y2-y1)


def carre(x):
    return x**2


def perimetre(x1, y1, x2, y2, x3, y3):
    return distance(x1, y1, x2, y2) + distance(x2, y2, x3, y3) + distance(x3, y3, x1, y1)


print(perimetre(0, 0, 4, 0, 4, 3))
