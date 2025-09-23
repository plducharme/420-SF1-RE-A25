import math
# Arguments avec défaut, deviennent optionnels


def hypothenuse(a=3, b=4):
    print(f"c = {math.sqrt(a**2 + b**2)}")


hypothenuse(5)  # a=5, b=4
hypothenuse()  # a=3, b=4

hypothenuse(b=7)  # a=3, b=7



