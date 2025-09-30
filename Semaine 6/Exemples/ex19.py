# pseudo tests unitaires

def carre(x):
    return x ** 2


def test_carre():
    if carre(-3) != 9:
        print("Erreur dans la fonction carre()")
    if carre(0) != 0:
        print("Erreur dans la fonction carre()")


test_carre()
