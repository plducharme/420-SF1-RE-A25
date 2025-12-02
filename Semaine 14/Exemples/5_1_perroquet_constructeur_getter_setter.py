# Classe Perroquet
class Perroquet:
    # Constructeur
    def __init__(self, nom, age_en_annees):
        self.nom = nom
        self.age = age_en_annees
        self.altitude = 0

    def repete(self, phrase):
        print(self.nom + " dit: " + phrase)

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def affiche(self):
        print("nom= " + self.nom + " age= " + str(self.age))


# programme principal
perroquet1 = Perroquet("Coco", 3)
# print(perroquet1.nom)       # Coco
print(perroquet1.get_nom())  # la bonne maniere qui respecte l'encapsulation : principe de OO
perroquet1.set_nom("Jaco")
print(perroquet1.get_nom())
perroquet1.affiche()
perroquet1.repete('"Bonjour les pirates!"')  # Coco dit: "Bonjour les pirates!"
