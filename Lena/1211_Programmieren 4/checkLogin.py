user_name = "Neysi"
password = "12345"

print("Please give your username: ")
input_user = input()

print("Please give your password: ")
input_password = input()

if input_user == user_name and input_password == password:
    print("The Username and Password are correct")
else:
    print("The username or password are not correct")