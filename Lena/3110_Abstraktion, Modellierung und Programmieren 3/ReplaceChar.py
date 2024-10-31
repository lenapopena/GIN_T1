satz = input("Gib einen Satz ein: ")
buchstabe1 = input("Gib den ersten Buchstaben ein: ")
buchstabe2 = input("Gib den zweiten Buchstaben ein: ")

neuer_satz = satz.replace(buchstabe1, buchstabe2)

print(f"Der neue Satz lautet: {neuer_satz}")
