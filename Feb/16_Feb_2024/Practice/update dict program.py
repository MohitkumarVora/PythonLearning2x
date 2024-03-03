api_response = {
    "first_name": "Mohit",
    "age": 35,
    "last_name": "Vora",
    "email": "mohit@yopmail.com",
    "password": "Test@4321",
    "commission": 10
}
print(api_response)
print(type(api_response))
print(api_response.get('password'))

api_response["password"] = "Mohit"
print(api_response)

print("---------print for loop details------")
for key, value in api_response.items():
    print(key, " => ", value)
