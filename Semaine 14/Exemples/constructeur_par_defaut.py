# En python, si on ne définit pas de constructeur à une classe, il en existe un par défaut

class MaClasse:
    pass

# C'est l'équivalent de
# class MaClasse:
#     def __init__(self):
#         super().__init__()

mc1 = MaClasse()
