
def livre(titre, *args):
    print(f"pour le livre {titre}, les auteurs sont:")

    for auteur in args:
        print(f"- {auteur}")


livre("Python en vrac", "Pier Luc")
livre("Super Python", "Pier Luc", "Mustapha", "Jean-Jacques")

