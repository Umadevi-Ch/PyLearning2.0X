#Lambda Express
#f(n) -> one liner in Python


#def double_my_salary(salary):
 #   return salary*2

#result=double_my_salary(10000)
#print(result)

d_salary= lambda salary: salary*2
print(d_salary(10))

pow_or_two= lambda num: num**2
print(pow_or_two(5))

sum = lambda a,b,c:a+b+c
print(sum(3,8,9))

say_my_name = lambda name:print("your name is ", name)
say_my_name("Pramod")
