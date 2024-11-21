def returnValue(num):
    if num == 0:
        raise ValueError("The return value from 0 is not defined")
    return 1 / num

def main():
    print("Calculate return value:")
    print("-----------------------")

    while True:
        #user input
        num = float(input("Input your number: "))

        retVal = returnValue(num)
        print(f"The return value of {num} is: {retVal}")

        again = input("Calculate another return value? [y], [n]:\n")

        if again.lower() == 'n':
            print("Byebye!")
            break

if __name__ == "__main__":
    main()