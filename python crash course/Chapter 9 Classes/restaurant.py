class Restaurant():
    """Restaurant class"""

    def __init__(self, restaurant_name, cousine_type):
        """Initialize the name od the restaurant and the type of cousine"""
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type
        self.number_served = 0

    def describe_restaurante(self):
        """Method to describe the restaurant"""
        print(self.restaurant_name.title(
        ) + " is a a restaurant with type of cousine " + self.cousine_type.title())

    def open_restaurant(self):
        """Method to advertise the schedule"""
        print(self.restaurant_name.title() + " opens at 9:00 hrs to 19:00 hrs")

    def customers_served(self):
        """Method to print the number of customers serverd"""
        print(str(self.number_served) + " customers served")

    def set_number_served(self, number):
        """method to change the number of customers served"""
        self.number_served = number

    def increment_number_served(self, number):
        """Method to increment of number of customers served"""
        self.number_served += number
