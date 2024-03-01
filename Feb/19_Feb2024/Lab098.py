class calc:
    def sum(self, a,b):
        return a+b

    def sub(self, a,b):
        return a -b


    def Prod(self, a,b):
        return a * b


    def Div(self, a,b):
        return a/b


object_ref = calc()
result = object_ref.sum(3,4)
print(result)

object_ref = calc()
result = object_ref.sub(7,3)
print(result)

object_ref = calc()
result = object_ref.Prod(3,4)
print(result)

object_ref = calc()
result = object_ref.Div(14,7)
print(result)