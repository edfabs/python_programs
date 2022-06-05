# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

# prompt = "\nEnter a list of topping for you pizza: "
# prompt += "\n(enter a quit to end the list) "
# while True:
#     topping = input(prompt)
#     if topping == 'quit':
#         break
#     else:
#         print(topping)

# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

# prompt = "Enter your age to determine the proce of a ticke (enter 'quit' to end the buy): "
# while True:
#     age = input(prompt)
#     if age != 'quit':
#         if int(age) < 3:
#             price = 0
#         elif int(age) < 12:
#             price = 10
#         else:
#             price = 15
#         print("Your age is: " + str(age) +
#               "The cost of your ticket is: " + str(price))
#     else:
#         break

# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once: • Use a conditional test in the while statement to stop the loop. • Use an active variable to control how long the loop runs. • Use a break statement to exit the loop when the user enters a 'quit' value.

# prompt = "Enter your age to determine the proce of a ticke (enter 'quit' to end the buy): "
# active = True
# while active:
#     age = input(prompt)
#     if age != 'quit':
#         if int(age) < 3:
#             price = 0
#         elif int(age) < 12:
#             price = 10
#         else:
#             price = 15
#         print("Your age is: " + str(age) +
#               "The cost of your ticket is: " + str(price))
#     else:
#         active = False

# 7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press CTRL-C or close the window displaying the output.)

while True:
    print('loop')
