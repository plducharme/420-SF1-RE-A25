
def renverse_chaine(chaine: str):
    chaine_inversee = ""
    for s in chaine:
        chaine_inversee = s + chaine_inversee
    return chaine_inversee


if __name__ == "__main__":
    print(renverse_chaine("Allo les amis!"))
