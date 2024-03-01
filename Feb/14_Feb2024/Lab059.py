def make_pizza(*toppings):
    print(toppings)
    for topping in toppings:
        print(topping)

pramod= make_pizza("mushroom", "onion", "tomato")
santosh = make_pizza("mushroom","pineapple","paneer","tomato")
vinay = make_pizza("mushroom","pineapple","paneer","sweetcorn")


def make_pizza_base(*toppings,base):
    print(toppings,base)
    for topping in toppings:
        print(topping)
amit= make_pizza_base("mushroom", "onion", "tomato",base="thin")