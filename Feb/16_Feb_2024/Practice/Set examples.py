# SET
set3 = {1, 2, 3, 4, 5, 5, 4}
print(set3)

list1 = [45.2, 33, 33, 45, 21]
set1 = set(list1)  # Unordered, Unique
print(len(set1))
print(set1)

print("-------------------")

t = ("TheTestingAcademy", "for", "TheTestingAcademy")
print(set(t))

set1 = {1, 2, 3}
set2 = {4, 5, 6}
my_set = set1.union(set2)  # use "union" function to merge two set value in single set
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
my_set = set1.intersection(set2)  # use "intersection" function to get the similar value in two set values.
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
my_set = set1.difference(set2)  # use "difference" function to remove the similar value in the compare set value.
my_set2 = set2.difference(set1)
print(my_set)
print(my_set2)
