# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 21:57:35 2020

@author:
"""


# Appel des fonctions avec moins de paramètres
def f(arg1, arg2="Bonjour", arg3=233, arg4=True, arg5=-0.25):
    print(arg1, arg2, arg3, arg4, arg5)


f(1, 2, 3, 4, 5)  # 1 2 3 4 5
f(1, 2, 3, 4)  # 1 2 3 4 -0.25
f(1, 2, 3)  # 1 2 3 True -0.25
f(1, 2)  # 1 2 233 True -0.25
f(1)  # 1 Bonjour 233 True -0.25
# f()           # erreur: f() missing 1 required positional argument: 'arg1'
