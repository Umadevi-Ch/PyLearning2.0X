# Hierarchical Inheritance
class Father:
    def home(self):
        return "This is a Father Home"

class Pramod(Father):
    pass
    #def home(self):
     #   return "This is a Pramod's Home."
class Bro_of_Pramod(Father):
    def home(self):
        return "This is a Brother Home"

pramod = Pramod()
print(pramod.home())
