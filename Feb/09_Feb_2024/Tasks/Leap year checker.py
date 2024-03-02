# Create a program that determines whether a given year is a leap year or not.

"""
Logic: A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
       Use an if-else statement to make this determination.

Example: Input = 2024
         Output = Leap year
"""

year_input = int(input("Enter a year to check if it's a leap year: "))
if year_input % 4 == 0 and (year_input % 100 != 0 or year_input % 400 == 0):
    print(f"{year_input} is a leap year!")
else:
    print(f"{year_input} is not a leap year.")

# Write a program to find the leap year numbers from the 1 to enter value and also display the count of leap years.

year_input = int(input("Enter a year to check if it's a leap year: "))
print("Leap years from 1 to", year_input, ":")
leap_year_count = []
for year_input in range(1, year_input + 1):
    if (year_input % 4 == 0 and year_input % 100 != 0) or (year_input % 400 == 0):
        print(year_input)
        leap_year_count.append(year_input)
print("Total of Leap Year Counts are: ", len(leap_year_count))
