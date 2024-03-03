# Tuple - Collection of items

# List - Collection of items
# mutable -

my_list = [1, 2, 3, 4, 5]
my_list[0] = 21
print(my_list)
print(type(my_list))

# Tuple -
my_tuple = (1, 2, 3, 4, 5)
# my_tuple[0] = 21  # TypeError: 'tuple'
print(my_tuple)
print(type(my_tuple))
print(len(my_tuple))

new_tup = tuple(my_list)
print(new_tup)

print("---------------------")

API_URLS = ("sdet.live", "google.com", "tta.com")
print(API_URLS[0])
print(API_URLS[1])

print("---------------------")

tuple1 = ()
tuple2 = (1, 2, 3, 4, 5)
tuple3 = tuple(["Mohit", "Lucky", 123])

print(tuple1)
print(tuple2)
print(tuple3)

del tuple3

try:
    print(tuple3)
except Exception as e:
    print(e)

print("------------------")

tuple3 = tuple(["Mohit", "Lucky"])
print(tuple3)
print(tuple3[1])

hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = hero1 + hero2
print(awesome_team)
print(list(awesome_team))

# Convert to List
my_tuple = (1, 2, 3, 4, 5)
print(list(my_tuple))

print("-----------------------")

x = 10
a, b = 23, 34
q, w, e = (45, 56, 78)

# Nested Tuples
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = (hero1, hero2)
print(awesome_team)
print(awesome_team[0][1])
print(awesome_team[1][1])

# Search in Tuple
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Paris" in cities)
print("Moscow" in cities)


print("------------------------")

# String - String is a bunch of character
name = "Mohit"
# name[0] = "A" # TypeError: 'str'
print(name)

# append, clear, pop, del , push, extend, remove, sort, reverse

# String is a bunch of character, immutable
# tuple is list of any data type items which can't changed.
# list is collection of items, which can be changed, you can duplicate

