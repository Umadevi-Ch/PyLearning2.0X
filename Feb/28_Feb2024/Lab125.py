# Abstraction
# Hiding the details and showing what is required.
#Ex: For a car..
#We dont know how the car engine is started
# How gear box is managed?
#Hide the implementation and show only the important details
# In Java Abstraction is done by Abstract Class and interface
#In Python Abstraction is done by
#1. Abstract Base classes
#2. Abstract Base methods

from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass
class Cat(Animal):
    def sound(self):
        return "Meow"
class Dog(Animal):
    def sound(self):
        return "Bow Bow"
dog = Dog("Browny")
print(dog.sound())

cat = Cat("Pussy")
print(cat.sound())