users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for user, user_info in users.items():
    full_name = user_info['first'].title() + " " + user_info['last'].title()
    location = user_info['location'].title()
    print(user)
    print("Full name: " + full_name)
    print("Location: " + location)
