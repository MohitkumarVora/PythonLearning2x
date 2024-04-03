# Web Automation - Selenium

# Page - You are going automate

class VWOLoginPage:
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def loginconfirm(self):
        if self.password == "Pass123":
            print("You are allowed to enter")
        else:
            print("Invalid user")


amit = VWOLoginPage("akash@akash.com", "123")
amit.loginconfirm()

print(" ------")

pramod = VWOLoginPage("mohit@mohit.com", "Pass123")
pramod.loginconfirm()

print("Akash ID:", id(amit))
print("Mohit ID:", id(pramod))
