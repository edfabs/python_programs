# Start with user that needs to be verifued,
# adn empty list to hold confirmed users.

unconfirmed_users = ['alice', 'fabian', 'candance']
confirmed_users = []

# Verify eacu user until there are no more unconfirmed user.
# Move each virified user into the list od confirmed uses.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

    # Display all confirmed users
    print("\nthe folloging users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())
