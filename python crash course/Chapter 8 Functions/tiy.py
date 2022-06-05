# 8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly

from ast import Continue
from itertools import count
from threading import current_thread


def display_message(learner):
    """This function is to make a message to learn inthis course"""
    print(learner.title() +
          " In this course you learn to do stuf that will make earn money")


display_message('Fabian')

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.


def favorite_book(title):
    """print a message whit the name of a book"""
    print("One of my favorite book is " + title.title() + ".")


favorite_book('Python crash course')

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.


def make_shirt(size, message):
    print("The size of the t-shit is: " + size)
    print("The mssage to print in the t-shirt is: " + message)


make_shirt('m', 'The capitalisim is god')
make_shirt(message='The capitalisim i the ostia', size='M')

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

print("Ex8-4")


def make_shirt(size="l", message="I love Python"):
    if(size == "l" or size == "m"):
        message = "I love Python"
    else:
        message = 'Diferente message'

    print("The size of the t-shit is: " + size)
    print("The mssage to print in the t-shirt is: " + message)


make_shirt('m', 'The capitalisim is god')
make_shirt(message='The capitalisim i the ostia', size='m')
make_shirt('xl')
make_shirt('m')
make_shirt('s')

print("Ex 8-5")
# 8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.


def describe_city(city, country='mexico'):
    print(city.title() + " is in " + country.title())


describe_city("ciudad de mexico")
describe_city("guadalajara")
describe_city("Ontario", "canada")

# 8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:"Santiago, Chile" Call your function with at least three city-country pairs, and print the value that’s returned.


def city_country(city, country):
    formatt = "\"" + city.title() + ", " + country.title() + "\""
    return formatt


print(city_country("Santiago", "chile"))

# 8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.


def make_album(artist_name, album_title, tracks=''):
    album = {"artista": artist_name.title(), "album": album_title.title()}
    if tracks:
        album['tracks'] = tracks
    return album


album = make_album("jimi hendrix", "expirience")
print(album)
album = make_album("john lennon", "imagine")
print(album)
album = make_album("the beatles", "Srgt. Peppers")
print(album)
album = make_album("metallica", "black", 14)
print(album)

# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.

while True:
    print("This program create a dictionary whit artis and album")
    print("(entrer 'q' letter to out of the program)")
    artist = input("Enter the Artist: ")
    if artist == 'q':
        break
    album = input("Enter the nam of the album: ")
    if album == 'q':
        break
    album_dictionary = make_album(artist, album)
    print(album_dictionary)

# 8-9. Magicians: Make a list of magician’s names. Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# 8-10. Great Magicians: Start with a copy of your program from Exercise 8-9. Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician’s name. Call show_magicians() to see that the list has actually been modified.

# 8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the function make_great() with a copy of the list of magicians’ names. Because the original list will be unchanged, return the new list and store it in a separate list. Call show_magicians() with each list to show that you have one list of the original names and one list with the Great added to each magician’s name.


def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())


def make_greate(magicians, greate_magicians):
    while magicians:
        current_magician = magicians.pop()
        greate_magicians.append("The greate " + current_magician.title())
    return greate_magicians


magicians = ['haudiny', 'david coperfield', 'septien']
greate_magicians = []
greate_magicians = make_greate(magicians[:], greate_magicians)
show_magicians(greate_magicians)
show_magicians(magicians)

# 8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that is being ordered. Call the function three times, using a different number of arguments each time.


def make_sandwich(*toppings):
    print("\nMaking the sandwich")
    for topping in toppings:
        print("- " + topping)


make_sandwich('mayonesa', 'jamon', 'queso')
make_sandwich('mayonesa', 'cebolla', 'jitomate', 'queso', 'jamon')
make_sandwich('queso', 'frijoles', 'crema', 'lechuga')

# 8-13. User Profile: Start with a copy of user_profile.py from page 153. Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.


def build_profile(fname, lname, **profile_info):
    profile = {'first_name': fname, 'last_name': lname}
    for key, value in profile_info.items():
        profile[key] = value
    print('\nPersona')
    for key, value in profile.items():
        print(key.title() + ': ' + value.title())


build_profile('fabian', 'suchett', employee='engineer', team='chiefs')

# 8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) Print the dictionary that’s returned to make sure all the information was stored correctly.


def car(manufacturer, model_name, **car_information):
    car_info = {'manufacturer': manufacturer, 'model name': model_name}
    for key, value in car_information.items():
        car_info[key] = value
    print("\n Car information")
    print(car_info)


car("toyota", 'corolla', tow_package=True, plazas=5)

# 8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.

# 8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:

# 8-17. Styling Functions: Choose any three programs you wrote for this chapter, and make sure they follow the styling guidelines described in this section.
