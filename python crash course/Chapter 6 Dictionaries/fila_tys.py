emails = {
    'ckkarlaroaro@gmail.com': {
        'fname': 'karla',
        'lname': 'roaro',
        'age': 34,
        'location': 'mexico city',
    },
    'suchettr@gmail.com': {
        'fname': 'fabian',
        'lname': 'suchett',
        'age': 33,
        'location': 'mexico city',
    },
    'dfabsur@gmail.com': {
        'fname': 'diego',
        'lname': 'suchett',
        'age': 10,
        'location': 'mexico city',
    },
}

for user, user_info in emails.items():
    full_name = user_info['fname'].title() + " " + user_info['lname'].title()
    age = user_info['age']
    location = user_info['location'].title()
    print(full_name + " con " + str(age) +
          " de edad " + " viviendo en " + location)


gary = {
    'kind': 'dog',
    'owner': 'karla',
}

nayu = {
    'kind': 'dog',
    'owner': 'silvia',
}

luna = {
    'kind': 'cat',
    'owner': 'carlos',
}

pets = [gary, nayu, luna]

for pet in pets:
    print(pet)

favorite_places = {
    'karal': ['playa', 'casa', 'trabajo'],
    'carlos': ['playa', 'casa', 'escuela'],
    'fabian': ['montna', 'casa', 'negocio'],
}

for key, value in favorite_places.items():
    print("a " + key.title() + " le gusta mucho los siguientes  lugares:")
    print(value)

favorite_numbers = {
    'karla': [3, 5, 4],
    'diego': [7, 9, 10],
    'carlos': [15],
    'fabian': [22, 30],
    'alonso': [10, 30, 33],
}

for name, numbers in favorite_numbers.items():
    print("numeros favoritos de " + name.title())
    print(numbers)

cities = {
    'ciudad de mexico': {
        'contry': 'mexico',
        'population': 8855000,
        'fact': 'Conocido por las playas en el Pacifico y en el golfo de Mexico',
    },
    'montreal': {
        'contry': 'canada',
        'population': 1780000,
        'fact': 'Se extiende desde la frontera con EUA hasta el circulo polar artico',
    },
    'new york': {
        'contry': 'eua',
        'population': 8419000,
        'fact': 'En su centro se encuentra Manhattan',
    },
}

for city, city_info in cities.items():
    print(city.title())
    print("Ubicado en el pais de  " + city_info['contry'].title() + " con una poblacion de " + str(
        city_info['population']) + " " + city_info['fact'])
