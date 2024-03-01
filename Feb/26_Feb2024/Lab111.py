class Father:
    __private_villa_= "GOA"
    gold = 5
    def drive_car(self):
        print("Lambo")

    def threeBHKflat(self):
           print("3BHK Flat")

    def private_villa_(self,is_my_son):
        print(self.__private_villa_)
class Son(Father): # Single Inheritance...
    pass

pramod = Son()
print(pramod.gold)
pramod.drive_car()
pramod.threeBHKflat()
#print(pramod.__private_villa)
pramod.private_villa_(True)

mmd = Father()
print(mmd.gold)
mmd.drive_car()
mmd.threeBHKflat()