import sys


def moyenne(somme_notes, nombre_etudiants):
    assert nombre_etudiants != 0
    assert somme_notes >= 0, "La somme des notes doit être 0 ou positive"
    return somme_notes / nombre_etudiants


sys.tracebacklimit = 0
moyenne(250, 16)
moyenne(250, 0)


