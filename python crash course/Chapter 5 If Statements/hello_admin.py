usernames = ['admin', 'edfabs', 'adrian', 'karla', 'diego', 'carlos']
usernames = []
if usernames:
    for user in usernames:
        if user == 'admin':
            print('Hello ' + user + ', would you see a status report?')
        else:
            print('Hello ' + user + ', thank you for logging in again.')
else:
    print('We need to find some user!')

current_user = ['admin', 'edfabs', 'adrian', 'diego', 'carlos', 'fabian']
new_user = ['admin', 'Fabian', 'karla', 'diego', 'JOHN']

for user in new_user:
    user = user.lower()
    if user in current_user:
        print(user + ' is in use, pleas change the name!')
    else:
        print(user + ' is available!')

numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        message = 'st'
    elif number == 2:
        message = 'nd'
    elif number == 3:
        message = 'rd'
    else:
        message = 'th'
    print(str(number) + message)
