def maximum(zahl1, zahl2):      #funktion und 2 eingabewertvariablen definieren
    if zahl1 > zahl2:           #überprüfen, ob zahl1 größer ist und
        return zahl1            #wenn ja, die zahl1 returnen (in die variable groessere_zahl) 
    
    else:                       #sonst...
        return zahl2            #...zahl2 returnen (in die variable groessere_zahl) 

groessere_zahl = maximum(4, 5)  #variable definieren für die ausgabe des funktionsergebnisses
print(groessere_zahl)           #variable aka ergebnis ausgeben