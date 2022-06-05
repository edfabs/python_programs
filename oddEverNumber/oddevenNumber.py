number = int(input("Enter a number between 1 and 10: "))
if(number >=1 and number <=10):
    if(number%2 == 0):
        print(f"The number {number} is even")
    else:
        print(f"the number {number} is odd")
else:
    print(f"The number {number} is out of range")