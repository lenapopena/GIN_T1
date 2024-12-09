#Aufgabe 4. Testing und Debugging: Teste Code ausführlich 
#Alle Pfade, Grenzfälle, verschiedenster User-Input, negativ Werte, falscher Datentyp,keine Eingabe, usw.) und dokumentiert alle Tests.
#Fehler dokumentieren, Debug-Verfahren,Fixt die gefundenen Fehler im Code, verwendet den fehlgeschlagenen Test, um zu testen, ob der Fehler nun gelöst ist.



def mittelwert(liste):
    return sum(liste) // len(liste) #sum(liste) = Summe aller Elemente,  // = Operator für ganzzahlige Divison, len(liste) = Anzahl Elemente




print("Testing und Debugging")

# Test 1: Standardfall
test1 = [1, 2, 3, 4, 5]
print("Test 1 - Standardfall:", mittelwert(test1))  # Erwartetes Ergebnis: 3

# Test 2: Leere Liste
try:
    test2 = []
    print("Test 2 - Leere Liste:", mittelwert(test2))
except ZeroDivisionError as e:
    print("Fehler in Test 2 - Leere Liste:", e)

# Test 3: Negative Werte
test3 = [-10, -20, -30]
print("Test 3 - Negative Werte:", mittelwert(test3))  # Erwartetes ergebnis: -20

# Test 4: Falscher Datentyp (String in der Liste)
try:
    test4 = [10, "Wort", 30]
    print("Test 4 - Falscher Datentyp:", mittelwert(test4))
except TypeError as e:
    print("Fehler in Test 4 - Falscher Datentyp:", e)

# Test 5: Keine Eingabe
try:
    print("Test 5 - Keine Eingabe:", mittelwert())
except TypeError as e:
    print("Fehler in Test 5 - Keine Eingabe:", e)

# Test 6: Floats in der Liste
test6 = [1.5, 2.5, 3.5]
print("Test 6 - Floats in der Liste:", mittelwert(test6))  # Erwartetes Ergebnis: 2 (da Operator für ganzzahlige Zahlen genutzt wird)

# Debugging und Fixing:
print("Debugging und Fixing")

def mittelwert_flexibel(liste):
    if not isinstance(liste, list):
        raise TypeError("Eingabe muss eine Liste sein.")#raise= um Ausnahme (Exception) auszulösen. Eine Ausnahme ist eine spezielle Bedingung, dass ein Fehler im Programm aufgetreten ist
    if not liste:
        raise ValueError("Die Liste darf nicht leer sein.")
    if not all(isinstance(x, (int, float)) for x in liste):
        raise TypeError("Alle Elemente in der Liste müssen Zahlen sein.")
    return sum(liste) / len(liste)  # Änderung von // zu / für präzise Ergebnisse

# Erneute Tests mit gefixter Funktion
print("Wiederholte Tests mit mittelwert_flexibel")

# Test 1: Standardfall
print("Test 1 - Standardfall:", mittelwert_flexibel(test1))  # Erwartet: 3

# Test 2: Leere Liste
try:
    print("Test 2 - Leere Liste:", mittelwert_flexibel(test2))
except ValueError as e:
    print("Fehler in Test 2 - Leere Liste:", e)

# Test 3: Negative Werte
print("Test 3 - Negative Werte:", mittelwert_flexibel(test3))  # Erwartet: -20

# Test 4: Falscher Datentyp (String in der Liste)
try:
    print("Test 4 - Falscher Datentyp:", mittelwert_flexibel(test4))
except TypeError as e:
    print("Fehler in Test 4 - Falscher Datentyp:", e)

# Test 5: Keine Eingabe
try:
    print("Test 5 - Keine Eingabe:", mittelwert_flexibel())
except TypeError as e:
    print("Fehler in Test 5 - Keine Eingabe:", e)

# Test 6: Floats in der Liste
print("Test 6 - Floats in der Liste:", mittelwert_flexibel(test6))  # Erwartet: 2.5
