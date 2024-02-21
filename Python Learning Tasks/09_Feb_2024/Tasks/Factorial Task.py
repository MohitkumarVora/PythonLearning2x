# # Factorial
# n = 5
# 5*4*3*2*1 => 120
# n = 3
# 3*2*! => 6

fact = 1
number = int(input("Enter the number to calculate factorial: "))

# first approach with increment for loop
print("First approach with increment for loop: ")
if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("Factorial of 0 is 1.")
else:
    for i in range(1, number + 1, 1):
        j = fact
        fact = fact * i
        print(fact, "= ", i, "* ", j)

print("Factorial of ", number, "is ", fact)


"""
# second approach with decrement for loop
print("Second Approach with decrement for loop: ")
if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("Factorial of 0 is 1.")
else:
    for i in range(number, 0, -1):
        j = fact
        fact = fact * i
        print(fact, "=", i, "* ", j)
print("Factorial of ", number, "is ", fact)
"""


"""
# Third approach with return function call
def factorial(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result

# Test the function
number = int(input("Enter a number to calculate its factorial: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("Factorial of 0 is 1.")
else:
    print("Factorial of", number, "is", factorial(number))
"""