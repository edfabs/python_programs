usernames = ['admin', 'edfabs', 'adrian', 'karla', 'diego', 'carlos']

for user in usernames:
    if user == 'admin':
        print('Hello admin, would you see a status report?')
    else:
        print('Hello ' + user + ', thank you for logging in again.')
