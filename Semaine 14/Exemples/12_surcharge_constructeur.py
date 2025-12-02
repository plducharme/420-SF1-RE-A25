# -*- coding: utf-8 -*-
"""
Created on 2020

@author:
"""


# Classe Personne
class Personne:
    # Constructeur tous les objets personnes habitent LAVAL
    # propritétés: nom, prenom, age, adresse
    # principe de surcharge de constructeur
    def __init__(self, arg1="Rezgui", arg2="Jihene", arg3=30, arg4=1.8):
        self.nom = arg1
        self.prenom = arg2
        self.age = arg3
        self.taille = arg4
        self.adresse = "LAVAL"

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
p1 = Personne("Gagné", "Mireille", 3, 1.2)
p2 = Personne("Rajhi", "Salim", 9, 1.85)
p3 = Personne()
p4 = Personne(arg2="Sarah", arg4=1.63)  # appel des aruments pas dans l'ordre
p5 = Personne("Rezgui", "Maya")
# On appelle des méthodes sur ces objets
p1.veillir()
p1.info()  #
p1.veillir(4, 5)  # surcharge de la méthode veillir
p1.info()
p1.veillir(3, 6, "ottawa")
p1.info()
p3.info()
p4.info()
p5.info()
# objet p2
p2.veillir()
p2.info()  #
