def calcul_commission(ventes: float, taux: float) -> float:
    commission = ventes * taux
    print(f"commission: {commission} ventes: {ventes} taux: {taux}")
    return commission


# Attention, les variables suivantes sont dans la portée globale et sont différentes de celle de la fonction
n = 25
ventes = 3000
taux = 0.5
print("la commission reçue est de", calcul_commission(2500, 0.10))
print("affichage 2 =", n, "ventes=", ventes, "taux=", taux)