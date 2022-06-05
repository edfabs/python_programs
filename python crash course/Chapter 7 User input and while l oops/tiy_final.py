# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwitch_order = ['BLT', 'pastrami', 'Ruben',
                   'roast beef', 'pastrami', 'croque-monsieur', 'pastrami']
print(sandwitch_order)
print('The deli has run out of pastrami\n')
finished_sandwiches = []
while 'pastrami' in sandwitch_order:
    sandwitch_order.remove('pastrami')

while sandwitch_order:
    current_sanwitch = sandwitch_order.pop()
    print("I made your " + current_sanwitch + " sandwich.")
print("\nThe list of sandwich was made")


# 7-10. Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.

responses = {}
while True:
    name = input("What is your name?")
    response = input(
        "If you could visit one place in the world, where would you go?")
    responses[name] = response
    if input("You would enter anoder participate (yes/no): ") == "no":
        break
print("---- Poll Results ----")
for name, result in responses.items():
    print(name.title() + " would like visit " + result.title())
