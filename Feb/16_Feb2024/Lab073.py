import math
def sq_rt(num):
    return math.sqrt(num)
my_list = [25,36,64]
sq_list = list(map(sq_rt,my_list))
print(sq_list)