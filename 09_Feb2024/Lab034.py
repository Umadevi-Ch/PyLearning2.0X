import math

number1 = float(input("Enter the number1 "))
sq = number1 ** 2
print("square of ", number1, "is",  sq)

number2 = float(input("Enter the number2 "))
sqrt = math.sqrt(number2)
print("squre root of the " ,number2, "is ", sqrt)

number3 = float(input("Enter the number3 "))
cube = number3 ** 3
print("cube of the" ,number3, "is", cube)

number4 = float(input("Enter the number4 "))
# cube = math.pow(number, 3)
cuberoot = math.cbrt(number4)
print("cuberoot of the ", number4," is ", cuberoot)


result = math.sin(45)
print("sin(45) is", result)