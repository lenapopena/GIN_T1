import random

zufallszahl = random.randint(0, 10)

gewonnen = False

weiterspielen = True
beenden = False


while weiterspielen:
    print("rate die zahl")
    geratene_zahl = int(input())
    if zufallszahl == geratene_zahl:
        print(f"das ist richtig! die zufallszahl und deine geratene lauten: {zufallszahl}.")
        gewonnen = True
        weiterspielen = False
    elif zufallszahl > geratene_zahl:
        print("die zahl ist größer")
    else:
        print("die zahl ist kleiner")

    if weiterspielen == False:
        print("möchtest du nochmal spielen?")
        nochmal = input()
        if nochmal == "ja":
            weiterspielen = True
        else:
            weiterspielen = False