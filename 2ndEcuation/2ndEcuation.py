import cmath

print("program what resolve a 2nd Ecuation")
a = int(input("Enter the value of the quadratic term: "))
b = int(input("Enter the value of lineal term: "))
c = int(input("Enter the value of independent term: "))

print(f"The form of the ecuations is {a}x^2+{b}x+{c}")

d = (b**2)-(4*a*c)

x1 = (-b-cmath.sqrt(d))/(2*a)
x2 = (-b+cmath.sqrt(d))/(2*a)

print(f"The value of x1 is: {x1} and x2 is: {x2}")