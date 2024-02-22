# Match Case
# Switch
numbers = int(input("Enter a Number 1-5\n"))
match numbers:  # BREAK IS NOT NEEDED in case of Match and CASE
    case 1:
        print("You have entered 1")
    case 2:
        print("You have entered 2")
    case 3:
        print("You have entered 3")
    case 4:
        print("You have entered 4")
    case 5:
        print("You have entered 5")
    case _:
        print("No idea")

# Another example of Match Case
browser = str(input("Enter the browser name\n"))
browser = browser.lower()
match browser:
    case "chrome":
        print("Chrome code executed!")
    case "firefox":
        print("FF code executed!")
    case _:
        print("No browser Found!")
