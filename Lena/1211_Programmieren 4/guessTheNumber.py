
import random 

print("Welcome to 'Guess the Number'!")
while True:
    #generate random int
    randNum = random.randint(0,10)
    
    attempts = 0

    #print(randNum)

    while True:
        try: 
            #user guesses the number
            guess = int(input("Guess the number between 1 and 10: "))
            attempts += 1

            #check if guess is correct
            if guess == randNum:
                print(f"Correct! You have guessed the number {randNum} after {attempts} attempts.")
                break
            elif guess < randNum:
                print("The number is higher the your guess!")
            else:
                print("The number is lower then your guess!")
        except ValueError:
            print("Input a valid number!")

    again = input("Do you like to play again [y], [n]:\n")

    if again == 'n':
        print("Byebye!")
        break
