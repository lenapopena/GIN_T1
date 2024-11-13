temperatur = float(input("Geben Sie die Temperatur in Celsius ein: "))

if temperatur < 0:
    print("Kalt")

elif 0 <= temperatur <= 20:
    print("Kühl")

elif 21 <= temperatur <= 30:
    print("Warm")

else:
    print("Heiß")