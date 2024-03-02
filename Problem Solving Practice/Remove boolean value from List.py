# Write a program to remove the boolean value from list.


my_list = [1, True, 3, False, "Mohit"]
my_list1 = []

# Find the boolean instance and exclude those list value
for i in my_list:
    if not isinstance(i, bool):
        my_list1.append(i)  # add other than boolean value in the another list
print(my_list1)
