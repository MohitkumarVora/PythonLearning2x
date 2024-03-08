class Person:
    # Class Variables / Instance Var
    name = "Akash"
    age = None

    def walk(self):
        a = 10  # Local variable
        print("Hi your name is ", self.name)
        print("Hi your age is ", self.age)
        print(a)


Akash = Person()
Akash.walk()

Mohit = Person()
Mohit.walk()
