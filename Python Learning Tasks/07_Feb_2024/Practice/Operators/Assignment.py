from datetime import date


user_name = "Mohit"
user_age = 35
user_DOB = date(1988, 3, 30).strftime('%Y/%m/%d')

print("User details is:\n", "Name: ", user_name, "Age: ", user_age, "DOB: ", user_DOB)
