# Dictionary Dict
# Key and Value
name = "Pramod"
#Key --> name
# Value --> Pramod
# A Dictionary is an unordered collection of data
# in a key - value pair format
# A key must be unique and value can be duplicate

my_dict = {}
my_dict2 = dict()
print(type(my_dict))
print(type(my_dict2))

phone_book = {"Batman":987654321, "Superman":123456789, "Wonder":132343546}
print(len(phone_book))
print(phone_book["Batman"])

phone_book2 = dict(Batman = 123,ceiser = 342, GB = 323)
print(phone_book2)
print(phone_book2['GB'])
print(phone_book2["GB"])
print(phone_book2.get('GB'))
print(phone_book2.get("GB"))


Pramod_Details = dict(name= 'Pramod', age = 34, isMale = True, Address = "KA")
Pramod_Details2 = {"name":"Pramod", "90": 34.34,"isMale":True, "Address": "KA"}
print(Pramod_Details2.get(90))   #None
print(Pramod_Details2.get("90"))

my_dict = {'a':1,'b':2,'c':3,'a':90}
print(len(my_dict))
print(my_dict)