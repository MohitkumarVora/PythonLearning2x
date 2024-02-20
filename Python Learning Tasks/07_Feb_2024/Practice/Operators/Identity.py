x = ["apple", "banana"]
y = ["apple", "banana"]
z = x


# "is" identity Operators:
print(x is z)  # returns True because z is the same object as x
print(x is y)  # returns False because x is not the same object as y, even if they have the same content
print(x == y)  # to demonstrate the difference between "is" and "==": this comparison returns True because x is equal to y

# "is not" identity Operators:
print(x is not z)  # returns False because z is the same object as x
print(x is not y)  # returns True because x is not the same object as y, even if they have the same content
print(x != y)  # to demonstrate the difference between "is not" and "!=": this comparison returns False because x is
# equal to y
