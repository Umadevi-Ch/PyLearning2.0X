def make_pizza(*toppings):
    for topping in toppings:
        print(topping,"\r")

k = make_pizza("mushroom","cheese")
t = make_pizza("mushroom","veggies")
r = make_pizza("mushroom","meat")