#Todo Applikation
#leere Liste erzeugen
todos = []

def add_todo():
    #Todo eingeben
    text = input("Geben Sie das neue Todo ein: ")
    #Listeneintrag erstellen
    todo = {'text': text, 'erledigt': False}
    #Speichert neuen Listeneintrag in die ganz oben erstellte Liste "todos"
    todos.append(todo) 
    print("Todo hinzugefügt!\n")

def show_todo():
    print("Offene Todos:")
    nummer = 1
    for todo in todos:
        #Listeneinträge prüfen ob "erledigt" Attribut auf False gesetzt ist
        if not todo['erledigt']:
            print(f"{nummer}. {todo['text']}")
        nummer += 1
    print()

def set_todo_done():
    show_todo()
    nummer = int(input("Geben Sie die Nummer des abzuschließenden Todos ein: "))
    #User Eingabe prüfen, ob diese innerhalb der Liste existiert
    if 1 <= nummer <= len(todos):
        #Prüfen ob das eingegebene Todo auch wirklich noch nicht abgeschlossen ist
        if not todos[nummer - 1]['erledigt']:
            #auf erledigt setzen
            todos[nummer - 1]['erledigt'] = True
            print("Todo abgeschlossen!\n")
        else:
            print("Dieses Todo ist bereits abgeschlossen.\n")
    else:
        print("Ungültige Nummer.\n")

def show_completed_todo():
    print("Abgeschlossene Todos:")
    nummer = 1
    for todo in todos:
        #gucken ob die Listeneinträge erledigt sind bzw. das Attribut auf True gesetzt ist
        if todo['erledigt']:
            #wenn ja dann ausgeben
            print(f"{nummer}. {todo['text']}")
        nummer += 1
    print()

def change_todo():
    show_todo()
    #todo zum ändern auswählen
    nummer = int(input("Geben Sie die Nummer des zu ändernden Todos ein: "))
    #gibt es diesen listeneintrag?
    if 1 <= nummer <= len(todos):
        #prüfen auf nicht abgeschlossene todos, abgeschlossene todos braucht man ja nicht mehr ändern
        if not todos[nummer - 1]['erledigt']:
            #eingabe neuer text
            neuer_text = input("Geben Sie den neuen Text ein: ")
            #hier überschreiben wir den alten text des ausgewählten todos
            todos[nummer - 1]['text'] = neuer_text
            print("Todo aktualisiert!\n")
        else:
            print("Dieses Todo ist bereits abgeschlossen und kann nicht geändert werden.\n")
    else:
        print("Ungültige Nummer.\n")

def menue_anzeigen():
    print("Bitte wählen Sie eine Option:")
    print("1. Neues Todo hinzufügen")
    print("2. Offene Todos anzeigen")
    print("3. Todo abschließen")
    print("4. Abgeschlossene Todos anzeigen")
    print("5. Text von offenem Todo ändern")
    print("6. Beenden")

def main():
    #main menu
    while True:
        menue_anzeigen()
        auswahl = input("Was möchtest du tun?: ")
        print()
        if auswahl == '1':
            add_todo()
        elif auswahl == '2':
            show_todo()
        elif auswahl == '3':
            set_todo_done()
        elif auswahl == '4':
            show_completed_todo()
        elif auswahl == '5':
            change_todo()
        elif auswahl == '6':
            print("Programm beendet.")
            break
        else:
            print("Diese Auwahl existiert leider nicht! :(.\n")

if __name__ == "__main__":
    main()
