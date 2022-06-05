class Privileges():
    """Class that is an a attribute of Administrator class"""

    def __init__(self, privileges="admin"):
        """methot taht initialize the class privileges"""
        self.privileges = privileges

    def show_privileges(self):
        """Method to shoe the privileges of the user"""
        if self.privileges == 'admin':
            print("You have privileges like " + self.privileges.title())
            print("You can\n\t- Add post\n\t- Delete post\n\t- Ban user")
        else:
            print("You have privileges like " + self.privileges.title())
