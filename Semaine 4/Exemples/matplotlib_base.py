import matplotlib.pyplot as plt


coord_x = [1, 2, 3, 4]
coord_y = [1, 2, 3, 4]

plt.plot(coord_x, coord_y, marker="h", color="blue", linestyle="--")
plt.title("Ma première droite!")
plt.xlabel("Axe des x")
plt.ylabel("Axe des y")
plt.legend(["x = y"])
plt.show()


