# -*- coding: utf-8 -*-
"""
Created on 2020

@author:
"""


# Classe Personne
class Personne:
    # Constructeur tous les objets personnes habitent LAVAL
    # propritétés: nom, prenom, age, adresse
    def __init__(self, nom, prenom, age, taille):
        self.nom = nom
        self.prenom = prenom
        self.age=age
        self.taille=taille
        self.adresse = "LAVAL"

    # Méthodes
    def veillir(self):
        self.age+=1
        if self.age <18:
            self.taille +=0.02

    def veillir(self ):  # le principe de surcharge de OO
        self.age += 1
        if self.age < 18:
            self.taille += 0.02

    def info(self):
        print("Prenom=" + self.prenom + " Nom=" + self.nom + " Age=" + str(self.age) + " Taille=" + str(
            self.taille) + " Adresse=" + self.adresse)


# Ex d’utilisation: on crée deux objets de type personnes
p1 = Personne("Mireille", "Gagné", 3, 1.2)
p2 = Personne("Salim", "Rajhi", 9, 1.85)
# p3= Personne("Sarah", "Rajhi")
# On appelle des méthodes sur ces objets
p1.veillir()
p1.info()  #

# objet p2
p2.veillir()
p2.info()  #
