ratings = {"F" : 4, "E": 5, "D" : 6, "C" : 7, "B" : 8, "A" : 9}
rating = input("Enter the rating of the student: ")
if (rating in ratings.keys()):
    print(f"The Rating of the student is: {ratings[rating]}")
else:
    print(f"the calification {rating} is invalid")