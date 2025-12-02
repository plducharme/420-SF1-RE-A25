# Classe Personne
class Personne:
    # Constructeur tous les objets personnes habitent LAVAL
    # propritétés: nom, prenom, age, adresse
    def __init__(self, nom, prenom, age, taille):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.taille = taille
        self.adresse = "LAVAL"

    # Surcharge princpe de OO
    # Méthodes
    def veillir(self, arg1=2, arg2=3, arg3="Montréal"):  # le principe de surcharge de OO
        self.age += arg1
        if self.age < 18:
            self.taille += arg2
            self.adresse = arg3

    def info(self):
        print("Prenom=" + self.prenom + " Nom=" + self.nom + " Age=" + str(self.age) + " Taille=" + str(
            self.taille) + " Adresse=" + self.adresse)


# Ex d’utilisation: on crée deux objets de type personnes
p1 = Personne("Mireille", "Gagné", 3, 1.2)
p2 = Personne("Salim", "Rajhi", 9, 1.85)
# On appelle des méthodes sur ces objets
p1.veillir()  # surcharge de la méthode veillir
p1.info()  #
p1.veillir(4, 5)  # surcharge de la méthode veillir
p1.info()
p1.veillir(3, 6, "ottawa")  # surcharge de la méthode veillir
p1.info()

##objet p2
#p2.veillir()
#p2.info()  #
