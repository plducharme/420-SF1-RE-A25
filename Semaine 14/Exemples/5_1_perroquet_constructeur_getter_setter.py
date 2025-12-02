# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 19:11:41 2020

@author:
"""


# Classe Perroquet
class Perroquet:
    # Constructeur
    def __init__(self, nom, age_en_annees):
        self.nom = nom
        self.age = age_en_annees
        self.altitude = 0

    def repete(self, phrase):
        print(self.nom + " dit: " + phrase)

    def getNom(self):
        return (self.nom)

    def setNom(self):
        self.nom = "JACO"

    def affiche(self):
        print("nom= " + self.nom + " age= " + str(self.age))


# programme principal
perroquet1 = Perroquet("Coco", 3)
# print(perroquet1.nom)       # Coco
print(perroquet1.getNom());  # la bonne maniere qui respecte l'encapsulation : principe de OO
perroquet1.setNom();
print(perroquet1.getNom());
perroquet1.affiche()
perroquet1.repete('"Bonjour les pirates!"')  # Coco dit: "Bonjour les pirates!"
