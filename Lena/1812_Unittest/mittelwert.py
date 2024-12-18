def mittelwert_flexibel(liste):
    if not isinstance(liste, list):
        raise TypeError("Eingabe muss eine Liste sein.")  # Eingabe muss eine Liste sein
    if not liste:
        raise ValueError("Die Liste darf nicht leer sein.")  # Die Liste darf nicht leer sein
    if not all(isinstance(x, (int, float)) for x in liste):
        raise TypeError("Alle Elemente in der Liste müssen Zahlen sein.")
    return sum(liste) / len(liste)  # Änderung von // zu / für präzise Ergebnisse
