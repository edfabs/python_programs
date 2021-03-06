class Dog():
    """a simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + "is now sitting.")

    def roll_over(self):
        """Simulate roll over in response to a command."""
        print(self.name.title() + "roll over!")


my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog name is " + my_dog.name.title() + ".")
print("My dog age is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

print("Your dog name is " + your_dog.name.title() + ".")
print("Your dog age is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()
