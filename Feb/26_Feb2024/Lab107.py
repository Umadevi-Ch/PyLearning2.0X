class MyClass:

    def __init__(self):
        self.name = "Amit"

    def public_func(self):
        print("Public Function")

    def __private_func(self):
        print("This is private function")

    def public_fn_private(self):
        self.__private_func()
        # Private functions are created for security ie., Not everyone can access your variable and functions

a = MyClass()
a.public_func()
#a.__private_function