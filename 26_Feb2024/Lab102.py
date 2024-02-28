class Person:
    # class variables? instance variables
    name = None
    age =  None

    def walk(self):
        a = 10 # local variable
        print("Hi your name is ", self.name)
        print("Hi your age is ", self.age)
        print(a)
amit = Person()
amit.walk()

#constructor will basically change the values