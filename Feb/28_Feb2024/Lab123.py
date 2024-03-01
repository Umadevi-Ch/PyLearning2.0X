# Method Overriding - Same name in the Parent and Child
# Method Overriding means child always over ride the parent functions.
#super() means call my parent function

class Animal:

    def __init__(self):
        pass
    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def __init__(self):
        pass
    def sound(self):
        #super().sound()
        print("Dog Sound")

animal = Animal()
animal.sound()

dog = Dog()
dog.sound()