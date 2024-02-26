# Class & Objects in Pyhton
# Class - Attributes and Behavior
# Person  -> Objecta Vani, Pramod, Sriram

class person:
    # Attributes -> Data members
    name = None
    age = None
    id = None
    phone_no = None


# Behavior -> Methods (not the functions) whenever a function used in the class is called a Method
def talk(self):  # self means it is own instance,
    # this is the first argument for every function with in the class,
    # instance reference
    print("I can talk")


def sleep(self):
    print("I can sleep")


def walk(self):
    print("I can walk")


# Objects- ClassName()
SriRam = person()
SriRam.name = "Shree Ram"
print(SriRam.name)
Pramod = person()
amit = person()
