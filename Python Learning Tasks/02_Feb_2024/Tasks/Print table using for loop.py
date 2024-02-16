# print table using "for" loop

print("------ Print table using 'For' loop--------")

table_number = int(input("Enter the table number you want: "))
for i in range(1, 11):
    result = (table_number*i)
    print(f"{table_number} x {i} = {result}")
