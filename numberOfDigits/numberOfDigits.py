from string import digits


number = int(input("Enter a number to determine the number of digits: "))
one = [n for n in range(10)]
two = [n for n in range(10,100)]
three = [n for n in range(100, 1000)]
four = [n for n in range(1000, 10000)]
five = [n for n in range(10000,100000)]
six = [n for n in range(100000, 1000000)]
digits = {1:one, 2:two, 3:three, 4:four, 5:five, 6:six}
for digit in digits:
    if number in digits[digit]:
        print(f"The number of digits in the number entered is: {digit}")    