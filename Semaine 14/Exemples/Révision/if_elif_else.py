# if
a = 42
b = 666

if a < b:
    print("plus petit")

if a < 10:
    print("C")
elif a < 100:
    print("D")
elif a > 2300:
    print("Z")
else:
    print("Aucune des conditions dans haut")

# on peut imbriquer les conditions
z = 123
if z > 100:
    if z < 150:
        print("Entre 101 et 149")
    else:
        print("150 et plus")
else:
    print("100 ou moins")
