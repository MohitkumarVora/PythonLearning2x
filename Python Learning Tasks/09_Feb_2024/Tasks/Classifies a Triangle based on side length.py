# Write a program that classifies a triangle based on its side lengths.

"""
Requirement: Given three input values representing the lengths of the sides,
determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal),
or scalene (no sides are equal).

Logic: Use an if-else statement to classify the triangle.
3 Input
side 1, side 2 and side 3
output - Eq, Iso, Scalene -
Eq. = side 1 == side 2 = side 3
"""

side_1 = int(input("Enter the Side 1 Length: "))
side_2 = int(input("Enter the Side 2 Length: "))
side_3 = int(input("Enter the Side 3 Length: "))

if side_1 == side_2 == side_3:
    print("This is the Equilateral Triangle when all sides are equal!")
elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
    print("This is the Isosceles Triangle when exactly two sides are equal!")
elif side_1 != side_2 or side_1 != side_3 or side_2 != side_3:  # here we can use "else" as well.
    print("This is the Scalene Triangle when no sides are equal!")
