# Globals
points = 0
hintCount = 2

# Funktion 1: Frage stellen, Antwort einlesen und Antwort prüfen
def ask_question(question, options, correct_answer, hint_letter):
    global hintCount  # Zugriff auf globale Variable
    print(question)
    for option in options:
        print(option)
    print("---------------------------------")
    # Zeilenumbruch und die Trennungslinie
    
    if hintCount > 0:
        getHint = input("Need a hint? [y], [n]: ")
        if getHint.upper() == "Y":
            hintCount -= 1
            print(f"Hint: Capital starts with letter '{hint_letter}'")

    answer = input("Your answer: ")
    return answer.upper() == correct_answer.upper()

# Funktion 2: Punkte berechnen
def update_points(is_correct):
    global points  # Zugriff auf globale Variable
    if is_correct:
        points += 10
        print("Answer is correct!")
    else:
        print("Answer is incorrect!")
    print("---------------------------------\n")
    # Zeilenumbruch und die Trennungslinie

# Hauptprogramm
questions = [
    {"question": "What is the capital of Germany?", "options": ["(A) Berlin", "(B) Hamburg", "(C) Köln", "(D) München"], "answer": "A", "hint": "B"},
    {"question": "What is the capital of Austria?", "options": ["(A) Linz", "(B) Bregenz", "(C) Wien", "(D) Klagenfurt"], "answer": "C", "hint": "W"},
    {"question": "What is the capital of Spain?", "options": ["(A) Bilbao", "(B) Madrid", "(C) Valencia", "(D) Barcelona"], "answer": "B", "hint": "M"},
    {"question": "What is the capital of the Netherlands?", "options": ["(A) Maastricht", "(B) Rotterdam", "(C) Den Haag", "(D) Amsterdam"], "answer": "D", "hint": "A"},
    {"question": "What is the capital of the Czech Republic?", "options": ["(A) Prague", "(B) Krumau", "(C) Budweis", "(D) Brenn"], "answer": "A", "hint": "P"},
    {"question": "What is the capital of Italy?", "options": ["(A) Vatican", "(B) Rome", "(C) Brixen", "(D) Palermo"], "answer": "B", "hint": "R"},
    {"question": "What is the capital of Ireland?", "options": ["(A) Kirk", "(B) Galway", "(C) Dublin", "(D) Kilkenny"], "answer": "C", "hint": "D"},
    {"question": "What is the capital of France?", "options": ["(A) Marseille", "(B) Bordeaux", "(C) Lyon", "(D) Paris"], "answer": "D", "hint": "P"},
]

for q in questions:
    is_correct = ask_question(q["question"], q["options"], q["answer"], q["hint"])
    update_points(is_correct)

# Endausgabe
print("Your score: " + str(points))
print("Hints left: " + str(hintCount))
