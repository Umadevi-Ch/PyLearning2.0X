# Multiple Inheritance
# father and Mother ----> Son
class Father:
    def father_money(self):
        return "5"

    def home(self):
        return "This is from the Father"

class Mother:
    def mother_money(self):
        return "10"

    def home(self):
        return "This is from the Mother"


class Son(Father, Mother):
    pass

son = Son()
print(son.father_money())
print(son.mother_money())
print(son.home())
print(Son.mro()) #[<class '__main__.Son'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>]
# Object is the Father of all the classes.. by default object is Father class.

#MRO- Method Resolution Order