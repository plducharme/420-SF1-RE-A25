import matplotlib.pyplot as plt

mes_x = []
mes_y = []

for x in range(50):
    mes_x.append(x)
    mes_y.append(x**2)

# plot() permet d'ajouter des points à un graphique
plt.plot(mes_x, mes_y, linestyle="--", color="b", marker="*")
# xlabel(), ylabel() ajoutent des libellés aux axes
plt.xlabel("Valeurs en X")
plt.ylabel("Valeurs en Y")
# title() ajoute une titre
plt.title("Titre de mon graphique")

constante_x = [0, 49]
constante_y = [1000, 1000]
plt.plot(constante_x, constante_y, linestyle="-", color="g", marker="^")

# legend() ajoute une légende pour chaque série de courbes
plt.legend(["y = x**2", "y = 1000"])
plt.show()


# Listes en compréhension
barre_x = [x for x in range(50)]
barre_y = [x**3 for x in range(50)]
plt.bar(barre_x, barre_y, color="y")
plt.xlabel("x")
plt.ylabel("y")

plt.title("Les cubes")
plt.legend(["y = x**3"])

plt.show()






