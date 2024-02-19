# Strings is basically a bunch of Characters
# define string by using (double cot)"" or (single cot)''
name1 = "Mohit"
name2 = 'Mohit'
print(name1)
print(name2)
print(type(name1))
print(type(name2))

# raw String
# This will be helpful in the dir paths
Dir = r'C:\Program Files\PythonProject'
print(Dir)


# format String
first_name = "Akash"
last_name = "Khatri"
age = 40
isMarried = True
print(f'My friend name is {first_name} {last_name}, his age is {age} and he is {isMarried} ')

name = "batman"

print(len(name))  # len -> 1
print(name[4])
print(name[5])
# print(name[6]) # IndexError: string index out of range
print(len(name)-1)
print(name[len(name)-1])

# String - Immutability
# that can't be changed, modify
string = "Hello"
string = "Pramod"
print(string)
# string[0] = "P" #TypeError: 'str' object does not support item assignment
