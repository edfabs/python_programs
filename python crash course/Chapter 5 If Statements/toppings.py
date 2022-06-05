
# request_topping = 'mushrooms'

# if request_topping != 'anchovies':
#     print('Hold the anchovies!')

# request_topping = ['mushrooms', 'onions', 'pineapple', 'extra cheese']

# if 'mushrooms' in request_topping:
#     print('Adding mushrooms')
# elif 'pepperoni' in request_topping:
#     print('Adding pepperoni.')
# elif 'extra cheese' in request_topping:
#     print('Addinf extra cheese.')

# print("\nfinished making your pizza!")


# requested_toppings = []
# if requested_toppings:
#     print()
# else:
#     print('Are you sure you want a plain pizza?')

available_toppings = ['mushrooms', 'olives',
                      'green peppers', 'pepperoni', 'pinapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping)
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nfiniched making your pizza!")
