set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4}
subset = set2.issubset(set1)  # use "issubset" function to find the set2 value in set1 and return boolean value
print(subset)

for i in set1:
    print(i)

set1 = set([1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12])

print(set1)
set1.remove(5)
set1.remove(6)
print(set1)
print(len(set1))

print("--------------------")

