def build_person(first_name, last_name, age=''):
    """Return a dictonary of a information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix')
print(musician)

musician = build_person('fabian', 'suchett', 33)
print(musician)
