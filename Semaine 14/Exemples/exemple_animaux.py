class Animal:

    def __init__(self, espece: str, nb_de_pattes, pays_origine: str):
        self.espece = espece
        self.nb_pattes = nb_de_pattes
        self.pays_origine = pays_origine

    def parler(self):
        print(self.espece + " parle")


vache = Animal("vache", 4, "Hollande")
vache.parler()

poule = Animal("poule", 2, "France")
poule.parler()

