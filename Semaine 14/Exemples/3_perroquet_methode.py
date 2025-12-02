# Classe Perroquet
class Perroquet:
    def repete(self, phrase):
        print(self.nom + " dit: " + phrase)

    def affiche(self):
        print("nom= " + self.nom + " age= " + str(self.age))


# programme principal
perroquet1 = Perroquet()
tomy = Perroquet()
perroquet1.nom = "Coco"
perroquet1.age = 3
perroquet1.altitude = 0

tomy.nom = "TT"
tomy.age = 2
tomy.altitude = 2
# print(perroquet1.nom)       # Coco
# print(perroquet1.age)       # 3
# print(perroquet1.altitude)  # 0
perroquet1.repete('"Bonjour les pirates!"')  # Coco dit: "Bonjour les pirates!"
# print (type(perroquet1))
perroquet1.affiche()
tomy.repete("hello world ")
tomy.affiche()
