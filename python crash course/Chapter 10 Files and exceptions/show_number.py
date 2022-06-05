import json

filename = 'favorite_number.json'
with open(filename) as f:
    favorite_number = json.load(f)
for key, value in favorite_number.items():
    print(f"The favorite number of {key} is: {value}")
