class Animal:

    def __init__(self, espece: str, nb_de_pattes, pays_origine: str):
        self.espece = espece
        self.nb_pattes = nb_de_pattes
        self.pays_origine = pays_origine

    def parler(self):
        print(self.espece + " parle")


# Une classe peut hériter d'une autre classe, elle hérite de ses propriétés et ses méthodes
class Poule(Animal):
    def __init__(self, pays_origine, moy_oeufs_heure):
        super().__init__("poule", 2, pays_origine)
        self.moyenne_oeufs_heure = moy_oeufs_heure


class Vache(Animal):

    def __init__(self, pays_origine, nb_litres_lait):
        super().__init__("vache", 4, pays_origine)
        self.nb_litres = nb_litres_lait

    def parler(self):
        print("Meeeeeeeeeeeuuuuuuuh!")


poule = Poule("France", 3)
poule.parler()

vache = Vache("Hollande", 4)
vache.parler()
