# Frage nach der Eingabe-Einheit
print("In welcher Einheit findet deine Eingabe statt?")
print("K. Kelvin")
print("C. Grad Celsius")
print("F. Grad Fahrenheit")

eingabe = input()


# Temperatur-Eingabe
print("Gib nun die Temperatur an")
temperatur = float(input())


# Frage nach der Umwandlungs-Einheit
print("In welche Einheit soll umgewandelt werden?")
print("K. Kelvin")
print("C. Grad Celsius")
print("F. Grad Fahrenheit")

konvertierung = input()


# Eingabe in Kelvin
if (eingabe.upper() == "K" and konvertierung.upper() == "C"):
    print(temperatur - 273.15)

if (eingabe.upper() == "K" and konvertierung.upper() == "F"):
    print(((temperatur - 273.15) * 1.8) + 32)



#Eingabe in Grad Celsius
if (eingabe.upper() == "C" and konvertierung.upper() == "K"):
    print(temperatur + 273.15)

if (eingabe.upper() == "C" and konvertierung.upper() == "F"):
    print(temperatur * 1.8 + 32)



# Eingabe in Fahrenheit
if (eingabe.upper() == "F" and konvertierung.upper() == "C"):
    print((temperatur - 32) / 1.8)

if (eingabe.upper() == "F" and konvertierung.upper() == "K"):
    print(((temperatur - 32) / 1.8) + 273.15)

