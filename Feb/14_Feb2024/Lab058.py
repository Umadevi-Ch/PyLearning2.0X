# *args and **kwargs
def f1(a=1, b=1, c=1):
    return a + b + c


f1()
f1(1)
f1(1, 1, 1)
Ret = f1(10, 20, 30)
# Ret= f1(2,3,4)
print(Ret)


# args
def sum(a, b, c,d):
    return a+b+c+d


#r = sum(1, 2, 3)
r = sum(1, 2, 3, 4)
print(r)


def print_argument(*args):
    for i in args:
        print(i, end=" ")
print_argument(1)
print_argument(1, 2)
print_argument(1, 2, 3)
