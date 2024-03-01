# Tuple - A collection of items like list
# but list is mutable

my_list = [1,2,3,4,5]
my_list[0]=21
print(my_list)
print(type(my_list))
print(len(my_list))
#Tuple
my_tuple = (1,2,3,4,5)
#my_tuple[0] = 21
print(my_tuple) #TypeError: 'tuple' object does not support item assignment
print(type(my_tuple))
print(len(my_tuple))


new_tuple = tuple(my_list)
print(new_tuple)
