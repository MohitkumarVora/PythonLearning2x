# Condition
# age > 18 -> You are allowed to go the club
# age < 18 -> You are not allowed

age = int(input("Enter the your age: "))  # if condition: -> return true or false

if age > 18:
    print("You are allowed to go the club")
else:
    print("You are not allowed!")

print("\n_________________________________________")

# Problem  Find the Max between 3 numbers
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

max_num = max(num1, num2, num3)
print(max_num)

if num1 > num2 and num1 > num3:
    print("Max is: ", num1)
elif num2 > num1 and num2 > num3:
    print("Max is: ", num2)
else:
    print("Max is: ", num3)
