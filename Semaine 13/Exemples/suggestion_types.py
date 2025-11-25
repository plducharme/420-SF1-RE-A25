# On peut suggérer à l'IDE le type attendu

def ma_fonction(a: int, b: float) -> str:
    total = a + b
    return str(total)

# ceci va générer un avertissement
ma_fonction("adsfsadf", 1.0)

