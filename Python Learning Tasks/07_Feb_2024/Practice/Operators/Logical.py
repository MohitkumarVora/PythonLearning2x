# Logical "and" operator
x = 5
print(x > 3 and x < 10)  # returns True because 5 is greater than 3 AND 5 is less than 10
if (x >3 and x < 10):
    print("print the x value when both condition match", x)

# Logical "or" operator
x = 5
print(x > 3 or x < 4)  # returns True because one of the conditions are true (5 is greater than 3, but 5 is not less
# than 4)
if (x > 3 or x < 4):
    print("print the x value when one of the condition are true", x)

# Logical "not" operator
x = 5
print(not(x > 3 and x < 10))  # returns False because not is used to reverse the result
if (not(x > 3 and x < 10)):
    print("print the x value when non of the condition true", x)
