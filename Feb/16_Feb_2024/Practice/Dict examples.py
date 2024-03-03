# Dict
# Key and Value
name = "Mohit"
# Key -> name
# Value -> "Mohit"
# A dictionary is an unordered collection of data
# in a key-value pair format.
print("-------------")

my_dict = {}
my_dict2 = dict()
print(type(my_dict))
print(type(my_dict2))

print("---------------")

phone_book = {"Batman": 987654321, "Superman": 1234567890, "Wonder": 97876545}
print(len(phone_book))
print(phone_book["Batman"])  # print "Batman" value

phone_book2 = dict(Batman=123, Cersei=342, GB=323)
print(phone_book2)  # print "phone_books" dict key and value

print(phone_book2['GB'])
print(phone_book2["GB"])
print(phone_book2.get('GB'))
print(phone_book2.get("GB"))

Mohit_details2 = {"name": "Pramod", "90": 34.34, "isMale": True, "Address": "KA"}
print(Mohit_details2.get("90"))

my_dict = {'a': 1, 'b': 2, 'c': 3, 'a': 95}  # duplicate keys dict
print(len(my_dict))
print(my_dict)
