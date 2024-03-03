# try, except and finally
# multiple exception

try:
    num1 =int(input("Enter the number 1\n"))
    num2 =int(input("Enter the number 2\n"))
    result = num1/num2
except ValueError as v:
    print(v)
except ZeroDivisionError as z:
    print(z)
else:
    print(f"Result {result}")
finally:
    print("I will be executed anyhow!")