print("Gib ein Satz und danach ein Wort ein, das Programm überprüft ob das Wort in diesem Satz vorkommt.")

satz = input()
wort = input()

if wort in satz:
    print(f"Das Wort {wort} ist im Satz enthalten.")

else:
    print(f"das Wort {wort} ist nicht im Satz enthalten")