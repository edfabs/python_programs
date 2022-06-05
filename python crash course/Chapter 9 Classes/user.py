class User():
    """Clase usuario"""

    def __init__(self, first_name, last_name, username, age, email, privileges='user'):
        """Initialize the user instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.email = email
        self.login_attempts = 0
        self.privileges = privileges

    def descriptive_user(self):
        """Method to describe the user"""
        print("\nThe user names is: " + self.first_name.title() + " " + self.last_name.title() + " he's " +
              str(self.age) + " , his name is: " + self.username + " and his email is " + self.email)

    def great_user(self):
        """Method to personalize a greeting to the user"""
        print("\nHello " + self.first_name.title() + " " +
              self.last_name.title() + " you are the best user")

    def increment_login_attempts(self):
        """method to incement the attempts one by one"""
        self.login_attempts += 1

    def reste_login_attempts(self):
        """method to reset the number of attempts of login"""
        self.login_attempts = 0
