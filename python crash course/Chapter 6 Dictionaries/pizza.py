pizza = {
    'crush': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
print("You order a " + pizza['crush'] +
      "-crush pizza" + "wite the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
