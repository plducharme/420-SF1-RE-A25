
def fonction_kwargs(**kwargs):

    for k, v in kwargs.items():
        print(f"Clé:\t{k}\tValeur:\t{v} et son type:{type(v)}")


fonction_kwargs(a=3, b=5)

fonction_kwargs(nom="Pier Luc", age=21, couleur_yeux="bleu", taille=1.83)


