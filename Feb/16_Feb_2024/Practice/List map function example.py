import math

# Map()


def sq_of_number(num):
    return num ** 2


# result = sq_of_number(10)
# print(result)

numbers = [1, 2, 3, 4, 5]

# Map() -
# 1. Takes Each item from the list
# 2. execute the function on it.
# 3. Return same number of elements ( list)

sq_numbers = list(map(sq_of_number, numbers))
# 1,4,9, 16,25
print(sq_numbers)

print("-------------------------------------")


def sq_rt(num):
    return math.sqrt(num)
    # return math.cbrt(num)


# list, set, tuple, dic

my_list = [21, 34, 54]
sq_list = list(map(sq_rt, my_list))
print(sq_list)
