# -*- coding: utf-8 -*-
"""
Created on 2020

@author:
"""


# Classe Personne
class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.adresse = "LAVAL"

    # Méthodes
    def veillir(self):
        self.age += 1

    def info(self):
        print("Prenom=" + self.prenom + " Nom=" + self.nom + " Age=" + str(self.age) + " Adresse=" + self.adresse)

    def toString(self):
        return ("Prenom: " + self.prenom + " Nom: " + self.nom + " Age: " + str(self.age) + " Adresse: " + self.adresse)


# Ex d’utilisation: on crée deux objets de type personnes
les_personnes = list()
# afficher les personnes dans une boucle
l = int(input("nombre de personnes dans la liste : \n"))
for i in range(l):
    prenom = input(" personne " + str(i) + " votre prenom\n: ")
    nom = input("votre nom\n: ")
    age = input("votre age\n: ")
    les_personnes.append(Personne(prenom, nom, age))
    print(les_personnes[i].toString())
