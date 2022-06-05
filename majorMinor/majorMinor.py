a = int(input("Enter the first number: "))
b = int(input("Enter the secont number: "))
c = int(input("Enter the third number: "))

if(a > b):
    if(a > c):
        if(b > c):
            print(f"a: {a}, b: {b}, c: {c}")
        else:
            print(f"a: {a}, c: {c}, b: {b}")
    elif(b > a):
        print(f"c: {c}, b: {b}, a: {a}")
    else:
        print(f"c: {c},a: {a}, b: {b}")
elif(b > c):
    if(c > a):
        print(f"b: {b}, c: {c}, a: {a}")
    else:
        print(f"b: {b}, a: {a}, c: {c}")
else:
    if(b > a):
        print(f"c: {c}, b: {b}, a: {a}")
    else:
        print(f"c: {c},a: {a}, b: {b}")

