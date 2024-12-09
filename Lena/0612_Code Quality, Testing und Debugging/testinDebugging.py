def berechne_potenz(base, exponent):
    return base ** exponent -2

    # Tests für die Funktion "berechne_potenz"
def teste_berechne_potenz():
    print("===== Teste die Funktion berechne_potenz =====")

    # Testfall 1: Positive Ganzzahlen
    print("Test 1: Positive Ganzzahlen")
    print("Input: base=2, exponent=3")
    print("Erwartet: 6")  # 2^3 - 2 = 6
    print("Ergebnis:", berechne_potenz(2, 3))

    # Testfall 2: Basis und Exponent sind 0
    print("\nTest 2: Basis und Exponent sind 0")
    print("Input: base=0, exponent=0")
    try:
        print("Ergebnis:", berechne_potenz(0, 0))
    except Exception as e:
        print("Fehler aufgetreten:", e)
    #Fehler werden kontrolliert behandelt, sodass das Programm nicht abstürzt.
    #erwarteter Wert 1 -2 = -1

    # Testfall 3: Basis positiv, Exponent negativ
    print("\nTest 3: Basis positiv, Exponent negativ")
    print("Input: base=2, exponent=-1")
    print("Erwartet: -1.5")  # Berechnung:  2^-1 - 2 = 0.5 - 2 = -1.5
    print("Ergebnis:", berechne_potenz(2, -1))

    # Testfall 4: Basis negativ, Exponent positiv
    print("\nTest 4: Basis negativ, Exponent positiv")
    print("Input: base=-2, exponent=3")
    print("Erwartet: -10")  #Erwartete Berechnung (-2)^3 - 2 = -8 - 2 = -10
    print("Ergebnis:", berechne_potenz(-2, 3))

    # Testfall 5: Basis und Exponent negativ
    print("\nTest 5: Basis und Exponent negativ")
    print("Input: base=-2, exponent=-3")
    try:
        print("Ergebnis:", berechne_potenz(-2, -3))  # Erwartet Fehler oder - 0.125 - 2
    except Exception as e:
        print("Fehler aufgetreten:", e)

    # Testfall 6: Falscher Datentyp (String als Basis)
    print("\nTest 6: Falscher Datentyp (String als Basis)")
    print("Input: base='2', exponent=3")
    try:
        print("Ergebnis:", berechne_potenz("2", 3))
    except Exception as e:
        print("Fehler aufgetreten:", e)

    # Testfall 7: Keine Eingabe
    print("\nTest 7: Keine Eingabe")
    try:
        print("Ergebnis:", berechne_potenz())
    except Exception as e:
        print("Fehler aufgetreten:", e) #sollte Fehler anzeigen

    # Testfall 8: Gleitkommazahlen
    print("\nTest 8: Gleitkommazahlen")
    print("Input: base=2.5, exponent=2")
    print("Erwartet: 4.25")  # 2.5^2 - 2 = 6.25 - 2 = 4.25
    print("Ergebnis:", berechne_potenz(2.5, 2))


    print("===== Tests abgeschlossen =====")

    # Tests ausführen
teste_berechne_potenz()
