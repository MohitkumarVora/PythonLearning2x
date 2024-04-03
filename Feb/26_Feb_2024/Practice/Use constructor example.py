class Car:
    name = None
    make = None
    model = None

    # Initialize the Constractor
    def __init__(self, car_name, car_make, car_model):  # Special F(n), called Object is created!
        self.name = car_name
        self.make = car_make
        self.model = car_model

    def start_engine(self):
        print("Starting a car with the name " + self.name)
        print("Starting a car with the make " + self.make)
        print("Starting a car with the model " + self.model)


lambo = Car("lambo", "V2", "2024")
lambo.start_engine()

print(" -- ---- ")

Tata = Car("Tata Nexon", "V6", "2023")
Tata.start_engine()
