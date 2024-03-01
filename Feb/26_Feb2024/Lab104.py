#Web Automation - Selenium
# Page - you are going to automate

class VWOLoginPage:
    email = None
    password = None

    def __init__(self, email, password):
        self.email  = email
        self.password = password

    def loginconfirm(self):
        if self.password == "Pass123":
            print("You are allowed to enter")
        else:
            print("Invalid User")

amit = VWOLoginPage("amit123","password""\n")
amit.loginconfirm()

pramod = VWOLoginPage("pramod@123", "Pass123")
pramod.loginconfirm()


print(id(amit))
print(id(pramod))