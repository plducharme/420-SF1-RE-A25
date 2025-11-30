# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 21:12:40 2020

@author:
"""


# Classe Perroquet
class Perroquet:
    # Constructeur
    def __init__(self, nom, age_en_annees):
        self.nom = nom
        self.age = age_en_annees
        self.altitude = 0

    # Méthodes
    def repete(self, phrase):
        print( self.nom + " dit: " + phrase )
    
    def envoleToi(self,altitude):
        self.altitude = altitude


# Ex d’utilisation: on crée deux objets de type Perroquet
mon_perroquet = Perroquet("Coco",3)
jaco = Perroquet("Jaco",0)

# On appelle des méthodes sur ces objets

mon_perroquet.envoleToi(20)
jaco.repete("Coco s’envole!")  # Jaco dit: Coco s’envole!





