import exercice_2_utils


def saisie():
    mot = input("Entrez le mot à composer: ")
    sequence = input("Entrez la séquence de lettre:")
    return mot, sequence


def verifier_mot_composable(mot: str, sequence: str):
    if sequence.find(mot) >= 0 or exercice_2_utils.renverse_chaine(sequence).find(mot) >= 0:
        print(f"Le mot '{mot}' est composable à partir de la séquence '{sequence}'")
    else:
        print(f"Le mot '{mot}' n'est pas composable à partir de la séquence '{sequence}'")


mot_composable, sequence_a_verifier = saisie()
verifier_mot_composable(mot_composable, sequence_a_verifier)
