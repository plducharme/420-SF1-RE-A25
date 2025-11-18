joueur_cfm = {"Samuel Piette", "Prince Owosu", "Viktor Loturi", "Jonathan Sirois"}
joueur_cmnt = {"Stephen Eustaquio", "Alfonso Davies", "Jonathan Sirois", "Tajon Buccannan"}

print(f"Joueur du CFM qui sont dans CMNT {joueur_cfm.intersection(joueur_cmnt)}")

print(f"Liste de tous les joueurs dans CFM ou CMNT {joueur_cfm.union(joueur_cmnt)}")

print(f"Joueur de CMNT sans ceux du CFM {joueur_cmnt.difference(joueur_cfm)}")

print(f"Joueur de CFM ou CMNT qui ne sont pas communs aux deux (xor) {joueur_cfm ^ joueur_cmnt}")
