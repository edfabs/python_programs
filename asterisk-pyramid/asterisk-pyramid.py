rows = 5
columns = 9

for row in reversed(range(rows)):
    for space in reversed(range(row)):
        print(" ", end=" ")
    for column in reversed(range(columns - (row)*2)):
        print("*",end=" ")     
    print("\r")