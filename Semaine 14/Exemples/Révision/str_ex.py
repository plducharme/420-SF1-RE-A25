ma_str = "bonjour"

# Les méthodes sur les str ne modifient pas la str, elles retournent une nouvelle str
ma_str.replace("o", "i")
# ma_str n'a pas été modifiée
print(ma_str)
nouvelle_str = ma_str.replace("o", "i")
print(nouvelle_str)

