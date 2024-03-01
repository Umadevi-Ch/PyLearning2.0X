# Triangle Classifier
# if side1 = side2= side3----Equi
# if side 1= =side2 or side2 == side3 or side 1==side3--> Iso
# Else --> scalene

side1 = float(input("Enter the side1\n"))
side2 = float(input("Enter the side2\n"))
side3 = float(input("Enter the side3\n"))

if side1 == side2 == side3:
    print("It is an Equilateral Triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("It is an Isosceles Triangle")
else:
    print("It is scalene triangle")
