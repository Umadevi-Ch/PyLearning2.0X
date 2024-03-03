try:
    c = 10/0
except Exception as e:
    print(e)


try:
    a =int(input("Enter a number only\n"))
except ValueError as v:
    print("Hi",v)
except Exception as e:
    print(e)
else:
    print("Else")
