# Hierarchical Inheritance
class Vehicle:
    def info(self):
        return "Ths is a vehicle"

class Car(Vehicle):
    def info(self):
        return "Ths is a Car."
class Bicycle(Vehicle):
    def info(self):
        return "Ths is a Bicycle"

car = Car()
bicycle = Bicycle()
print(car.info())
