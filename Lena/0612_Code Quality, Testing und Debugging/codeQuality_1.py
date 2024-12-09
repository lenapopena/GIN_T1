#Methode zur Prüfung, ob eine Zahl durch 3 teilbar ist
def checkNumber(numb: int):
    if numb % 3 == 0:
        print(numb)
        return True
    return False

#Angabe der Zahlenliste
inputList = [3, 5, 9, 12, 20, 33, 40, 45]
sum = 0

#Schleife zum Iterieren der Zahlen
for numb in inputList:
    checkNumber(numb)

#Ausgabe der Zahlenergebnisse
print("Summe:", sum)