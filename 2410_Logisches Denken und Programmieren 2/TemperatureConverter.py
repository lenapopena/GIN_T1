print("Convert temperature to K°, C° or F°\n")

print("Choose one of the following converting methods: ")
print("+----------------------------------------------+")
print("| (1) Kelvin -> Celsius                        |")
print("| (2) Kelvin -> Fahrenheit                     |")
print("| (3) Celsius -> Kelvin                        |")
print("| (4) Celsius -> Fahrenheit                    |")
print("| (5) Fahrenheit -> Kelvin                     |")
print("| (6) Fahrenheit -> Celsius                    |")
print("+----------------------------------------------+")

convMethod = int(input("Choose: "))

#Kelvin
if convMethod == 1 or convMethod == 2:
    kelvin = float(input("Input your kelvin value: "))
    if convMethod == 1:
        #kelvin -> celsius
        res = kelvin - 273.15
        print(str(kelvin) + " °K equals " + str(res) + " °C")
    else:
        #kelvin -> fahrenheit
        res = ((kelvin - 273,15) * 1.8) + 32
        print(str(kelvin) + " °K equals " + str(res) + " °F")
#Celsius
elif convMethod == 3 or convMethod == 4:
    celsius = float(input("Input your celsius value: "))
    if convMethod == 3:
        #celsius -> kelvin
        res = celsius + 273.15
        print(str(celsius) + " °C equals " + str(res) + " °K")
    else:
        #celsius -> fahrenheit
        res = celsius * 1,8 / 32
        print(str(celsius) + " °C equals " + str(res) + " °F")
#Fahrenheit
elif convMethod == 5 or convMethod == 6:
    fahrenheit = float(input("Input your fahrenheit value: "))
    if convMethod == 5:
        #fahrenheit -> kelvin
        res = ((fahrenheit - 32) / 1.8) + 273.15
        print(str(fahrenheit) + " °F equals " + str(res) + " °K")
    else:
        #fahrenheit -> celsius
        res = (fahrenheit * 1.8 / 32)
        print(str(fahrenheit) + " °F equals " + str(res) + " °C")




