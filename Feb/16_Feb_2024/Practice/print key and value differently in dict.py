from collections import OrderedDict

# Dict - It will not keep the Order of insertion
# OrderedDict - It will keep the order of insertion
od = OrderedDict()
od['a'] = 45
od['c'] = 78
od['b'] = 97
od['d'] = 31
print(od)

print("-----------------------------------------")

my_dict = {'b': 2, 'c': 3, 'a': 95}
print(my_dict)

keys = my_dict.keys()
values = my_dict.values()
print(values)
keys_list = list(keys)
print(keys_list)

print("-----------------------------")

my_dict = {'a': 1, 'b': 2}
val = my_dict.pop('a')
print(val)

knights = {'Wonder_Woman': 'the pure', 'Captain_America': 'the brave'}
print(len(knights))

for k, v in knights.items():  # print key and value using "item" function with for loop
    print(k, " - ", v)


