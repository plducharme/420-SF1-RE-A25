import ex17

# afficher contenu ex17
print(dir(ex17))
print(help(ex17))

nom_produit = input("Donnez le nom du produit acheté: ")
quantite = int(input("Quantité: "))
prix = float(input("Prix: "))

total_hors_taxe = quantite * prix

montant_tps = ex17.calcul_tps(total_hors_taxe)
montant_tvq = ex17.calcul_tvq(total_hors_taxe)

total_avec_taxes = ex17.calcul_taxes(total_hors_taxe)

print(f"Produit: {nom_produit} Qte: {quantite} Prix Unitaire: {prix}")
print(f"TPS: {montant_tps} TVQ: {montant_tvq} Total: {total_avec_taxes}")





