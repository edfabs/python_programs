favorite_lenguages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_lenguages.items():
    print(name.title() + "'s favorite lenguage is " + language.title() + ".")
print("\n")
for name in favorite_lenguages.keys():
    print(name.title())
print("\n")
for name in favorite_lenguages:
    print(name.title())
print("\n")
friends = ['phil', 'sarah']
for name in favorite_lenguages.keys():
    print(name.title())
    if name in friends:
        print("Hi" + name.title() + ", I see your favorite lenguage is " +
              favorite_lenguages[name].title() + "!")

if 'enri' not in favorite_lenguages.keys():
    print('Enri, plase take our poll')

for name in sorted(favorite_lenguages.keys()):
    print(name.title() + ", tank you for taking the poll.")

print("\n The folowing lenguage have been mentioned:")
for lenguages in set(favorite_lenguages.values()):
    print(lenguages.title())

favorite_lenguages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_lenguages.items():
    print(" \nLos lenguages favoritos de " + name.title() + " son:")
    for language in languages:
        print("\t" + language.title())
