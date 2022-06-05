def greet_user(username):
    """Display a simple greeting for each user in the list"""
    for name in usernames:
        print("Hello " + name + "!")


usernames = ['hannah', 'ty', 'margot']
greet_user(usernames)
