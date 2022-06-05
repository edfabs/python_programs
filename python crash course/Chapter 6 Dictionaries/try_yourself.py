person = {'name': 'karla', 'last_name': 'roaro',
          'age': 34, 'city': 'mexico city'}
print(person)

favorite_number = {
    'karla': 3,
    'diego': 7,
    'carlos': 15,
    'fabian': 22,
    'alonso': 10
}

print("\nEl numero favorito de Karla es: " + str(favorite_number['karla']))
print("\nEl numero favorito de Diego es: " + str(favorite_number['diego']))
print("\nEl numero favorito de Calros es: " + str(favorite_number['carlos']))
print("\nEl numero favorito de Fabian es: " + str(favorite_number['fabian']))
print("\nEl numero favorito de Alonso es: " + str(favorite_number['alonso']))

glossary = {
    'dictionary': 'A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key.',
    'if': 'You can put any conditional test in the first line and just about any action in the indented block following the test.',
    'conditional test': 'At the heart of every if statement is an expression that can be evaluated as True or False and is called a conditional test. Python',
    'tuple': 'A tuple looks just like a list except you use parentheses instead of square brackets.',
    'list comprehensions': 'A list comprehension allows you to generate this same list in just one line of code. A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element.',
    'dictonary': 'Dictionary is a built-in Python Data Structure that is mutable. It is similar in spirit to List, Set, and Tuples. However, it is not indexed by a sequence of numbers but indexed based on keys and can be understood as associative arrays. On an abstract level, it consists of a key with an associated value.',
    'string': 'In Python, Strings are arrays of bytes representing Unicode characters. However, Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.',
    'Boolean Type': 'There can be only two types of value in the Boolean data type of Python, and that is True or False. '
}

for key, value in sorted(glossary.items()):
    print('\n' + key.title() + ':')
    print(value)

rivers = {
    'amazonas': 'brasil',
    'nilo': 'egipto',
    'misisipi': 'eua',
    'rio bravo': 'mexico'
}


for key, value in rivers.items():
    print("The " + value + " runs through " + key + ".")

for river in rivers.keys():
    print(river)
for contry in rivers.values():
    print(contry)

people = ['fabian', 'karla', 'jen', 'sarah', 'edward', 'phil']

favorite_lenguages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for encuestado in people:
    if encuestado in favorite_lenguages.keys():
        print("Thak you " + encuestado + "for responding the poll")
    else:
        print(encuestado + " you not yet taken the poll, please take the poll")
