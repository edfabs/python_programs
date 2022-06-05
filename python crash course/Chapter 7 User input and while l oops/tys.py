# Ex 7-2 Rental Car: Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me see if I can find you a Subaru.”

# car = input("What kind of rental car would you like? ")
# print("Let me see if I can find you a " + car.title() + ".")

# 7-2. Restaurant Seating: Write a program that asks the user how manypeople are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.

# restaurante = int(input("How manypeople are in the dinner group? "))
# if restaurante >= 8:
#     print("You'll have to wait for a table")
# else:
#     print("You can pass to your table")

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.

multiples = int(input("In a number to know is a multipler of ten: "))
if multiples % 10 == 0:
    print("The number " + str(multiples) + " is multipler of 10")
else:
    print("The number " + str(multiples) + " is not multipler of 10")
