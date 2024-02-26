class Mul_param:
    name = None #Class Variable
    def print_information(self,First_name,Last_Name,Age):
        a = 10 # Local Variable
        print("your name is ", First_name, Last_Name, Age)

obj_ref = Mul_param()
obj_ref.print_information("Amit", "Sharma", 68)