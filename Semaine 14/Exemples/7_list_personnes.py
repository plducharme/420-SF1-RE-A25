# Classe Personne
class Personne:
    # Constructeur tous les objets personnes habitent LAVAL
    # propriétés: nom, prenom, age, adresse
    def __init__(self, nom, prenom, age, taille):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.taille = taille
        self.adresse = "LAVAL"

    # Méthodes
    def veillir(self):
        self.age += 1

    def info(self):
        print("Prenom=" + self.prenom + " Nom=" + self.nom + " Age=" + str(self.age) + " Taille=" + str(
            self.taille) + " Adresse=" + self.adresse)

    def to_string(self):
        return "Prenom=" + self.prenom + " Nom=" + self.nom + " Age=" + str(self.age) + " Taille=" + str(
            self.taille) + " Adresse=" + self.adresse


# Ex d’utilisation: on crée deux objets de type personnes
les_personnes = list()
p1 = Personne("Salim", "Gagné", 10, 1.89)
les_personnes.append(Personne("Mireille", "Gagné", 3, 1.1))
les_personnes.append(p1)
# afficher les personnes dans une boucle
for i in range(len(les_personnes)):
    print(les_personnes[i])
