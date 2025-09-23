nom = input("Veuillez entrer votre nom: ")

nom = nom.capitalize()
print(nom)
email = input("Entrez votre email: ")

position_arobas = email.find("@")
print("Position du arobas:", position_arobas)

if email.endswith(".ca"):
    print("se termine par .ca")

if email.startswith("plducharme"):
    print("Commence par plducharme")

print(email.startswith("plducharme"))





