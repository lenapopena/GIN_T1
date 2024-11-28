#leeres set mit normalen klammern statt geschwungenen erstellen:
lieblingsfilme = set()

#leere kontrollvariable hinzufügen
film = ""

print("Bitte gib deine Lieblingsfilme ein oder beende mit 'stop':")

#endloslange schleife die eingabe erlaubt, solange die eingabe nicht stop ist
while film != "stop":
    film = input()

    if film != "stop":
        #überprüfen, ob die eingabe schon einmal vorkommt, falls ja -> löschen
        if film in lieblingsfilme:
            lieblingsfilme.remove(film)
            print(f"{film} kommt bereits vor und wurde deshalb entfernt")
        #falls nein -> hinzufügen
        else:
            lieblingsfilme.add(film)
            print(f"{film} wurde hinzugefügt")

print("deine lieblingsfilme sind: ")
for film in lieblingsfilme:
    print(lieblingsfilme)