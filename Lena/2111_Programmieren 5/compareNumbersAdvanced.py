def maximum(zahl1, zahl2):                                          #funktion und 2 eingabewertvariablen definieren
    print("bitte gib 2 zahlen ein, die du vergleichen möchtest")    #ausgeben, dass der nutzer zwei zahlen eingeben soll
    zahl1 = float(input())                                          #eingabe zahl1 als float um kommazahlen auch zu testen
    zahl2 = float(input())                                          #eingabe zahl2 als float um kommazahlen auch zu testen

    if zahl1 > zahl2:                                               #überprüfen, ob zahl1 größer ist und 
        return zahl1                                                #wenn ja, die zahl1 returnen (in die variable groessere_zahl)  
    
    else:                                                           #sonst...
        return zahl2                                                #...zahl2 returnen (in die variable groessere_zahl)

groessere_zahl = maximum(4, 5)                                      #variable definieren für die ausgabe des funktionsergebnisses
print("die größere zahl lautet " + str(groessere_zahl))             #variable aka ergebnis ausgeben 