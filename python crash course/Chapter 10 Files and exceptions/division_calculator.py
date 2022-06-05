# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")


print("Give me two numbers and i divide (press 'q to out of the programm)")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero, try again")
    else:
        print(answer)
