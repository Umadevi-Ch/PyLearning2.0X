class GF:
    def car(self):
        return "Old Car"

class F(GF):
    def car(self):
        return "honda civic"

class S(F):
    def car(self):
        return "Lambo"

son = S()
print(son.car())