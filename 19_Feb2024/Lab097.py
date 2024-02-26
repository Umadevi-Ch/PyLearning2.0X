# Car
# Objects - Tesla,Lambo


class Car:
    name = None
    color = None
    model = None
    speed = None
    engine = None

    def start_engine(self):
        print("starting engine")

    def drive(self):
        print("Drive")

    def car_break(self):
        print("Break")

    def who_is_driving(self):
        print("I am driving ->" + self.name)

tesla_obj_ref = Car()
Lambo_obj_ref = Car()

tesla_obj_ref.name = "Tesla"
Lambo_obj_ref.name = "Lambo"

tesla_obj_ref.who_is_driving()
Lambo_obj_ref.who_is_driving()
