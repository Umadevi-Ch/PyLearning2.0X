class Car:
    name = None
    make = None
    model = None

    def __init__(self,o_name,o_make,o_model): #SPecial Function it will automatically called whenever object is created
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
                print("Starting a car with the name " + self.name)
                print("Starting a car with the make " + self.make)
                print("Starting a car with the model " + self.model)
lambo = Car("lambo","V2","2024 \n")
lambo.start_engine()

xuv = Car("XUV", "V3", "2024 \n")
xuv.start_engine()