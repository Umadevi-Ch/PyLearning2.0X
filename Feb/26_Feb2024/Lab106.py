#Encapsulation - binding the data and methods (hide the important variables)
# Data members / Class variable-
# Functions - they are closed with in a single blueprint
# Wrapping or binding the data variables with the methods

class Car:
    name =  None
    password = "123"
    # 3 different types of data members / class variables

    def __init__(self):
        self.public_var =  "public" #Public - Anyone can access it
        self._protected_var = "protected123"
        self.__private_var = "pass@123"
        self.__password ="pass@123"

    def _protectedmethod(self):
        print("Protected!")

    def __privatemethod(self):
        print("Protected!")

    def printName(self):
        print("I am allowed to use the private variable becos i am in class "+self.__password)

xuv =Car()
xuv.printName()

print(xuv.public_var)
print(xuv.password)
print(xuv.printName())
