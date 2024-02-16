# Take user input and print the user details and type the data type of each variable.

user_name = str(input("Enter the User Name: "))
user_age = int(input("Enter the User Age: "))
user_roll_Number = int(input("Enter the User Roll Number: "))
user_phone_number = int(input("Enter the User Phone Number: "))


# print input variable Data type and display the input value.
print(type(user_name), "- User name is ", user_name)
print(type(user_age), " - User Age is ", user_age)
print(type(user_roll_Number), "- User Roll Number is ", user_roll_Number)
print(type(user_phone_number), "- User Phone Number is :", user_phone_number)
