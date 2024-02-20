"""
Write a Python program to calculate the area of a circle given its radius using the formula area=π×r^2
(Take pie as 3.14)
"""
import math

pi = 3.14
radius = int(input("Enter the radius of circle: "))

# Normal approach
area_of_circle = pi * (radius * radius)
print("area of circle with Normal approach: ", area_of_circle)

# Using Exponentiation arithmetic Operator
area_of_circle = (pi * (radius ** 2))
print("area of circle with arithmetic Operator: ", area_of_circle)

# Using math.pi approach
area_of_circle = math.pi * math.pow(radius, 2)
print("area of circle using math.pi approach: ", area_of_circle)
