# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
# 9-4. Number Served: Start with your program from Exercise 9-1 (page 166). Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again. Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business.


from collections import OrderedDict
from email import message
from random import randint


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


restaurant = Restaurant('Bistro', 'International')
print(restaurant.restaurant_name)
print(restaurant.cousine_type)
restaurant.describe_restaurante()
restaurant.open_restaurant()
restaurant.set_number_served(10)
restaurant.customers_served()
restaurant.increment_number_served(25)
restaurant.customers_served()


# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.


restaurant_2 = Restaurant('sushidom', 'japanise')
restaurant_3 = Restaurant('el 10', 'cortes de carne')

restaurant.describe_restaurante()
restaurant_2.describe_restaurante()
restaurant_3.describe_restaurante()

# 9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users, and call both methods for each user.

# 9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166). Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.


class User():
    """Clase usuario"""

    def __init__(self, first_name, last_name, username, age, email, privileges='user'):
        """Initialize the user instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.email = email
        self.login_attempts = 0
        self.privileges = privileges

    def descriptive_user(self):
        """Method to describe the user"""
        print("\nThe user names is: " + self.first_name.title() + " " + self.last_name.title() + " he's " +
              str(self.age) + " , his name is: " + self.username + " and his email is " + self.email)

    def great_user(self):
        """Method to personalize a greeting to the user"""
        print("\nHello " + self.first_name.title() + " " +
              self.last_name.title() + " you are the best user")

    def increment_login_attempts(self):
        """method to incement the attempts one by one"""
        self.login_attempts += 1

    def reste_login_attempts(self):
        """method to reset the number of attempts of login"""
        self.login_attempts = 0


user = User('fabian', 'suchett', 'edfabs', 33, 'fabian.suchett@edfabs.com')
user.descriptive_user()
user.great_user()

user_2 = User('karla', 'roaro', 'cdkarla', 34, 'cdkarla@gmail.com')
user_2.descriptive_user()
user_2.great_user()

user_3 = User('diego', 'suchett', 'diesur', 10, 'diesur@gmail.com')
user_3.descriptive_user()
user_3.great_user()

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(str(user.login_attempts) + " Number of attempts to login")
user.reste_login_attempts()
print(str(user.login_attempts) + " reset number of attempts")


# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.

class IceCreamStand(Restaurant):
    """Class to attempt to represent a restaurant od Ice cream"""

    def __init__(self, restaurant_name, list_flavors, cousine_type="Ice cream restaurant"):
        super().__init__(restaurant_name, cousine_type)
        self.list_flavors = list_flavors

    def display_flavors(self):
        print("The flavors of this restaurant is: ")
        for flavor in self.list_flavors:
            print("- " + flavor)


michoacana = IceCreamStand(
    'La michoacana', ['fresa', 'chocolotae', 'nuez', 'crema'])
michoacana.describe_restaurante()
michoacana.display_flavors()

# 9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 166) or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.

# 9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.


class Privileges():
    """Class that is an a attribute of Administrator class"""

    def __init__(self, privileges="admin"):
        """methot taht initialize the class privileges"""
        self.privileges = privileges

    def show_privileges(self):
        """Method to shoe the privileges of the user"""
        if self.privileges == 'admin':
            print("You have privileges like " + self.privileges.title())
            print("You can\n\t- Add post\n\t- Delete post\n\t- Ban user")
        else:
            print("You have privileges like " + self.privileges.title())


class Admin(User):
    """class inherited of user"""

    def __init__(self, first_name, last_name, username, age, email):
        super().__init__(first_name, last_name, username, age, email)
        self.privileges = Privileges()


admin = Admin('fabian', 'suchett', 'edfabs', 33,
              'fabian.suchet@edfabs.com')

admin.privileges.show_privileges()

# 9-9. Battery Upgrade: Use the final version of electric_car.py from this section. Add a method to the Battery class called upgrade_battery(). This method should check the battery size and set the capacity to 85 if it isn’t already. Make an electric car with a default battery size, call get_range() once, and then call get_range() a second time after upgrading the battery. You should see an increase in the car’s range.


class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize aatributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        """Set  the odometer reading to the riven value.
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back and odometer!")

    def increment_odometer(self, mileage):
        """Add the given amount to the odommeter reading."""
        self.odometer_reading += mileage


class Battery():
    """A simple attempt  to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """print a statement describing the battery size."""
        print("this car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "this car can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)

    def upgrade_battery(self):
        """his method should check the battery size and set the capacity to 85 if it isn’t already"""
        if self.battery_size != 85:
            print("This battery will be upgrade")
            self.battery_size = 85


class ElectricCar(Car):
    """Represent aspect of a car, spesific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electronic car
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don´t have gas tank"""
        print("this car doesn't need a gas tank!")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.update_odometer(22)
my_new_car.increment_odometer(100)
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

# 9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.

#  9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178). Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.

#  9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.

# 9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you used a standard dictionary to represent a glossary. Rewrite the program using the OrderedDict class and make sure the order of the output matches the order in which key-value pairs were added to the dictionary.

favorite_number = OrderedDict()

favorite_number['karla'] = 3
favorite_number['diego'] = 7
favorite_number['carlos'] = 15
favorite_number['fabian'] = 22

for name, number in favorite_number.items():
    print(name.title() + "'s favorite number is " + str(number))

# 9-14. Dice: The module random contains functions that generate random numbers in a variety of ways. The function randint() returns an integer in the range you provide. The following code returns a number between 1 and 6: from random import randint x = randint(1, 6) Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided


class Die():
    """Class Die"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        return x


my_random = Die()
print(f"The random number s: {my_random.roll_die()}")

# 9-15. Python Module of the Week: One excellent resource for exploring the Python standard library is a site called Python Module of the Week. Go to http://pymotw.com/ and look at the table of contents. Find a module that looks interesting to you and read about it, or explore the documentation of the collections and random modules.
