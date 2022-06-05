def make_pizza(size, *toppings):
    """Print the topping thst have been requested"""
    print("\nMaking a " + str(size) + " pizza with the folowing toppings:")
    for topping in toppings:
        print("- " + topping)
