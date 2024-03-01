class Car:
    name = None
    color = None
    model = None
    speed = None
    engine = None

    def car_details(self):
        print("Your car details are ",self.color,self.model)

car_color = input("Enter your car color\n")
car_model = input("Enter your car model\n")

car_obj_ref = Car()
car_obj_ref.color = car_color
car_obj_ref.model = car_model

car_obj_ref.car_details()