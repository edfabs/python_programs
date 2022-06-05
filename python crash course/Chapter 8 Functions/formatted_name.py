from black import get_future_imports


def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a formatted full name."""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hook', 'lee')
print(musician)

# This is an infinite loop!
while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' an any time to quit)")
    f_name = input("First name: ")
    if f_name == "q":
        break
    l_name = input("Last name: ")
    if l_name == "q":
        break
    formated_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formated_name + "!")
