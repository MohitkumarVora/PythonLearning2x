# Create a program that takes two numbers as input and print whether
# the first number is greater than, less than, or equal to the second number.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("greater than status: ", num1 > num2)
print("less than status: ", num1 < num2)
print("equal to status: ", num1 == num2)

if num1 > num2:
    print("num1 is greater than num2")
elif num1 < num2:
    print("num1 is less than num2")
elif num1 == num2:
    print("num1 is equal to num2")
