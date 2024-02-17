# Functions
# Block of code which can be executed
#They can return something
#They cant return --> Nonreturn type
#They have parameters
#They dont have parameters/ arguments

#Define --> call
def say_Hello():
    print("Hello")

say_Hello()

#With arguments
def say_Hello_arg(name):
    print("Hello", name)

say_Hello_arg("Amit")

#With Multiple arguments
def say_Hello_args(name, age):
    print("Hello", name, age)

say_Hello_args("Amit", 65)

#with default arguments
def say_Hello_args_default(name= "Pramod"):
    print("Hello", name)

say_Hello_args_default("Amit")
say_Hello_args_default()

#With Return Values
def sum_number_argument_ret(a,b):
    return a+b
Result=sum_number_argument_ret(3,4)
print(Result)

#With any data type
def sum_number_argument_ret(a,b):
    return a+b
Result1=sum_number_argument_ret(3,4)
Result2=sum_number_argument_ret("Pramod","Dutta")
Result3=sum_number_argument_ret(a= 10, b= 19)
print(Result1)
print(Result2)
print(Result3)

