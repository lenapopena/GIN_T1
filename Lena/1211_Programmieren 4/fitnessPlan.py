
trainingsart = input("Welche Trainingsart möchten Sie ausüben? (Kraft oder Ausdauer): ").strip().lower()
alter = int(input("Wie alt sind Sie? (Bitte in Jahren angeben): "))
fitnesslevel = input("Wie würden Sie Ihr Fitnesslevel einschätzen? (Anfänger, Fortgeschritten, Profi): ").strip().lower()


if alter <= 18:
    
    if fitnesslevel == "anfänger":
        programm = "Leichte Gymnastik und Joggen"
    elif fitnesslevel == "fortgeschritten":
        programm = "Gymnastik, Joggen und Kraftübungen."
    else:
        programm = "Joggen  und  Kraftübungen."


elif 19 <= alter <= 40:
    
    if trainingsart == "kraft":
        if fitnesslevel == "anfänger":
            programm = "Leichtes Krafttraining."
        elif fitnesslevel == "fortgeschritten":
            programm = "Mittelschweres Krafttraining."
        else:
            programm = "Intensives Krafttraining."
    elif trainingsart == "ausdauer":
        if fitnesslevel == "anfänger":
            programm = "Leichtes Ausdauertraining."
        elif fitnesslevel == "fortgeschritten":
            programm = "Mittelschweres Ausdauertraining."
        else:
            programm = "Intensives Ausdauertraining."
    else:
        programm = "Ungültige Eingabe der Trainingsart."

else:
    
    if fitnesslevel == "anfänger":
        programm = "Gelenkschonende Übungen wie Yoga und Schwimmen, 30 Minuten ."
    elif fitnesslevel == "fortgeschritten":
        programm = "Moderates Gewichtstraining, Yoga und Schwimmen, 45 Minuten."
    else:
        programm = "Yoga, moderates Gewichtstraining und Schwimmen, 60 Minuten."


print(f"Ihr vorgeschlagenes Trainingsprogramm lautet: {programm}")