a = int(input("Enter the number 1\n"))
b = int(input("Enter the number 2\n"))
try:
    c= a/b #ZeroDivisionError: division by zero
    print("Div is ",c)
except Exception as e:
    print(e)
    print("zero Division, Please don't use B as zero!")
print("This is an important message that we need to show to the user")