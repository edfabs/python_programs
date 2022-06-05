import json


def show_number():
    """Show the favorite number of a user"""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
        return favorite_number
    except FileNotFoundError:
        return None


def new_favorite_number():
    """Save a favorite number in a json file"""
    filename = 'favorite_number.json'
    favorite_number = input("What is you favorite number:")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    return favorite_number


def get_favorite_number():
    """Revew if the user save your favorite number"""
    favorite_number = show_number()
    if favorite_number:
        print(f"Your favorite number is: {favorite_number}")
    else:
        favorite_number = new_favorite_number()
        print(f"Your number {favorite_number}, was saved")


get_favorite_number()
