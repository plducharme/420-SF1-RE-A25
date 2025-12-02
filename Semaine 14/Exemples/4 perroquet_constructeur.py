# Classe Perroquet
class Perroquet:

    # Constructeur
    def __init__(self, nom, age_en_annees):
        self.nom = nom
        self.age = age_en_annees
        self.altitude = 0

    def repete(self, phrase):
        print(self.nom + " dit: " + phrase)


# programme principal
perroquet1 = Perroquet("Coco", 3)
print(perroquet1.nom)       # Coco

print(perroquet1.age)       # 3
print(perroquet1.altitude)  # 0
perroquet1.repete('"Bonjour les pirates!"') # Coco dit: "Bonjour les pirates!"

print(perroquet1.nom, perroquet1.age)

jaco = Perroquet("Jaco", 4)
polly = Perroquet("Polly", 2)

print(jaco.nom)
print(polly.nom)
