print("Gib einen beliebigen Satz ein")

satz = input()

upper = satz.upper()
lower = satz.lower()
laenge = len(satz) 

print(f"Dein Satz in Großbuchstaben: {upper}")
print(f"Dein Satz in Kleinbuchstaben: {lower}")
print(f"Die Länge deines Satzes beträgt {laenge} Zeichen.")