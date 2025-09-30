def calcul_commission(ventes: float, taux: float) -> float:
    commission = ventes * taux
    print(f"commission: {commission} ventes: {ventes} taux: {taux}")
    return commission


print("la commission reçue est de", calcul_commission(2500, 0.10))
