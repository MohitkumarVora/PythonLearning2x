# Strings is basically a bunch of Characters
# define string by using (double cot)"" or (single cot)''
name1 = "Mohit"
name2 = 'Mohit'
print("print variable 'name1' assigned value: ", name1)
print("print variable 'name2' assigned value: ", name2)
print("print variable 'name1' data type: ", type(name1))
print("print variable 'name2' data type: ", type(name2))

# raw String
# This will be helpful in the dir paths
Dir = r'C:\Program Files\PythonProject'
print(Dir)


# format String
first_name = "Akash"
last_name = "Khatri"
age = 40
isMarried = True
print(f'My friend name is {first_name} {last_name}, his age is {age} and he is Married = {isMarried} ')

name = "batman"

print("print length of the character count: ", len(name))  # len -> 1
print("print string character using positive indexing: ", name[4])
print("print string character using positive indexing: ", name[5])
# print(name[6]) # IndexError: string index out of range
print(len(name)-1)
print(name[len(name)-1])

# String - Immutability
# that can't be changed, modify
string = "Hello"
string = "Pramod"
print("String override example", string)
# string[0] = "P" #TypeError: 'str' object does not support item assignment

name = "This is a Big line"
print("Print string last character using negative indexing: ", name[-1])
print("Print string last character using negative indexing: ", name[-2])
print("Print length of the String", len(name))
