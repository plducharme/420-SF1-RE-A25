# Classe Personne
class Personne:
    # Constructeur tous les objets personnes habitent LAVAL
    # propriétés : nom, prenom, age, adresse
    def __init__(self, nom: str, prenom: str, age: int, taille: float):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.taille = taille
        # valeur par défaut, non passée en paramètre
        self.adresse = "LAVAL"

    # Méthodes
    def vieillir(self):
        self.age += 1
        if self.age < 18:
            self.taille += 0.02

    # def veillir(self):  # le principe de surcharge de OO
    #     self.age += 1
    #     if self.age < 18:
    #         self.taille += 0.02

    def info(self):
        print("Prenom=" + self.prenom + " Nom=" + self.nom + " Age=" + str(self.age) + " Taille=" + str(
            self.taille) + " Adresse=" + self.adresse)


# Ex d’utilisation: on crée deux objets de type personnes
mireille = Personne("Mireille", "Gagné", 3, 1.2)
salim = Personne("Salim", "Rajhi", 9, 1.85)
# p3= Personne("Sarah", "Rajhi")
# On appelle des méthodes sur ces objets
mireille.vieillir()
mireille.info()  #

# objet p2
salim.vieillir()
salim.info()  #
