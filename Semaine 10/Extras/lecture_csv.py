import csv

liste_site_no = []
with open("Water-Qual-Eau-Sites-National.csv", mode="r") as fichier_csv:
    data = csv.reader(fichier_csv, delimiter=",")

    for i, ligne in enumerate(data):
        if i == 0:
            continue
        liste_site_no.append(ligne[0])

print(liste_site_no)

with open("nos_sites.txt", mode="w") as fichier_txt:

    for no in liste_site_no:
        fichier_txt.write(no + "\n")




