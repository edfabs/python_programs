num = int(input("Enter the number to do the factorial: "))
i = 0
factorial = 1
while i != num:
    factorial = factorial * (num - i)
    i = i + 1

print(f"The factorial of the number entered is: {factorial}")