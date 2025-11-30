# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 21:38:31 2020

@author:
"""


# Passage d’un nombre arbitraire d’arguments
def f(*args):
    print(*args)


f(3, 5)  # affiche 3, 5
f(3)  # affiche 3
f(3, "Bonjour", 5, True, -0.25)  # affiche 3,Bonjour,5,true,-0.25
