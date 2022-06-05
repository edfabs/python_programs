import math
a = float(input("Enter lhe long of a: "))
b = float(input("Enter the long of b: "))
c = float(input("Enter the long of c: "))
p = (a+b+c)/2
area = math.sqrt((p*(p-a)*(p-b)*(p-c)))
print(f"The perimeter is: {p} and the Area is : {area}")