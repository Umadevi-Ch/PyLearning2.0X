# Method OverLoading
# Python does not support Method overloading in the traditional sense
# Method overloading means same name of a function with different parameter


class MathUtil:
    def add(self,a,b=0,c=0):
        return a+b+c
    #def add(self,a,b):#TypeError: MathUtil.add() missing 1 required positional argument: 'b'
     #   pass
math = MathUtil()
op0 = math.add(1)
op1 = math.add(1,2)
op2 = math.add(1,2,3)
print(op2)

