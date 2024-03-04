# Class & Objects in Python
# Class -  Attributes and Behaviour
# Person -> Object Mohit, Akash, Nirav

class Person:
    # Attributes  -> Data members
    name = None
    age = None
    id = None
    phone_no = None

    # Behaviour -> Methods (not the functions)
    def talk(self):
        print("I cam talk")

    def another(self):
        print("I am a Method")

    def sleep(self, name):
        print("I am a Method!!")
        print("Sleep", name)

    def walk(self):
        return "I am walking"


def another():
    print("I am f(n)")


# Objects - ClassName()
nirav = Person()
nirav.name = "nirav"
print(nirav.name)
nirav.talk()  # This belong Nirav

Mohit = Person()

Akash = Person()
# Nothing is there, So clean the memory
# exit the program
