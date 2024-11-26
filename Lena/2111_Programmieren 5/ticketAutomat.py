def zeige_preise():
    print("Verfügbare Tickets:")
    print("1. Ticket A - 2.50€")
    print("2. Ticket B - 3.00€")
    print("3. Ticket C - 1.80€")

def berechne_restbetrag(preis, bezahlt):
     return preis - bezahlt
def fahrkartenautomat():
    print("Willkommen zum Fahrkartenautomat!")
    zeige_preise()

    # Ticket wählen
    ticket = int(input("Wählen Sie ein Ticket (1, 2 oder 3): "))
    if ticket == 1:
        preis = 2.50
    elif ticket == 2:
        preis = 3.00
    elif ticket == 3:
        preis = 1.80
    else:
        print("Ungültige Auswahl. Das Programm wird beendet.")
        return

    #  ticket Zahlen
    bezahlt = 0
    while bezahlt < preis:
        print(f"Es fehlen noch {berechne_restbetrag(preis, bezahlt):.2f}€.")
        einwurf = float(input("Bitte Münze einwerfen: "))
        bezahlt += einwurf
    print("Ticket bezahlt! Ihr Ticket wird gedruckt. Vielen Dank!")

fahrkartenautomat()
