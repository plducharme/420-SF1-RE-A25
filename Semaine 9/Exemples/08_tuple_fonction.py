# Pour l'explication complète, voir tuple_extras.py

def somme_et_produit(x, y):
    return (x + y), (x * y)


tup = somme_et_produit(2, 3)
print(tup)
somme, produit = somme_et_produit(5, 10)
print(somme, produit)




