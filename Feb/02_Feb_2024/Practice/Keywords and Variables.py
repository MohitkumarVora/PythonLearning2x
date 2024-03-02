# Keyword and Identifier
# Keyword - reserved words.
# Variable name = Variable value

#define variable name in different ways
PI = 3.14 # Constant = Uppercase
temp_pi = 8.98 # variable
print() # function name is always smaller case


age = 45
print(age)
age = "Mohit"
print(age)
age = 'C'
print(age)

# class = "Mohit"
_123 = 789
print(_123)

_ = "Akash"
print(_)

#______________________________________
#Python is Case sensitive Language so Upper and Lower case Variables are consider as different
age = 45
Age = 56

#class = "Mohit"
Class = "mohit"
print(Class)

#as = "Mohit"
As = "At"
print(As)

#print list of Keywords which was use by Python
import keyword
print(keyword.kwlist)

# Take a User Input and Print the details
name = input("Enter your Name")
print("This is your name", name)

#Variable Override
a = 10
b = a
c = b
a = "Mohit"
print(a)
print(b)
print(c)
