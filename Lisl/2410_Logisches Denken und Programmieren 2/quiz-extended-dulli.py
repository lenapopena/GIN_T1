points = 0
hints = 2

# Frage 1
print("Frage 1: Was ist die Hauptstadt von Deutschland?")
print("A. Berlin")
print("B. Hamburg")
print("C. Köln")
print("D. München")

# Frage 1 - Hints
if hints > 0:
    print("Willst du einen Tipp?")
    print("Ja")
    print("Nein")

    getHint = input()

    if getHint.upper() == "JA":
        hints = hints - 1
        print("Reimt sich auf Merlin")


# Frage 1 - Antwort
print("Bitte gib deine Antwort ein")
antwort1 = input()

if antwort1.upper() == "A":
    print("Das ist richtig!")
    points = points + 10

if antwort1.upper() != "A":
    print("Das ist falsch.")


# Frage 2
print("Frage 2: Was ist die Hauptstadt von Österreich?")
print("A. St. Pölten")
print("B. Wien")
print("C. Bregenz")
print("D. Linz")

# Frage 2 - Hints
if hints > 0:
    print("Willst du einen Tipp?")
    print("Ja")
    print("Nein")

    getHint = input()

    if getHint.upper() == "JA":
        hints = hints - 1
        print("Beginnt mit W")


# Frage 2 - Antwort
print("Bitte gib deine Antwort ein")
antwort2 = input()

if antwort2.upper() == "B":
    print("Das ist richtig!")
    points = points + 10

if antwort2.upper() != "B":
    print("Das ist falsch.")


# Frage 3
print("Frage 3: Was ist die Hauptstadt der Schweiz?")
print("A. Luzern")
print("B. Bern")
print("C. Zürich")
print("D. St. Gallen")

# Frage 3 - Hints
if hints > 0:
    print("Willst du einen Tipp?")
    print("Ja")
    print("Nein")

    getHint = input()

    if getHint.upper() == "JA":
        hints = hints - 1
        print("Erinnert an Bär")

# Frage 3 - Antwort
print("Bitte gib deine Antwort ein")
antwort3 = input()

if antwort3.upper() == "B":
    print("Das ist richtig!")
    points = points + 10

if antwort3.upper() != "B":
    print("Das ist falsch.")


# Ergebnis
print("Deine Punkte: " + str(points))
print("Deine verbleibenden Hints: " + str(hints))