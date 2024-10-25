#globals
points = 0
hintCount = 2

#Question 1
print("What is the capital of Germany?\n")
print("(A) Berlin")
print("(B) Hamburg")
print("(C) Köln")
print("(D) München")
print("---------------------------------")

if hintCount > 0:
    getHint = input("Need a hint? [y], [n]: ")

    if getHint.capitalize() == "Y":
        hintCount -= 1
        print("Capital starts with letter 'R'")

answer = input("Your answer: ")

if answer.capitalize() == "A":
    print("Answer is correct!")
    points += 10
else:
    print("Answer is incorrect!")
print("---------------------------------\n")

#Question 2
print("What is the capital of Austria?\n")
print("(A) Linz")
print("(B) Bregenz")
print("(C) Wien")
print("(D) Klagenfurt")
print("---------------------------------")

if hintCount > 0:
    getHint = input("Need a hint? [y], [n]: ")

    if getHint.capitalize() == "Y":
        hintCount -= 1
        print("Capital starts with letter 'R'")

answer = input("Your answer: ")

if answer.capitalize() == "C":
    print("Answer is correct!")
    points += 10
else:
    print("Answer is incorrect!")
print("---------------------------------\n")

#Question 3
print("What is the capital of Spain?\n")
print("(A) Bilbao")
print("(B) Madrid")
print("(C) Valencia")
print("(D) Barcelona")
print("---------------------------------")

if hintCount > 0:
    getHint = input("Need a hint? [y], [n]: ")

    if getHint.capitalize() == "Y":
        hintCount -= 1
        print("Capital starts with letter 'R'")

answer = input("Your answer: ")

if answer.capitalize() == "B":
    print("Answer is correct!")
    points += 10
else:
    print("Answer is incorrect!")
print("---------------------------------\n")

#Question 4
print("What is the capital of the Netherlands?\n")
print("(A) Maastricht")
print("(B) Rotterdam")
print("(C) Den Haag")
print("(D) Amsterdam")
print("---------------------------------")

if hintCount > 0:
    getHint = input("Need a hint? [y], [n]: ")

    if getHint.capitalize() == "Y":
        hintCount -= 1
        print("Capital starts with letter 'R'")

answer = input("Your answer: ")

if answer.capitalize() == "D":
    print("Answer is correct!")
    points += 10
else:
    print("Answer is incorrect!")
print("---------------------------------\n")

#Question 5
print("What is the capital of the Czech Republic?\n")
print("(A) Prag")
print("(B) Krumau")
print("(C) Budweis")
print("(D) Brenn")
print("---------------------------------")

if hintCount > 0:
    getHint = input("Need a hint? [y], [n]: ")

    if getHint.capitalize() == "Y":
        hintCount -= 1
        print("Capital starts with letter 'R'")

answer = input("Your answer: ")

if answer.capitalize() == "A":
    print("Answer is correct!")
    points += 10
else:
    print("Answer is incorrect!")
print("---------------------------------\n")

#Question 6
print("What is the capital of Italy?\n")
print("(A) Vatican")
print("(B) Rome")
print("(C) Brixen")
print("(D) Palermo")
print("---------------------------------")

if hintCount > 0:
    getHint = input("Need a hint? [y], [n]: ")

    if getHint.capitalize() == "Y":
        hintCount -= 1
        print("Capital starts with letter 'R'")

answer = input("Your answer: ")

if answer.capitalize() == "B":
    print("Answer is correct!")
    points += 10
else:
    print("Answer is incorrect!")
print("---------------------------------\n")

#Question 7
print("What is the capital of Ireland?\n")
print("(A) Kirk")
print("(B) Galway")
print("(C) Dublin")
print("(D) Kilkenny")
print("---------------------------------")

if hintCount > 0:
    getHint = input("Need a hint? [y], [n]: ")

    if getHint.capitalize() == "Y":
        hintCount -= 1
        print("Capital start with letter 'D'")

answer = input("Your answer: ")

if answer.capitalize() == "C":
    print("Answer is correct!")
    points += 10
else:
    print("Answer is incorrect!")
print("---------------------------------\n")

#Question 8
print("What is the capital of France?\n")
print("(A) Marseille")
print("(B) Bordeaux")
print("(C) Lyon")
print("(D) Paris")
print("---------------------------------")

if hintCount > 0:
    getHint = input("Need a hint? [y], [n]: ")

    if getHint.capitalize() == "Y":
        hintCount -= 1
        print("Capital start with letter 'P'")

answer = input("Your answer: ")

if answer.capitalize() == "D":
    print("Answer is correct!")
    points += 10
else:
    print("Answer is incorrect!")
print("---------------------------------\n")

print("Your score: " + str(points))
print("Hints left: " + str(hintCount))