# Funktion zum Zählen der Wörter in einem Satz
def zähle_wörter_im_satz(satz):
    
# Zählt die Anzahl der Wörter in einem gegebenen Satz
    return len(satz.split())

# Funktion zum Verarbeiten einer Liste von Sätzen
def zähle_wörter(sätze):
# Zählt und gibt die Anzahl der Wörter in jeder Zeile aus
    for satz in sätze:  # Hier 'sätze' korrekt verwenden
        anzahl_wörter = zähle_wörter_im_satz(satz)
        print(f"Der Satz '{satz}' hat {anzahl_wörter} Wörter.")

# Liste von Sätzen
sätze = ["Das ist ein Satz.", "Noch ein Satz.", "Python ist toll."]

# Aufruf der Funktion mit der Liste von Sätzen
zähle_wörter(sätze)
