tps = 0.05
tvq = 0.09975


def calcul_tps(montant):
    return montant * tps


def calcul_tvq(montant):
    return montant * tvq


def calcul_taxes(montant):
    return montant + calcul_tps(montant) + calcul_tvq(montant)


def reverse_taxe(montant_avec_taxe):
    return montant_avec_taxe / 1.149175






