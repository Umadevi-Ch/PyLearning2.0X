 # Multi Level Inheritance
class GF:
    def home(self):
        print("5BHK")
class Father(GF):
    def home2(self):
        print("Goa")
        #pass #pass means nothing is there in this class
class Son(Father):
    def home3(self):
        print("Mumbai")

pramod = Son()
pramod.home()
pramod.home2()
pramod.home3()

mmd = Father()
mmd.home()
#mmd.home2()
#mmd.home3()

gkd = GF()
gkd.home()
#gkd.home2()
#gkd.home3()